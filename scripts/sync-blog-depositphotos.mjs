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
import { queryFromSectionTitle, ARTICLE_FALLBACK } from './blog-section-query-map.mjs';

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
  const sections = [];
  const sectionRe =
    /<h2 class="blog-content__section-title">([^<]+)<\/h2><figure class="section-visual"><img[^>]+src="(\/img\/blog-sections\/[^"]+\.jpg)"/gi;
  let m;
  while ((m = sectionRe.exec(html)) !== null) {
    const title = decodeHtml(m[1].trim());
    const webPath = m[2];
    const paragraph = extractParagraphAfter(html, webPath);
    const query = queryFromSectionTitle(title, paragraph, articleSlug);
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
      query: ARTICLE_FALLBACK[articleSlug] || queryFromSectionTitle(pageTitle, introText, articleSlug),
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
      : queryFromSectionTitle(pageTitle, introText, articleSlug);
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

function relevanceScore(item, query) {
  const tokens = query
    .toLowerCase()
    .split(/\s+/)
    .filter((t) => t.length > 3);
  const title = (item.title || '').toLowerCase();
  let score = 0;
  for (const t of tokens) {
    if (title.includes(t)) score += 4;
  }
  // Leichte Popularitäts-Gewichtung, aber Relevanz dominiert
  score += Math.min((item.downloads || 0) / 80000, 1.5);
  return score;
}

function pickBestResult(results, query) {
  if (!results.length) return null;
  return results.reduce((best, cur) => {
    const sb = relevanceScore(best, query);
    const sc = relevanceScore(cur, query);
    return sc > sb ? cur : best;
  });
}

async function trySearch(query, excludeIds = new Set(), limit = 20) {
  const data = await apiGet(
    new URLSearchParams({
      dp_apikey: apiKey,
      dp_session_id: sessionId,
      dp_command: 'search',
      dp_search_query: query.slice(0, 120),
      dp_search_limit: String(limit),
      dp_search_sort: 1,
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
  const attempts = [query, words.slice(0, 6).join(' '), words.slice(0, 4).join(' ')];
  const seen = new Set();
  let bestOverall = null;
  let bestScore = -1;

  for (const q of attempts) {
    const key = q.toLowerCase();
    if (seen.has(key) || !q.trim()) continue;
    seen.add(key);
    const results = await trySearch(q, excludeIds, 20);
    if (!results.length) {
      await sleep(100);
      continue;
    }
    const candidate = pickBestResult(results, query);
    const sc = relevanceScore(candidate, query);
    if (sc > bestScore) {
      bestScore = sc;
      bestOverall = candidate;
    }
    if (bestScore >= 8) break;
    await sleep(100);
  }
  return bestOverall;
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
