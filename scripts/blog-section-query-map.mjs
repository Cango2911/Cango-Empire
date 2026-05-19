/**
 * Präzise englische Depositphotos-Suchanfragen pro Abschnitts-Titel (H2).
 * Reihenfolge: spezifischste Regel zuerst. Nur Titel wird gematcht — kein Keyword-Mix.
 */
export const TITLE_QUERIES = [
  // ── Automation (vor generischen „monitoring“-Regeln) ──
  [/monitoring.*logging|betrieb im alltag/i, 'server monitoring dashboard logs DevOps analytics screen'],

  // ── Finanzen & Versicherung ──
  [/finanztool.*unverzichtbar|warum finanztool/i, 'personal finance dashboard laptop charts wealth'],
  [/etf[\s-]*sparpl/i, 'ETF savings plan investment app stock chart'],
  [/versicherung.*vergleich|intelligent vergleichen/i, 'insurance policy comparison documents calculator'],
  [/automatisierung.*finanz|ki.*finanzbereich/i, 'AI fintech automation banking software screen'],
  [/finanztool.*faq|finanztools im dach/i, 'financial planning FAQ advisor consultation'],

  // ── PKV / GKV Artikel ──
  [/^gkv:|solidarisch.*beitrag/i, 'German public health insurance hospital ward patients'],
  [/^pkv:|individueller tarif/i, 'private health insurance doctor stethoscope patient'],
  [/versicherungspflicht|statuswechsel/i, 'health insurance eligibility form Germany office'],
  [/leistungsumfang|zuzahlung/i, 'medical insurance benefits comparison hospital bill'],
  [/denkfehler vermeiden/i, 'person thinking wrong decision health insurance choice'],
  [/checkliste.*expert|gespräch.*expert/i, 'insurance consultation checklist clipboard doctor'],

  // ── Bitcoin / Crypto Artikel ──
  [/etf.*zugänglichkeit/i, 'Bitcoin ETF fund stock exchange trading screen'],
  [/retail vs.*institution|institutionen/i, 'institutional investor bitcoin fund wall street'],
  [/standort.*liquidität|liquidität.*immobil/i, 'real estate location map property market city'],
  [/liquidität.*verwahrung|verwahrung|gegenpartei/i, 'cryptocurrency cold wallet vault secure storage'],
  [/sicherheit im alltag/i, 'cryptocurrency wallet mobile security two factor authentication'],
  [/regulatorik/i, 'financial regulation compliance SEC documents cryptocurrency'],
  [/steuern.*dokumentation|krypto.*steuer/i, 'cryptocurrency tax form documents calculator'],
  [/psychologie.*volatilit/i, 'stressed investor volatile bitcoin chart red screen'],
  [/on-chain|narrativ/i, 'blockchain analytics dashboard on chain data'],
  [/portfolio[\s-]*denkweise/i, 'diversified crypto portfolio allocation pie chart'],
  [/sicherheit im alltag.*krypto|wallet/i, 'cryptocurrency wallet mobile security two factor'],

  // ── Solar Artikel ──
  [/kosten.*amortisation|amortisation/i, 'solar panel cost savings calculator house roof'],
  [/eigenverbrauch|speicher/i, 'home solar battery storage system rooftop panels'],
  [/dach.*ausrichtung|verschattung/i, 'house roof solar panel installation sunlight angle'],
  [/förderung.*beantragen|fördermittel/i, 'government subsidy solar energy application documents'],
  [/installateur.*wählen/i, 'solar installer technician roof photovoltaic panels'],
  [/strom.*einspeisung|einspeisevergütung/i, 'solar energy meter grid connection house'],
  [/förderung.*rahmen|förderung und rahmen/i, 'government solar energy subsidy grant application form'],
  [/wartung.*monitoring|monitoring.*versicherung/i, 'solar panel maintenance technician roof inspection'],
  [/netz.*eeg|marktintegration/i, 'solar power grid connection electricity meter house'],
  [/content[\s-]*automation.*energie/i, 'automated blog content solar energy laptop publishing'],
  [/szenarien.*einfamilienhaus|mietwohnung.*gewerbe/i, 'solar panels detached house apartment commercial roof'],
  [/ökobilanz|erwartungsmanagement/i, 'sustainable solar ecology green house carbon footprint'],
  [/typische fehler.*vorbereitung/i, 'solar installation planning mistake checklist homeowner'],

  // ── Claude / KI Artikel ──
  [/business[\s-]*use[\s-]*case|typische business/i, 'AI chatbot business team laptop office meeting'],
  [/kontextfenster|api[\s-]*design|kosten.*api/i, 'API cloud pricing dashboard software developer'],
  [/dsgvo|av[\s-]*vertrag/i, 'GDPR data privacy EU regulation legal documents laptop'],
  [/halluzination|qualitätssicherung/i, 'AI human review fact checking document verification'],
  [/integration.*n8n|internen tools/i, 'workflow automation software integration diagram nodes'],
  [/governance.*rollen|logs.*retention/i, 'corporate IT governance policy meeting compliance'],
  [/anbieterwechsel|vendor[\s-]*lock/i, 'software vendor migration cloud platforms comparison'],
  [/api[\s-]*keys|least privilege/i, 'cybersecurity API key password lock server'],
  [/datenklassen|trennung/i, 'data classification secure folders enterprise laptop'],
  [/prompt[\s-]*autor|reviewer.*operator/i, 'team collaboration AI prompt engineering whiteboard'],
  [/internationale teams|sprachen/i, 'diverse international remote team video conference'],
  [/roadmap.*pilot|messen.*skalieren/i, 'business growth roadmap timeline strategy meeting'],
  [/ethik.*transparenz|markenstimme/i, 'AI ethics transparency trust brand communication'],

  // ── Immobilien Artikel ──
  [/zins.*preisumfeld|zinspolitik/i, 'mortgage interest rates real estate chart bank'],
  [/standort.*liquidität/i, 'city map real estate location property investment'],
  [/wohnungseigentum|teileigentum/i, 'condominium apartment building homeowners association'],
  [/kaufnebenkosten|grunderwerb/i, 'real estate purchase costs notary contract signing'],
  [/technischer zustand|gutachten/i, 'home inspection engineer property assessment clipboard'],
  [/finanzierung strukturieren/i, 'mortgage loan approval bank real estate financing'],
  [/mietrendite|rendite/i, 'rental income real estate investment apartment keys'],
  [/lead[\s-]*infrastruktur|immobilien[\s-]*content/i, 'real estate CRM lead generation property website'],
  [/kaufpreis vs.*miete/i, 'rent versus buy house comparison calculator decision'],
  [/kaufvertrag|verhandlung/i, 'real estate contract signing keys handshake apartment'],
  [/versicherung.*kauf|nach dem kauf/i, 'home insurance policy new homeowner documents'],
  [/psychologie.*kaufen/i, 'couple deciding buy house thoughtful decision'],

  // ── ADHS / Produktivität ──
  [/externe struktur|motivation/i, 'organized planner desk calendar productivity structure'],
  [/automation als stütze/i, 'productivity automation app smartphone reminders tasks'],
  [/kommunikation.*grenzen/i, 'work life balance boundaries office conversation calm'],
  [/energie.*schlaf|bewegung/i, 'healthy sleep exercise wellness morning routine energy'],
  [/teams einbinden|mikromanagement/i, 'team collaboration meeting without micromanagement trust'],
  [/fehlerkultur|iteration/i, 'team learning from mistakes agile retrospective whiteboard'],
  [/inbox[\s-]*zero|informationsdiät/i, 'clean email inbox organized laptop minimal distraction'],
  [/vertriebsrhythmen|produkt.*rhythmen/i, 'sales pipeline CRM dashboard business rhythm'],
  [/finanzen.*admin.*stress/i, 'paperwork stress bills organized desk accounting calm'],
  [/weiterbildung.*overload|lernen ohne/i, 'online learning laptop books balanced study'],
  [/gemeinschaft.*accountability|accountability.*ohne druck/i, 'accountability partner coaching group support meeting'],
  [/cango.*infrastruktur|motivationscoaching/i, 'business systems infrastructure workflow automation laptop'],
  [/notfallmodus|überlastung/i, 'burnout recovery rest overwhelmed professional calm'],

  // ── Energie / Solar Kategorie ──
  [/energie[\s-]*lead|qualität über quantität/i, 'solar sales lead CRM qualification form rooftop'],
  [/b2b energie|gewerbe.*industrie/i, 'commercial solar panels factory industrial rooftop energy'],
  [/content[\s-]*marketing.*energie|lokale seo/i, 'local SEO map google search solar business laptop'],
  [/energie[\s-]*automation.*faq|solar[\s-]*lead/i, 'solar energy FAQ customer support installer'],

  // ── Crypto Kategorie ──
  [/crypto[\s-]*automation|jenseits von hodl/i, 'cryptocurrency trading automation bot dashboard'],
  [/web3.*creator|community builder/i, 'web3 community NFT creator digital content social'],
  [/crypto[\s-]*steuer.*deutschland|steuer.*tools/i, 'Germany cryptocurrency tax declaration documents'],
  [/web3.*faq|crypto.*business/i, 'blockchain business FAQ support technology office'],

  // ── Trading ──
  [/automation.*trading|trading den unterschied/i, 'automated trading algorithm stock chart screen'],
  [/signal[\s-]*pipeline|analyse zur ausführung/i, 'trading signals algorithm chart execution monitor'],
  [/risikomanagement systematis/i, 'risk management trading stop loss chart protection'],
  [/trading[\s-]*reporting|steuern.*performance/i, 'trading tax report performance analytics spreadsheet'],
  [/trading[\s-]*automation.*faq/i, 'stock trading FAQ financial chart help'],

  // ── Karriere / HR ──
  [/talent[\s-]*pipeline|klare stufen/i, 'talent pipeline recruitment funnel HR dashboard'],
  [/hr[\s-]*tech|ats.*kalender|vorqualifizierung/i, 'ATS applicant tracking system HR software interview'],
  [/chatbots.*scoring|automation.*fairness/i, 'AI recruitment chatbot fair hiring HR technology'],
  [/employer branding|content[\s-]*pipeline/i, 'employer branding recruitment marketing social media team'],
  [/onboarding.*mitarbeit/i, 'employee onboarding welcome new hire office laptop'],
  [/recruiting.*faq|hr[\s-]*automation.*faq/i, 'HR recruitment FAQ job interview support'],

  // ── Immobilien Kategorie ──
  [/immobilien.*automation|wettbewerbsvorteil/i, 'real estate agent tablet property technology automation'],
  [/crm.*immobilien|immobilienprofis/i, 'real estate CRM software agent showing house tablet'],
  [/lead[\s-]*generierung.*immobilien|organisch.*immobil/i, 'real estate lead generation website marketing agent'],
  [/datenanalyse.*investoren|marktbewertung/i, 'real estate market analytics chart investor dashboard'],
  [/immobilien.*markt|kapitalanlage/i, 'real estate market investment property skyline'],
  [/finanzierung.*immobil|hypothek/i, 'mortgage real estate financing bank meeting couple'],
  [/vermietung|verwaltung/i, 'rental property management landlord keys apartment'],
  [/exposé|besichtigung/i, 'real estate property tour showing apartment bright room'],
  [/immobilien[\s-]*tool/i, 'real estate technology tools agent professional house'],

  // ── KI / Tech Kategorie ──
  [/ki im business|strategie vor tool/i, 'AI business strategy executives boardroom meeting innovation'],
  [/tool[\s-]*ökossystem|orientierung.*anbieter/i, 'AI tools logos comparison laptop screen ecosystem'],
  [/custom gpt|ki[\s-]*agenten|nächste stufe/i, 'ChatGPT custom AI agent assistant business laptop automation'],
  [/governance.*datenschutz|ki sicher eins/i, 'AI data privacy GDPR governance enterprise security laptop'],
  [/ki[\s-]*tool.*unternehmen|enterprise ai/i, 'enterprise AI software business team laptop innovation'],
  [/machine learning|ml[\s-]*pipeline/i, 'machine learning data pipeline server room technology'],
  [/prompt engineering|llm/i, 'prompt engineering AI text generation laptop developer'],
  [/ki.*integration|ki.*faq|tech.*faq/i, 'artificial intelligence FAQ technology support help desk'],

  // ── Automationen ──
  [/workflows dokumentiert|versionie/i, 'workflow documentation diagram business process chart'],
  [/n8n vs|zapier vs|make.*werkzeug/i, 'n8n Zapier Make automation software logos comparison'],
  [/apis.*webhooks|fehlerbehandlung/i, 'API webhook developer integration error handling code'],
  [/manuell zu skalierbar|typisches beispiel/i, 'business growth scaling automation team success chart'],
  [/workflow.*automatis|n8n.*mittelstand/i, 'n8n workflow automation business process diagram'],
  [/zapier.*n8n|tool.*vergleich/i, 'automation software comparison Zapier workflow integration'],
  [/prozess.*digitalis/i, 'business process digital transformation automation office'],
  [/automation.*orchestrierung/i, 'workflow orchestration automation software enterprise'],

  // ── Coaching ──
  [/digitale produkte.*standard|klare standard/i, 'digital coaching product online course laptop creator'],
  [/funnel ohne druck|klarheit statt/i, 'sales funnel marketing coaching whiteboard strategy calm'],
  [/content[\s-]*kalender|sichtbarkeit ohne/i, 'social media content calendar planner creator desk'],
  [/preise.*ratenzahlung|transparente kond/i, 'coaching business pricing payment plan contract handshake'],
  [/coaching[\s-]*business.*skalier|digitale skalier/i, 'online coaching business scaling laptop entrepreneur'],
  [/enneagramm|persönlichkeitstyp/i, 'personality test coaching psychology enneagram diagram'],
  [/mindset.*business|coaching.*unternehm/i, 'business coach mentor session whiteboard mindset'],
  [/achtsamkeit|meditation/i, 'mindfulness meditation calm business professional office'],

  // ── Davinci / Maschinen ──
  [/maschinen.*dienen|davinci|renaissance/i, 'human robot collaboration innovation Leonardo technology art'],
  [/mensch.*maschine|symbiose/i, 'human and robot handshake collaboration future technology'],

  // ── Generisch FAQ (zuletzt) ──
  [/^faq\b|häufige fragen/i, 'FAQ frequently asked questions help support desk'],
];

/** Nur wenn Titel vage ist: 1–2 Begriffe aus dem Absatz (gleiche Domäne) */
export const PARA_SNIPPETS = [
  [/photovoltaik|pv[\s-]*anlage|solaranlage/i, 'rooftop solar panels'],
  [/wärmepumpe/i, 'heat pump house'],
  [/n8n|zapier|make\.com/i, 'workflow automation'],
  [/crm|hubspot|salesforce/i, 'CRM dashboard'],
  [/dachgröße|eigenverbrauch/i, 'solar house roof'],
  [/etf|msci|broker/i, 'ETF broker app'],
  [/bu[\s-]|berufsunfähigkeit/i, 'disability insurance'],
  [/pkv|gkv|krankenkasse/i, 'health insurance card'],
  [/bitcoin|ethereum|wallet/i, 'bitcoin wallet'],
  [/candlestick|chart|börse/i, 'stock candlestick chart'],
  [/dsgvo|datenschutz/i, 'GDPR privacy'],
  [/bewerbung|lebenslauf|cv/i, 'job application resume'],
  [/pflegeimmobil/i, 'nursing home real estate'],
  [/pflichtgrenze|66400|69600/i, 'salary threshold documents'],
];

export const ARTICLE_FALLBACK = {
  'finanzen-versicherung': 'personal finance insurance Germany professional',
  'crypto-web3': 'cryptocurrency blockchain technology business',
  'energie-solar': 'solar energy renewable business professional',
  'trading': 'stock market trading chart professional screen',
  'immobilien': 'real estate property investment professional',
  'ki-tech': 'artificial intelligence technology business laptop',
  automationen: 'business workflow automation software diagram',
  'karriere-hr': 'human resources recruitment office professional',
  'coaching-mindset': 'business coaching mindset professional office',
  'artikel-pkv-vs-gkv-2026': 'health insurance Germany doctor hospital',
  'artikel-bitcoin-institutionen-2026': 'bitcoin cryptocurrency institutional investment',
  'artikel-solaranlage-ratgeber-2026': 'solar panels house roof installation',
  'artikel-claude-vs-chatgpt-unternehmen-2026': 'AI chatbot enterprise business laptop',
  'artikel-eigentumswohnung-kaufen-2026': 'apartment buying real estate keys',
  'artikel-produktivitaet-adhs-systeme': 'productive organized desk focus minimal',
  'maschinen-die-dienen-davinci-pfad': 'human robot technology innovation future',
};

export function queryFromSectionTitle(title, paragraph = '', articleSlug = '') {
  const t = title.trim();

  for (const [re, query] of TITLE_QUERIES) {
    if (re.test(t)) return query;
  }

  // Absatz nur ergänzen wenn Titel kein klares Mapping hatte
  const extras = [];
  const p = paragraph.toLowerCase();
  for (const [re, snippet] of PARA_SNIPPETS) {
    if (re.test(p) && !extras.includes(snippet)) extras.push(snippet);
    if (extras.length >= 2) break;
  }

  const fallback = ARTICLE_FALLBACK[articleSlug] || 'business professional modern';
  if (extras.length) return `${fallback.split(' ').slice(0, 3).join(' ')} ${extras.join(' ')}`.trim();
  return fallback;
}
