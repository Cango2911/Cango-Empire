#!/usr/bin/env node
/**
 * Blog-Bilder per Depositphotos Enterprise API — kontextgenau pro Abschnitt.
 * Parst H2-Titel + Absatztext, baut englische Kern-Keywords, vermeidet Duplikate pro Seite.
 *
 * Nutzung:
 *   node scripts/sync-blog-depositphotos.mjs              # nur fehlende/kleine
 *   node scripts/sync-blog-depositphotos.mjs --force      # alle neu
 *   node scripts/sync-blog-depositphotos.mjs --force --keep-covers  # ohne Hero-main
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
const DELAY_MS = 300;
const FORCE = process.argv.includes('--force');
const KEEP_COVERS = process.argv.includes('--keep-covers');

/** Deutsch → englische Stock-Suchbegriffe (Kern-Keywords) */
const PHRASE_MAP = [
  [/etf[\s-]*sparpl[aä]n|sparplan/i, 'ETF savings plan investment portfolio chart'],
  [/versicherung.*vergleich|versicherungen intelligent/i, 'insurance comparison documents policy'],
  [/berufsunf[aä]higkeit|\bbu\b/i, 'disability insurance protection family umbrella'],
  [/pkv|private kranken/i, 'private health insurance doctor stethoscope card'],
  [/gkv|gesetzlich.*kranken|solidarisch.*beitrag/i, 'statutory health insurance hospital Germany'],
  [/krankenversicherung|gesundheits?vorsorge/i, 'health insurance medical checkup'],
  [/bitcoin|btc\b/i, 'bitcoin gold coin cryptocurrency chart institutional'],
  [/krypto|crypto|web3|defi/i, 'cryptocurrency blockchain digital finance'],
  [/steuer.*krypto|krypto.*steuer/i, 'cryptocurrency tax documents calculator'],
  [/solar|photovoltaik|pv-anlage/i, 'solar panels house roof sunshine photovoltaic'],
  [/w[aä]rmepumpe/i, 'air source heat pump modern house energy'],
  [/strom.*sparen|stromanbieter|energietarif/i, 'electricity bill energy saving light bulb'],
  [/cfd|trading|broker|aktien|börse/i, 'stock trading chart candlestick forex screen'],
  [/technische analyse|candlestick|rsi/i, 'technical analysis trading chart indicators'],
  [/immobil|pflegeimmobil|kapitalanlage.*immobil/i, 'real estate investment property building'],
  [/eigentumswohnung|wohnung kaufen|miete/i, 'apartment keys buying real estate handshake'],
  [/ki\b|künstliche intelligenz|chatgpt|claude|llm/i, 'artificial intelligence AI chatbot laptop business'],
  [/n8n|zapier|automatisierung|workflow/i, 'business process automation workflow diagram software'],
  [/bewerbung|recruiting|karriere|hr\b|personal/i, 'job interview recruitment HR talent'],
  [/gehalt|verhandlung/i, 'salary negotiation business meeting handshake'],
  [/coaching|mindset|enneagramm|persönlichkeit/i, 'business coaching mentor mindset workshop'],
  [/adhs|produktivit|fokus|konzentration/i, 'organized productive workspace focus minimal desk'],
  [/finanztool|vermögen|portfolio|anlage/i, 'personal finance dashboard wealth management'],
  [/buchhaltung|datev|rechnung/i, 'accounting bookkeeping invoice laptop office'],
  [/steuer|steueroptim/i, 'tax planning documents calculator business'],
  [/faq|häufige fragen/i, 'FAQ help support question answer customer service'],
  [/checkliste|gespräch.*expert/i, 'checklist consultation meeting professional advisor'],
  [/denkfehler|fehler vermeiden/i, 'mistake warning decision thinking business'],
  [/institutionell|adoption|etf.*institut/i, 'institutional investment finance corporate'],
  [/energie.*effizienz|renewable|nachhaltig/i, 'renewable energy sustainability green technology'],
  [/robot|maschine.*dienen|davinci/i, 'human robot collaboration innovation technology'],
  [/compliance|regulierung|rechtlich/i, 'legal compliance regulation documents business'],
  [/signal.*pipeline|algorithmus/i, 'algorithm data pipeline trading technology'],
  [/risikomanagement/i, 'risk management finance protection shield chart'],
  [/reporting|performance.*track/i, 'financial reporting analytics dashboard screen'],
];

const WORD_MAP = {
  finanzen: 'finance money',
  versicherung: 'insurance',
  energie: 'energy power',
  solar: 'solar panels',
  trading: 'stock trading',
  immobilien: 'real estate',
  automatisierung: 'automation technology',
  unternehmen: 'business corporate',
  digital: 'digital technology',
  beratung: 'consultation advisor',
  vergleich: 'comparison choice',
  investition: 'investment growth',
  sicherheit: 'security protection',
  familie: 'family protection',
  arzt: 'doctor medical',
  krankenhaus: 'hospital medical',
  vertrag: 'contract document signing',
  laptop: 'laptop business',
  team: 'business team meeting',
  daten: 'data analytics dashboard',
};

const STOP = new Set(
  'der die das und oder ein eine einer eines einem den dem des von zu im in auf für mit ist sind war werden als auch nicht nur noch sehr mehr als bei nach über durch ohne bis zum zur beim bereits heute jahr jahre 2026 2025 dach raum deutschland'.split(
    ' ',
  ),
);

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

function decodeHtml(s) {
  return s
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>');
}

function stripHtml(s) {
  return decodeHtml(s)
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Aus Titel + Absatz englische Kern-Keywords für Depositphotos */
function buildContextQuery(title, paragraph = '', pageTopic = '') {
  const combined = `${title} ${paragraph}`.toLowerCase();
  const parts = [];

  for (const [re, en] of PHRASE_MAP) {
    if (re.test(combined)) parts.push(en);
  }

  const words = combined
    .replace(/[^\wäöüß\s-]/g, ' ')
    .split(/\s+/)
    .filter((w) => w.length > 2 && !STOP.has(w));

  for (const w of words) {
    const stem = w.replace(/(en|er|em|es|e|n|s)$/i, '').slice(0, 6);
    for (const [de, en] of Object.entries(WORD_MAP)) {
      if (w.includes(de) || de.startsWith(stem)) parts.push(en);
    }
  }

  if (parts.length === 0 && pageTopic) parts.push(pageTopic);

  const unique = [...new Set(parts.join(' ').split(/\s+/))].filter((w) => w.length > 2);
  const query = unique.slice(0, 12).join(' ');
  return query || 'business professional modern office';
}

function extractParagraphAfter(html, imgPath) {
  const idx = html.indexOf(imgPath);
  if (idx < 0) return '';
  const slice = html.slice(idx, idx + 4000);
  const paras = [...slice.matchAll(/<p class="blog-content__section-text">([\s\S]*?)<\/p>/g)];
  return paras
    .slice(0, 2)
    .map((p) => stripHtml(p[1]))
    .join(' ');
}

function parseBlogPage(html, sourceFile) {
  const articleSlug = sourceFile.replace(/\.html$/, '');
  const jobs = [];

  const h1 = html.match(/class="blog-header__title"[^>]*>([^<]+)/i);
  const pageTitle = h1 ? stripHtml(h1[1]) : articleSlug.replace(/-/g, ' ');

  const intro = html.match(/class="blog-content__intro"[^>]*>([\s\S]*?)<\/div>/i);
  const introText = intro ? stripHtml(intro[1]) : '';
  const pageTopic = buildContextQuery(pageTitle, introText);

  const sections = [];
  const sectionRe =
    /<h2 class="blog-content__section-title">([^<]+)<\/h2><figure class="section-visual"><img[^>]+src="(\/img\/blog-sections\/[^"]+\.jpg)"/gi;
  let m;
  while ((m = sectionRe.exec(html)) !== null) {
    const title = decodeHtml(m[1].trim());
    const webPath = m[2];
    const paragraph = extractParagraphAfter(html, webPath);
    const query = buildContextQuery(title, paragraph, pageTopic);
    sections.push({ webPath, query, title, paragraph: paragraph.slice(0, 120) });
  }

  for (const s of sections) {
    jobs.push({
      webPath: s.webPath,
      query: s.query,
      source: sourceFile,
      articleSlug,
      kind: 'section',
      context: s.title,
    });
  }

  // Bento: main = Seitenthema; s1–s3 = erste drei Abschnitte (unterschiedliche Motive)
  const bentoMain = html.match(
    /class="blog-visual-bento__main"[\s\S]*?src="(\/img\/blog-bento\/[^"]+-main\.jpg)"/i,
  );
  if (bentoMain) {
    jobs.push({
      webPath: bentoMain[1],
      query: buildContextQuery(pageTitle, introText),
      source: sourceFile,
      articleSlug,
      kind: 'bento-main',
      context: pageTitle,
    });
  }

  const sideRe =
    /class="blog-visual-bento__side"[\s\S]*?src="(\/img\/blog-bento\/[^"]+-s[123]\.jpg)"/gi;
  const sides = [];
  while ((m = sideRe.exec(html)) !== null) sides.push(m[1]);

  sides.forEach((webPath, i) => {
    const sec = sections[i];
    const query = sec
      ? sec.query
      : buildContextQuery(
          `${pageTitle} aspect ${i + 1}`,
          introText,
          pageTopic,
        );
    jobs.push({
      webPath,
      query,
      source: sourceFile,
      articleSlug,
      kind: `bento-s${i + 1}`,
      context: sec?.title || pageTitle,
    });
  });

  return jobs;
}

function collectImageJobs() {
  const byPath = new Map();
  for (const file of fs.readdirSync(BLOGS_DIR).filter((f) => f.endsWith('.html'))) {
    const html = fs.readFileSync(path.join(BLOGS_DIR, file), 'utf8');
    for (const job of parseBlogPage(html, file)) {
      if (KEEP_COVERS && job.kind === 'bento-main') continue;
      if (!byPath.has(job.webPath)) byPath.set(job.webPath, job);
    }
  }
  return [...byPath.values()];
}

function groupByArticle(jobs) {
  const groups = new Map();
  for (const j of jobs) {
    if (!groups.has(j.articleSlug)) groups.set(j.articleSlug, []);
    groups.get(j.articleSlug).push(j);
  }
  return groups;
}

async function apiGet(params) {
  const res = await fetch(`${API_BASE}/?${params.toString()}`);
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
  process.stderr.write(`✅ Login OK\n`);
}

function pickUrl(item) {
  return (
    item.url_big ||
    item.thumb_max ||
    item.huge_thumb ||
    item.large_thumb ||
    item.url2 ||
    item.medium_thumbnail
  );
}

async function trySearch(query, excludeIds = new Set(), limit = 12) {
  const data = await apiGet(
    new URLSearchParams({
      dp_apikey: apiKey,
      dp_session_id: sessionId,
      dp_command: 'search',
      dp_search_query: query.slice(0, 120),
      dp_search_limit: String(limit),
      dp_search_sort: 4,
      dp_search_orientation: 'horizontal',
      dp_search_photo: 1,
      dp_search_vector: 0,
      dp_search_nudity: 0,
      dp_watermark: 'neutral',
    }),
  );
  if (data.type !== 'success' || !data.result?.length) return [];

  return data.result
    .filter((item) => !excludeIds.has(String(item.id)))
    .map((item) => ({
      id: String(item.id),
      title: item.title || '',
      url: pickUrl(item),
      downloads: item.downloads || 0,
    }))
    .filter((item) => item.url);
}

async function searchImage(query, excludeIds) {
  const words = query.split(/\s+/).filter(Boolean);
  const attempts = [
    query,
    words.slice(0, 8).join(' '),
    words.slice(0, 5).join(' '),
    words.slice(0, 3).join(' '),
  ];
  const seen = new Set();
  for (const q of attempts) {
    const key = q.toLowerCase();
    if (seen.has(key) || !q.trim()) continue;
    seen.add(key);
    const results = await trySearch(q, excludeIds);
    if (results.length) {
      const best = results.reduce((a, b) => (b.downloads > a.downloads ? b : a));
      return best;
    }
    await sleep(100);
  }
  return null;
}

async function downloadToFile(url, dest) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
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
  const jobs = collectImageJobs();
  const groups = groupByArticle(jobs);

  process.stderr.write(
    `📋 ${jobs.length} Bilder · ${groups.size} Artikel · Kontext-Suche${KEEP_COVERS ? ' (ohne Hero-Cover)' : ''}\n`,
  );

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
  let n = 0;

  for (const [slug, articleJobs] of groups) {
    const usedIds = new Set();
    // Bereits vorhandene Cover (Hero) nicht in Abschnitten wiederholen
    for (const job of articleJobs) {
      if (job.kind === 'bento-main') continue;
      const mainPath = `/img/blog-bento/${slug}-main.jpg`;
      const prev = manifest[mainPath];
      if (prev?.mediaId) usedIds.add(String(prev.mediaId));
    }
    process.stderr.write(`\n📄 ${slug} (${articleJobs.length} Bilder)\n`);

    for (const job of articleJobs) {
      n++;
      const { webPath, query, context, kind } = job;
      const dest = path.join(WEBSITE, webPath.replace(/^\//, ''));

      if (!FORCE && fs.existsSync(dest) && fs.statSync(dest).size >= MIN_BYTES) {
        const prev = manifest[webPath];
        if (prev?.mediaId) usedIds.add(String(prev.mediaId));
        skip++;
        continue;
      }

      process.stderr.write(`  [${n}] ${path.basename(webPath)}\n`);
      process.stderr.write(`      § ${(context || '').slice(0, 55)}\n`);
      process.stderr.write(`      🔍 ${query.slice(0, 72)}\n`);

      try {
        const img = await searchImage(query, usedIds);
        if (!img) {
          process.stderr.write('      ❌ keine Treffer\n');
          fail++;
          await sleep(DELAY_MS);
          continue;
        }
        usedIds.add(img.id);
        const bytes = await downloadToFile(img.url, dest);
        manifest[webPath] = {
          mediaId: img.id,
          title: img.title,
          query,
          context,
          kind,
          bytes,
          at: new Date().toISOString(),
        };
        fs.writeFileSync(MANIFEST_PATH, JSON.stringify(manifest, null, 2));
        process.stderr.write(
          `      ✅ ${img.id} — ${(img.title || '').slice(0, 48)}\n`,
        );
        ok++;
      } catch (e) {
        process.stderr.write(`      ❌ ${e.message}\n`);
        fail++;
      }
      await sleep(DELAY_MS);
    }
  }

  process.stderr.write(`\nFertig: ${ok} neu, ${skip} übersprungen, ${fail} fehlgeschlagen\n`);
  console.log(JSON.stringify({ ok, skip, fail, total: jobs.length }, null, 2));
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
