/**
 * Script zum Aktualisieren aller Affiliate-Links in dark-factory.html
 * Führt die Links aus affiliate-links-config.json ein
 */

const fs = require('fs');
const path = require('path');

// Lade Konfiguration
const configPath = path.join(__dirname, 'affiliate-links-config.json');
const htmlPath = path.join(__dirname, 'dark-factory.html');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
let html = fs.readFileSync(htmlPath, 'utf8');

// Mapping von Platzhaltern zu echten Links
const linkMapping = {
  // AppSumo Deals
  'YOUR_DEPOSITPHOTOS_APPSUMO_LINK': config.affiliate_links.appsumo.deals.depositphotos,
  'YOUR_NEURON_APPSUMO_LINK': config.affiliate_links.appsumo.deals.neuron_writer,
  'YOUR_SURFER_APPSUMO_LINK': config.affiliate_links.appsumo.deals.surfer_seo,
  'YOUR_OPUS_APPSUMO_LINK': config.affiliate_links.appsumo.deals.opus_clip,
  'YOUR_UNMIXR_APPSUMO_LINK': config.affiliate_links.appsumo.deals.unmixr,
  'YOUR_PICTORY_APPSUMO_LINK': config.affiliate_links.appsumo.deals.pictory,
  'YOUR_CANVA_APPSUMO_LINK': config.affiliate_links.appsumo.deals.canva_pro,
  'YOUR_MOOTION_APPSUMO_LINK': config.affiliate_links.appsumo.deals.mootion,
  'YOUR_CAPCUT_APPSUMO_LINK': config.affiliate_links.appsumo.deals.capcut,
  'YOUR_VPILER_APPSUMO_LINK': config.affiliate_links.appsumo.deals.vpiler,
  'YOUR_KATTEB_APPSUMO_LINK': config.affiliate_links.appsumo.deals.katteb,
  'YOUR_YAPPER_APPSUMO_LINK': config.affiliate_links.appsumo.deals.yapper,
  'YOUR_GRETA_APPSUMO_LINK': config.affiliate_links.appsumo.deals.greta,
  
  // Partner Links
  'YOUR_BINANCE_AFFILIATE_LINK': config.affiliate_links.crypto_exchanges.binance,
  'YOUR_BYBIT_AFFILIATE_LINK': config.affiliate_links.crypto_exchanges.bybit,
  'YOUR_COINBASE_AFFILIATE_LINK': config.affiliate_links.crypto_exchanges.coinbase,
  
  // AI Tools
  'YOUR_OPENAI_LINK': config.affiliate_links.ai_tools.openai,
  'YOUR_CLAUDE_LINK': config.affiliate_links.ai_tools.claude,
  'YOUR_PERPLEXITY_LINK': config.affiliate_links.ai_tools.perplexity,
  'YOUR_GEMINI_LINK': config.affiliate_links.ai_tools.gemini,
  
  // Infrastructure
  'YOUR_HOSTINGER_AFFILIATE_LINK': config.affiliate_links.infrastructure.hostinger,
  'YOUR_N8N_SETUP_LINK': config.affiliate_links.infrastructure.n8n,
  
  // Media Tools
  'YOUR_KIE_APPSUMO_LINK': config.affiliate_links.media_tools.kie_ai,
  'YOUR_ELEVENLABS_LINK': config.affiliate_links.media_tools.elevenlabs,
  'YOUR_RUNWAY_LINK': config.affiliate_links.media_tools.runway,
  
  // Fallback URLs (Standard-Links wenn AppSumo Deal abgelaufen)
  'YOUR_DEPOSITPHOTOS_STANDARD_LINK': 'https://depositphotos.com/?ref=cango',
  'YOUR_NEURON_STANDARD_LINK': 'https://neuronwriter.com/?ref=cango',
  'YOUR_SURFER_STANDARD_LINK': 'https://surferseo.com/?ref=cango',
  'YOUR_OPUS_STANDARD_LINK': 'https://opus.pro/?ref=cango',
  'YOUR_JASPER_STANDARD_LINK': 'https://jasper.ai/?ref=cango',
  'YOUR_UNMIXR_STANDARD_LINK': 'https://unmixr.com/?ref=cango',
  'YOUR_PICTORY_STANDARD_LINK': 'https://pictory.ai/?ref=cango',
  'YOUR_CANVA_STANDARD_LINK': 'https://canva.com/?ref=cango',
  'YOUR_MOOTION_STANDARD_LINK': 'https://mootion.com/?ref=cango',
  'YOUR_CAPCUT_STANDARD_LINK': 'https://capcut.com/?ref=cango',
  'YOUR_VPILER_STANDARD_LINK': 'https://vpiler.com/?ref=cango',
  'YOUR_KATTEB_STANDARD_LINK': 'https://katteb.com/?ref=cango',
  'YOUR_YAPPER_STANDARD_LINK': 'https://yapper.ai/?ref=cango',
  'YOUR_GRETA_STANDARD_LINK': 'https://greta.ai/?ref=cango',
  'YOUR_KIE_STANDARD_LINK': 'https://kie.ai/?ref=cango',
  'YOUR_CANVA_CAPTIONS_APPSUMO_LINK': config.affiliate_links.appsumo.deals.canva_pro,
  'YOUR_CANVA_CAPTIONS_STANDARD_LINK': 'https://canva.com/?ref=cango'
};

// Ersetze alle Platzhalter
Object.keys(linkMapping).forEach(placeholder => {
  const regex = new RegExp(placeholder, 'g');
  html = html.replace(regex, linkMapping[placeholder]);
});

// Speichere aktualisierte HTML-Datei
fs.writeFileSync(htmlPath, html, 'utf8');
console.log('✅ Affiliate-Links erfolgreich aktualisiert!');
console.log(`📊 ${Object.keys(linkMapping).length} Links ersetzt`);

