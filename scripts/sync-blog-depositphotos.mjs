#!/usr/bin/env node
/**
 * Lädt für alle Blog-Detailseiten fehlende JPGs von Depositphotos Enterprise API
 * nach website/img/blog-bento/ und website/img/blog-sections/.
 * Credentials nur aus .env (DP_API_KEY, DP_USER, DP_PASS).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '..');
const WEBSITE = path.join(REPO, 'website');
const BLOGS_DIR = path.join(WEBSITE, 'blogs');
const API_BASE = 'https://api.depositphotos.com';
const MANIFEST_PATH = path.join(__dirname, 'blog-images-manifest.json');
const MIN_BYTES = 8_000;
const DELAY_MS = 280;
const FORCE = process.argv.includes('--force');

function loadEnv() {
  const envPath = path.join(REPO, '.env');
  if (!fs.existsSync(envPath)) {
    throw new Error('.env fehlt — DP_API_KEY, DP_USER, DP_PASS setzen');
  }
  const env = {};
  for (const line of fs.readFileSync(envPath, 'utf8').split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i > 0) env[t.slice(0, i).trim()] = t.slice(i + 1).trim();
  }
  return env;
}

const SLUG_EN = {
  'finanzen-versicherung': 'finance insurance Germany',
  'crypto-web3': 'cryptocurrency blockchain',
  'energie-solar': 'solar energy renewable home',
  'trading': 'stock market trading chart',
  'immobilien': 'real estate property investment',
  'ki-tech': 'artificial intelligence technology',
  'automationen': 'business workflow automation',
  'karriere-hr': 'human resources recruitment career',
  'coaching-mindset': 'business coaching mindset',
  'artikel-pkv-vs-gkv-2026': 'private health insurance doctor Germany',
  'artikel-bitcoin-institutionen-2026': 'bitcoin institutional investment',
  'artikel-solaranlage-2026': 'solar panels house roof',
  'artikel-solaranlage-ratgeber-2026': 'solar panels house roof photovoltaic',
  'maschinen-die-dienen-davinci-pfad': 'technology innovation future human machine',
  'artikel-claude-vs-chatgpt-unternehmen-2026': 'AI chatbot business laptop',
  'artikel-eigentumswohnung-kaufen-2026': 'apartment keys real estate buying',
  'artikel-produktivitaet-adhs-systeme': 'productive home office focus',
};

const SIDE_VARIANTS = [
  'technology digital',
  'team meeting professional',
  'planning documents business',
];

const SECTION_HINTS = {
  1: 'overview strategy professional',
  2: 'tools technology dashboard',
  3: 'comparison analysis documents',
  4: 'automation artificial intelligence',
  5: 'FAQ customer support helpdesk',
};

function slugFromFilename(name) {
  const m = name.match(/^(.+)-(main|s[123]|section-\d+)$/);
  return m ? m[1] : name.replace(/\.jpg$/, '');
}

function topicForSlug(slug) {
  if (SLUG_EN[slug]) return SLUG_EN[slug];
  return slug
    .replace(/^artikel-/, '')
    .replace(/-2026$/, '')
    .replace(/-/g, ' ');
}

function queryForPath(webPath, alt) {
  const name = path.basename(webPath, '.jpg');
  const slug = slugFromFilename(name);
  const base = topicForSlug(slug);

  const secM = name.match(/-section-(\d+)$/);
  if (secM) {
    const hint = SECTION_HINTS[Number(secM[1])] || 'business concept';
    return `${base} ${hint}`;
  }
  if (alt && alt.includes('Visuelle Zusammenfassung')) {
    const m = alt.match(/Visuelle Zusammenfassung:\s*([^|]+)/i);
    if (m) return `${m[1].replace(/&amp;/g, '&').trim()} hero banner`;
  }
  if (name.endsWith('-main')) return `${base} hero banner professional`;
  const sm = name.match(/-s([123])$/);
  if (sm) return `${base} ${SIDE_VARIANTS[Number(sm[1]) - 1]}`;
  const sec = name.match(/-section-(\d+)$/);
  if (sec) return `${base} concept section ${sec[1]}`;
  return `${base} business photo`;
}

function collectImageJobs() {
  const jobs = new Map();
  for (const file of fs.readdirSync(BLOGS_DIR).filter((f) => f.endsWith('.html'))) {
    const html = fs.readFileSync(path.join(BLOGS_DIR, file), 'utf8');
    const re = /<img[^>]+src="(\/img\/blog-(?:bento|sections)\/[^"]+\.jpg)"[^>]*>/gi;
    let m;
    while ((m = re.exec(html)) !== null) {
      const webPath = m[1];
      const tag = m[0];
      const altM = tag.match(/alt="([^"]*)"/i);
      const alt = altM ? altM[1].replace(/&amp;/g, '&') : '';
      const query = queryForPath(webPath, alt);
      if (!jobs.has(webPath)) jobs.set(webPath, { webPath, query, source: file });
    }
  }
  return [...jobs.values()];
}

async function apiGet(params) {
  const url = `${API_BASE}/?${params.toString()}`;
  const res = await fetch(url);
  return res.json();
}

let sessionId = null;
let apiKey = null;

async function login(env) {
  apiKey = env.DP_API_KEY;
  const data = await apiGet(
    new URLSearchParams({
      dp_apikey: apiKey,
      dp_command: 'loginEnterprise',
      dp_login_user: env.DP_USER,
      dp_login_password: env.DP_PASS,
    }),
  );
  if (data.type !== 'success' || !data.sessionid) {
    throw new Error(`Login fehlgeschlagen: ${JSON.stringify(data)}`);
  }
  sessionId = data.sessionid;
  process.stderr.write(`✅ Login OK — Session ${sessionId.slice(0, 12)}…\n`);
}

async function trySearch(query) {
  const data = await apiGet(
    new URLSearchParams({
      dp_apikey: apiKey,
      dp_session_id: sessionId,
      dp_command: 'search',
      dp_search_query: query.slice(0, 120),
      dp_search_limit: 8,
      dp_search_sort: 4,
      dp_search_orientation: 'horizontal',
      dp_search_photo: 1,
      dp_search_vector: 0,
      dp_search_nudity: 0,
      dp_watermark: 'neutral',
    }),
  );
  if (data.type !== 'success' || !data.result?.length) return null;
  const top = data.result.slice(0, 8);
  const best = top.reduce((a, b) =>
    (b.downloads || 0) > (a.downloads || 0) ? b : a,
  );
  const url =
    best.url_big ||
    best.thumb_max ||
    best.huge_thumb ||
    best.large_thumb ||
    best.url2 ||
    best.medium_thumbnail;
  if (!url) return null;
  return { id: best.id, title: best.title || '', url };
}

async function searchImage(query) {
  const words = query.split(/\s+/).filter(Boolean);
  const attempts = [
    query,
    words.slice(0, 6).join(' '),
    words.slice(0, 4).join(' '),
    words.slice(0, 2).join(' '),
    'business professional office',
  ];
  const seen = new Set();
  for (const q of attempts) {
    const key = q.toLowerCase();
    if (seen.has(key) || !q.trim()) continue;
    seen.add(key);
    const img = await trySearch(q);
    if (img) return img;
    await sleep(120);
  }
  return null;
}

async function downloadToFile(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} für ${url}`);
  const buf = Buffer.from(await res.arrayBuffer());
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.writeFileSync(dest, buf);
  return buf.length;
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function main() {
  const env = loadEnv();
  if (!env.DP_API_KEY || !env.DP_USER || !env.DP_PASS) {
    throw new Error('DP_API_KEY, DP_USER, DP_PASS in .env erforderlich');
  }

  const jobs = collectImageJobs();
  process.stderr.write(`📋 ${jobs.length} eindeutige Blog-Bildpfade\n`);

  let manifest = {};
  if (fs.existsSync(MANIFEST_PATH)) {
    try {
      manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
    } catch {
      manifest = {};
    }
  }

  await login(env);

  let ok = 0;
  let skip = 0;
  let fail = 0;

  for (let i = 0; i < jobs.length; i++) {
    const { webPath, query } = jobs[i];
    const dest = path.join(WEBSITE, webPath.replace(/^\//, ''));
    const rel = webPath;

    if (!FORCE && fs.existsSync(dest)) {
      const st = fs.statSync(dest);
      if (st.size >= MIN_BYTES) {
        skip++;
        continue;
      }
    }

    process.stderr.write(`[${i + 1}/${jobs.length}] ${rel}\n   🔍 ${query.slice(0, 70)}\n`);

    try {
      const img = await searchImage(query);
      if (!img) {
        process.stderr.write('   ❌ keine Treffer\n');
        fail++;
        await sleep(DELAY_MS);
        continue;
      }
      const bytes = await downloadToFile(img.url, dest);
      manifest[rel] = {
        mediaId: img.id,
        title: img.title,
        url: img.url,
        query,
        bytes,
        at: new Date().toISOString(),
      };
      fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2));
      process.stderr.write(`   ✅ ${img.id} — ${bytes} bytes — ${(img.title || '').slice(0, 50)}\n`);
      ok++;
    } catch (e) {
      process.stderr.write(`   ❌ ${e.message}\n`);
      fail++;
    }
    await sleep(DELAY_MS);
  }

  process.stderr.write(`\nFertig: ${ok} neu, ${skip} übersprungen, ${fail} fehlgeschlagen\n`);
  console.log(JSON.stringify({ ok, skip, fail, total: jobs.length }, null, 2));
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
