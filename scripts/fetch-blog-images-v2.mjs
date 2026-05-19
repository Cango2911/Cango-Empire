/**
 * Depositphotos Enterprise API — Blog-Bilder v2
 * Verbesserte, thematisch präzise Suchanfragen
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const API_BASE = 'https://api.depositphotos.com';

function loadEnv() {
  const envPath = path.join(REPO, '.env');
  const env = {};
  for (const line of fs.readFileSync(envPath, 'utf8').split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i > 0) env[t.slice(0, i).trim()] = t.slice(i + 1).trim();
  }
  return env;
}

const { DP_API_KEY, DP_USER, DP_PASS } = loadEnv();

// Präzisere Suchanfragen — nach Relevanz sortiert (best_match)
const ARTICLES = [
  { id: 'feat-finanzen',    query: 'private health insurance stethoscope doctor medical card',          type: 'featured' },
  { id: 'feat-crypto',      query: 'bitcoin gold coin cryptocurrency bull market profit',                type: 'featured' },
  { id: 'feat-energie',     query: 'solar panels house roof sunshine photovoltaic energy',              type: 'featured' },
  { id: 'card-etf',         query: 'ETF fund investment growth chart stock market wealth',              type: 'card' },
  { id: 'card-bu',          query: 'insurance protection umbrella security family safety',              type: 'card' },
  { id: 'card-defi',        query: 'blockchain digital decentralized finance crypto network',           type: 'card' },
  { id: 'card-kryptotax',   query: 'cryptocurrency bitcoin tax calculator finance law',                 type: 'card' },
  { id: 'card-strom',       query: 'electricity savings power bill light bulb energy cost',            type: 'card' },
  { id: 'card-waermepumpe', query: 'heat pump modern house heating installation eco energy',           type: 'card' },
  { id: 'card-cfd',         query: 'CFD trading stock chart finance broker risk',                      type: 'card' },
  { id: 'card-techanalyse', query: 'candlestick chart trading screen stock market analysis',           type: 'card' },
  { id: 'card-pflege',      query: 'senior care home real estate property investment',                 type: 'card' },
  { id: 'card-wohnung',     query: 'apartment keys real estate purchase modern city',                  type: 'card' },
  { id: 'card-claude-gpt',  query: 'artificial intelligence robot chatbot technology futuristic',      type: 'card' },
  { id: 'card-n8n-setup',   query: 'server rack data center cloud technology hosting',                 type: 'card' },
  { id: 'card-n8n-work',    query: 'business automation process workflow efficiency team',             type: 'card' },
  { id: 'card-zapier',      query: 'software integration automation tools digital workflow',           type: 'card' },
  { id: 'card-ki-bewerbung',query: 'job interview recruitment hiring artificial intelligence office',  type: 'card' },
  { id: 'card-gehalt',      query: 'salary negotiation handshake business meeting success',            type: 'card' },
  { id: 'card-enneagramm',  query: 'personality coaching mindset psychology business circle types',   type: 'card' },
  { id: 'card-adhs',        query: 'focus productivity work desk concentration organised workspace',   type: 'card' },
];

async function dpPost(params) {
  const body = new URLSearchParams(params);
  const res = await fetch(API_BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: body.toString(),
  });
  return res.json();
}

async function login() {
  const data = await dpPost({
    dp_command: 'loginEnterprise',
    dp_apikey: DP_API_KEY,
    dp_login_user: DP_USER,
    dp_login_password: DP_PASS,
  });
  if (data.type !== 'success') throw new Error('Login failed: ' + JSON.stringify(data.error));
  process.stderr.write(`✅ Login OK\n`);
  return data.sessionid;
}

async function searchImage(query, type) {
  const data = await dpPost({
    dp_command: 'search',
    dp_apikey: DP_API_KEY,
    dp_search_query: query,
    dp_search_limit: 10,
    dp_search_sort: 1,           // best_match statt bestseller
    dp_search_orientation: 'horizontal',
    dp_search_photo: 1,
    dp_search_vector: 0,
    dp_search_nudity: 0,
    dp_watermark: 'neutral',
    dp_search_imagesize: 'm',    // mindestens mittlere Auflösung
  });

  if (data.type !== 'success' || !data.result?.length) {
    // Fallback: kürzere Query
    const short = query.split(' ').slice(0, 3).join(' ');
    process.stderr.write(`  ↩ Fallback: "${short}"\n`);
    const data2 = await dpPost({
      dp_command: 'search',
      dp_apikey: DP_API_KEY,
      dp_search_query: short,
      dp_search_limit: 5,
      dp_search_sort: 4,
      dp_search_orientation: 'horizontal',
      dp_search_photo: 1,
      dp_search_vector: 0,
      dp_search_nudity: 0,
      dp_watermark: 'neutral',
    });
    if (data2.type !== 'success' || !data2.result?.length) return null;
    const item = data2.result[0];
    return { id: item.id, title: item.title, url: item.url2 || item.medium_thumbnail };
  }

  // Bestes Ergebnis auswählen (höchste Downloads unter Top-5)
  const top = data.result.slice(0, 5);
  const best = top.reduce((a, b) => ((b.downloads||0) > (a.downloads||0) ? b : a), top[0]);
  return { id: best.id, title: best.title, url: best.url2 || best.medium_thumbnail };
}

async function main() {
  await login();
  const results = {};
  for (const a of ARTICLES) {
    process.stderr.write(`🔍 ${a.id}: "${a.query.substring(0,55)}"\n`);
    const img = await searchImage(a.query, a.type);
    results[a.id] = img || null;
    if (img) process.stderr.write(`   ✅ ${img.id} — ${(img.title||'').substring(0,60)}\n`);
    else      process.stderr.write(`   ❌ kein Ergebnis\n`);
    await new Promise(r => setTimeout(r, 250));
  }
  console.log(JSON.stringify(results, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
