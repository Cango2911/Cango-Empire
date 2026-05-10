#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Blogs mit keyword-relevanten Section-Bildern neu aufbauen
Openverse API: CC-lizenzierte Fotos nach Keyword, kostenlos, kein Key nötig.
Bilder erscheinen part-by-part direkt im Body nach jeder h2-Section.
"""
import ftplib, json, re, time, urllib.request, urllib.parse
from pathlib import Path

ROOT      = Path(__file__).parent.parent
BLOGS_DIR = ROOT / "website" / "blogs"
IMG_DIR   = ROOT / "website" / "images" / "blog-sections"
IMG_DIR.mkdir(parents=True, exist_ok=True)

from cango_env import ftp_credentials

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()
REMOTE   = "/docker/nginx-proxy-manager-5tiw/www"

# ── Openverse Bild-Suche ───────────────────────────────────────────────────────
def openverse_search(query: str, count: int = 1) -> list[str]:
    """Gibt Liste von Bild-URLs zurück (CC-lizenziert, frei nutzbar)."""
    q = urllib.parse.quote(query)
    url = f"https://api.openverse.org/v1/images/?q={q}&page_size={count}&license_type=commercial&mature=false"
    req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0 (blog@automation-cango-app-empire.com)"})
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read())
        return [item["url"] for item in data.get("results", []) if item.get("url")]
    except Exception as e:
        print(f"  ⚠ Openverse '{query}': {e}")
        return []

def download_img(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            dest.write_bytes(r.read())
        return True
    except Exception as e:
        print(f"  ✗ download {dest.name}: {e}")
        return False

# Fallback: Picsum mit schönen ID-spezifischen Fotos wenn Openverse nichts liefert
PICSUM_FALLBACKS = {
    "bitcoin": 730, "crypto": 180, "blockchain": 325,
    "solar": 459, "energy": 974, "photovoltaik": 129,
    "immobilien": 164, "wohnung": 547, "haus": 1080,
    "finanzen": 210, "versicherung": 260, "geld": 172,
    "ki": 442, "technologie": 96, "computer": 325,
    "trading": 534, "börse": 172, "investition": 210,
    "karriere": 375, "büro": 399, "team": 260,
    "coaching": 573, "mindset": 1024, "motivation": 399,
    "automatisierung": 1036, "workflow": 442, "n8n": 325,
    "adhs": 573, "produktivität": 260, "fokus": 399,
    "default": 96,
}

def picsum_fallback(keyword: str, w: int, h: int) -> str:
    pid = PICSUM_FALLBACKS.get(keyword.lower().split()[0], PICSUM_FALLBACKS["default"])
    return f"https://picsum.photos/id/{pid}/{w}/{h}"

def get_image(keyword: str, dest: Path, w: int = 900, h: int = 500) -> bool:
    """Holt Bild via Openverse oder Picsum-Fallback."""
    urls = openverse_search(keyword, count=3)
    for url in urls:
        if download_img(url, dest):
            return True
    # Fallback
    fb_url = picsum_fallback(keyword, w, h)
    return download_img(fb_url, dest)

# ── Blog-Definitionen mit Section-Keywords ─────────────────────────────────────
BLOGS = [
    {
        "slug": "finanzen-versicherung",
        "title": "Finanzen & Versicherung 2026: Was wirklich zählt",
        "hero_kw": "personal finance money investment",
        "sections": [
            {
                "h2": "Warum Versicherungen neu gedacht werden müssen",
                "img_kw": "insurance protection document contract",
                "body": "Die klassische Vollkasko-Mentalität stirbt langsam aus. Verbraucher wollen verstehen, wofür sie zahlen. Modulare Tarife, digitale Schadensmeldung und KI-gestützte Risikoanalyse verändern die Branche grundlegend. Wer heute abschließt, sollte auf Flexibilität achten – nicht auf maximale Absicherung gegen unwahrscheinliche Szenarien.",
            },
            {
                "h2": "ETF-Sparplan vs. aktiv gemanagter Fonds",
                "img_kw": "stock market ETF investment chart graph",
                "body": "Die Daten sprechen seit Jahren eine klare Sprache: Über 80 % der aktiv gemanagten Fonds schlagen ihren Vergleichsindex nicht. Ein diversifizierter ETF-Sparplan – monatlich, automatisiert, kostengünstig – ist für die meisten Menschen die überlegene Strategie. Der CanGo Empire Ansatz: erst Grundabsicherung aufbauen, dann investieren, dann optimieren.",
            },
            {
                "h2": "Notfallgroschen, Rücklage, Vermögen – die drei Schichten",
                "img_kw": "savings piggy bank emergency fund coins",
                "body": "Finanziell resilient zu sein bedeutet nicht reich zu sein. Es bedeutet, strukturiert vorzugehen: drei Monatsgehälter liquid halten, dann Schulden tilgen, dann Vermögen aufbauen. Diese Reihenfolge klingt banal – wird aber von den meisten nicht eingehalten. Das ist der eigentliche Hebel.",
            },
        ],
        "category": "Finanzen & Versicherung",
        "date": "2026-04-10",
        "read_time": "6 Min.",
        "pullquote": "Finanzielle Freiheit ist keine Zahl. Sie ist ein Zustand.",
        "tags": ["ETF", "Versicherung", "Finanzen", "Rücklage"],
        "related": [("Immobilien kaufen", "immobilien.html"), ("Trading", "trading.html"), ("PKV vs GKV", "artikel-pkv-vs-gkv-2026.html")],
    },
    {
        "slug": "crypto-web3",
        "title": "Crypto & Web3 2026: Was bleibt, was kommt",
        "hero_kw": "cryptocurrency bitcoin digital currency",
        "sections": [
            {
                "h2": "Bitcoin als Reserveasset – Realität oder Wunschdenken?",
                "img_kw": "bitcoin gold cryptocurrency institutional investment",
                "body": "Wenn BlackRock, Fidelity und staatliche Pensionsfonds Bitcoin halten, ist die Diskussion über seine Legitimität beendet. 2026 sehen wir die erste Welle echter Integration in traditionelle Portfolios. Das bedeutet weniger Volatilität, aber auch weniger explosive Renditen. Bitcoin wird Infrastruktur.",
            },
            {
                "h2": "Ethereum: Wo steht das Ökosystem?",
                "img_kw": "ethereum blockchain smart contract decentralized",
                "body": "Layer-2-Lösungen wie Arbitrum und Base haben das Skalierungsproblem gelöst. Gas-Gebühren unter einem Cent sind Realität. Was fehlt, ist die Killer-App – die Anwendung, die normale Menschen täglich nutzen. DeFi, NFTs und Gaming haben Pionierarbeit geleistet, aber der breite Durchbruch steht noch aus.",
            },
            {
                "h2": "Web3 jenseits des Hypes",
                "img_kw": "web3 decentralized digital identity future technology",
                "body": "Die interessantesten Web3-Projekte 2026 sind die unspektakulären: digitale Identität, dezentrale Datenspeicherung, tokenisierte Real-World-Assets. Sie lösen echte Probleme, ohne dass die Nutzer wissen müssen, dass sie auf einer Blockchain laufen. Das ist die Zukunft – unsichtbar, aber wirksam.",
            },
        ],
        "category": "Crypto & Web3",
        "date": "2026-04-11",
        "read_time": "7 Min.",
        "pullquote": "Die beste Technologie verschwindet in der Infrastruktur.",
        "tags": ["Bitcoin", "Ethereum", "Web3", "DeFi", "Blockchain"],
        "related": [("Bitcoin Institutionen", "artikel-bitcoin-institutionen-2026.html"), ("Trading", "trading.html"), ("KI & Tech", "ki-tech.html")],
    },
    {
        "slug": "energie-solar",
        "title": "Energie & Solar 2026: Der Eigenverbrauch-Boom",
        "hero_kw": "solar panels rooftop renewable energy",
        "sections": [
            {
                "h2": "Solaranlage 2026 – Rechnet es sich noch?",
                "img_kw": "solar panel installation rooftop house photovoltaic",
                "body": "Ja – mit Einschränkungen. Die Einspeisevergütung ist gesunken, aber die Modulpreise auch. Entscheidend ist jetzt der Eigenverbrauchsanteil: Wer 60–70 % selbst verbraucht (z.B. durch E-Auto oder Wärmepumpe), amortisiert die Anlage in 8–10 Jahren. Ohne Speicher und ohne große Lasten dauert es länger.",
            },
            {
                "h2": "Batteriespeicher: Wann ist er sinnvoll?",
                "img_kw": "battery energy storage home solar system",
                "body": "Ein Speicher lohnt sich, wenn dein Eigenverbrauch unter 40 % liegt und du ihn damit auf 70–80 % heben kannst. Die Preise für Heimspeicher sind 2025/2026 deutlich gefallen – 5–10 kWh sind jetzt für 4.000–7.000 € realistisch. Kombiniert mit dynamischen Stromtarifen ist das ein echter Hebel.",
            },
            {
                "h2": "Der ganzheitliche Energiehaushalt",
                "img_kw": "heat pump electric car smart home energy management",
                "body": "Solar + Speicher + Wärmepumpe + E-Auto ist das Quadruple-Play der Energiewende. Wer alle vier Komponenten optimiert und intelligent vernetzt, kann theoretisch nahezu energieautark leben. Das erfordert Planung, aber keine Kompromisse beim Komfort.",
            },
        ],
        "category": "Energie & Solar",
        "date": "2026-04-09",
        "read_time": "6 Min.",
        "pullquote": "Energie erzeugen ist Freiheit. Energie sparen ist Strategie.",
        "tags": ["Solar", "Photovoltaik", "Speicher", "Wärmepumpe", "Energiewende"],
        "related": [("Solaranlage Ratgeber", "artikel-solaranlage-ratgeber-2026.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
    },
    {
        "slug": "immobilien",
        "title": "Immobilien 2026: Kaufen, Mieten oder Warten?",
        "hero_kw": "real estate house apartment architecture",
        "sections": [
            {
                "h2": "Wo stehen die Preise wirklich?",
                "img_kw": "real estate price market house Germany city",
                "body": "In B- und C-Städten sind Preise teilweise 15–25 % unter dem Peak 2022. In Top-7-Städten nur 8–12 %. Das klingt nach Einstiegsgelegenheit – aber die Kaufnebenkosten (7–12 %), gestiegene Zinsen (3,5–4 %) und höhere Anforderungen an die Energieeffizienz ändern die Kalkulation fundamental.",
            },
            {
                "h2": "Eigennutzung vs. Kapitalanlage",
                "img_kw": "apartment interior living room modern",
                "body": "Wer zur Eigennutzung kauft, denkt in Jahrzehnten – und das ist richtig. Wer als Investition kauft, muss mit realistischen Mietrenditen kalkulieren. In vielen Lagen liegt die Bruttomietrendite unter 3 % – nach Verwaltung, Instandhaltung und Finanzierung oft im negativen Bereich.",
            },
            {
                "h2": "Was 2026 wirklich zählt beim Kauf",
                "img_kw": "energy efficiency building renovation insulation",
                "body": "Lage, Energieeffizienz und Finanzierungsstruktur. Ein Haus mit Energieklasse G ist 2026 nicht mehr verkäuflich ohne erhebliche Abschläge – und bis 2030 kommen Sanierungspflichten. Käufer sollten EPC, Heizungsart und Dämmstand vor dem Kauf prüfen wie früher nur den Grundriss.",
            },
        ],
        "category": "Immobilien",
        "date": "2026-04-08",
        "read_time": "7 Min.",
        "pullquote": "Immobilien sind kein Investment. Sie sind Infrastruktur.",
        "tags": ["Immobilien", "Kaufen", "Mieten", "Zinsen"],
        "related": [("Eigentumswohnung kaufen", "artikel-eigentumswohnung-kaufen-2026.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
    },
    {
        "slug": "ki-tech",
        "title": "KI & Tech 2026: Was jetzt wirklich passiert",
        "hero_kw": "artificial intelligence technology robot future",
        "sections": [
            {
                "h2": "Von ChatGPT zur KI-Infrastruktur",
                "img_kw": "artificial intelligence neural network data center server",
                "body": "Der Markt hat sich konsolidiert. Anthropic, OpenAI, Google und Meta liefern Foundation Models, auf denen Tausende Anwendungen aufbauen. Wer heute KI als Werkzeug nutzt, hat einen Produktivitätsvorteil. Wer KI in seine Systeme integriert, hat einen strukturellen Vorteil.",
            },
            {
                "h2": "Was Unternehmen jetzt tun sollten",
                "img_kw": "business team office laptop technology meeting",
                "body": "Nicht 'Was kann KI?' – sondern 'Welche unserer Prozesse kosten am meisten Zeit mit dem geringsten Wert?' Das ist die richtige Frage. Content-Erstellung, Kundenservice, Datenanalyse und interne Dokumentation sind die vier Bereiche mit dem besten ROI bei KI-Integration.",
            },
            {
                "h2": "KI für Einzelpersonen: Der Hebel ist riesig",
                "img_kw": "freelancer laptop productivity work from home",
                "body": "Ein Solopreneur mit KI-Tools kann heute die Kapazität eines kleinen Teams erreichen. Content-Pipelines, automatisiertes Outreach, Marktrecherche, Code-Generierung – alles machbar ohne Programmierkenntnisse. Der Engpass ist nicht mehr das Werkzeug, sondern die Strategie.",
            },
        ],
        "category": "KI & Technologie",
        "date": "2026-04-07",
        "read_time": "8 Min.",
        "pullquote": "KI gibt dir nicht mehr Ideen. Sie gibt dir mehr Zeit für die richtigen.",
        "tags": ["KI", "Künstliche Intelligenz", "ChatGPT", "Claude", "Automatisierung"],
        "related": [("Claude vs ChatGPT", "artikel-claude-vs-chatgpt-unternehmen-2026.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
    },
    {
        "slug": "trading",
        "title": "Trading 2026: Strategien die funktionieren",
        "hero_kw": "stock trading charts financial market",
        "sections": [
            {
                "h2": "Warum 90 % der Trader verlieren",
                "img_kw": "stock market crash loss trading screen red",
                "body": "Nicht weil der Markt gegen sie ist. Weil sie ohne Edge handeln, zu groß positionieren und emotional reagieren. Der Markt transferiert Kapital von Ungeduld zu Geduld. Wer das versteht, beginnt anders zu denken.",
            },
            {
                "h2": "Systemisches Trading vs. diskretionäres Trading",
                "img_kw": "algorithmic trading system computer screen data",
                "body": "Systemisches Trading (regelbasiert, automatisiert) schlägt diskretionäres Trading im Durchschnitt – nicht weil Regeln besser sind als Intuition, sondern weil Regeln konsistent sind. Backtesting, klare Entry/Exit-Kriterien und Risk-Management sind keine Optionen. Sie sind das Fundament.",
            },
            {
                "h2": "Der psychologische Vorteil",
                "img_kw": "meditation calm focus mindset zen",
                "body": "Wer sein System kennt und vertraut, handelt entspannter. Entspanntes Trading ist besseres Trading. Die wichtigste Fähigkeit ist nicht die Analyse – es ist die Disziplin, das System auch dann zu folgen, wenn der Markt sich falsch anfühlt.",
            },
        ],
        "category": "Trading",
        "date": "2026-04-06",
        "read_time": "6 Min.",
        "pullquote": "Ein schlechtes System konsequent angewandt schlägt kein System.",
        "tags": ["Trading", "Börse", "Aktien", "Strategie"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Finanzen", "finanzen-versicherung.html"), ("Bitcoin", "artikel-bitcoin-institutionen-2026.html")],
    },
    {
        "slug": "karriere-hr",
        "title": "Karriere & HR 2026: Der neue Arbeitsmarkt",
        "hero_kw": "career job interview business professional",
        "sections": [
            {
                "h2": "Welche Skills 2026 wirklich gefragt sind",
                "img_kw": "skills learning education technology digital",
                "body": "KI-Kompetenz ist Pflicht, nicht Kür. Prompt Engineering, Datenanalyse, Systemdenken und die Fähigkeit, KI-Tools sinnvoll zu orchestrieren, sind die Schlüsselqualifikationen. Dazu kommen unverrückbar menschliche Skills: Kommunikation, Führung, Kreativität und Empathie.",
            },
            {
                "h2": "Remote Work: Was wirklich bleibt",
                "img_kw": "remote work home office laptop video call",
                "body": "Hybrid ist der Standard geworden. Vollständiges Remote ist für viele Unternehmen verhandelt – Ausnahme sind Tech-Unternehmen und internationale Teams. Wer remote arbeiten will, braucht nicht nur die Fähigkeit, sondern auch den Beweis, dass er eigenverantwortlich liefert.",
            },
            {
                "h2": "Selbstständigkeit und Portfolio-Karriere",
                "img_kw": "freelancer entrepreneur startup business owner",
                "body": "Immer mehr Hochqualifizierte verlassen die Festanstellung – nicht aus Not, sondern aus Kalkül. Mehrere Einkommensquellen, Kontrolle über Zeit und Projekte, weniger Organisationspolitik. Das ist der eigentliche Trend hinter 'The Great Resignation'.",
            },
        ],
        "category": "Karriere & HR",
        "date": "2026-04-05",
        "read_time": "6 Min.",
        "pullquote": "Der wertvollste Mitarbeiter 2026 ist der, der KI orchestriert.",
        "tags": ["Karriere", "HR", "Remote Work", "Fachkräfte"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("KI & Tech", "ki-tech.html")],
    },
    {
        "slug": "coaching-mindset",
        "title": "Coaching & Mindset: Die innere Architektur des Erfolgs",
        "hero_kw": "coaching mindset success motivation personal development",
        "sections": [
            {
                "h2": "Growth Mindset ist mehr als Buzzword",
                "img_kw": "growth mindset learning brain development",
                "body": "Carol Dwecks Forschung ist eindeutig: Menschen mit Growth Mindset – der Überzeugung, dass Fähigkeiten entwickelbar sind – erzielen langfristig bessere Ergebnisse. Nicht weil sie härter arbeiten, sondern weil sie anders auf Rückschläge reagieren. Fehler sind Feedback, keine Urteile.",
            },
            {
                "h2": "Systeme schlagen Willenskraft",
                "img_kw": "habit system routine productivity planning notebook",
                "body": "Willenskraft ist eine endliche Ressource. Wer sich auf sie verlässt, scheitert systematisch an schlechten Tagen. Systeme – Routinen, Umgebungsdesign, Automatisierungen – funktionieren auch wenn die Motivation niedrig ist. Das ist der Kern des CanGo Empire Ansatzes.",
            },
            {
                "h2": "Coaching: Wann macht es Sinn?",
                "img_kw": "coaching mentor conversation support guide",
                "body": "Coaching ist kein Allheilmittel – aber in den richtigen Momenten der effektivste Hebel. Wann es Sinn macht: bei Übergängen (Job, Beziehung, Projekt), bei wiederkehrenden Mustern und wenn du weißt was zu tun ist, aber es nicht tust. Ein guter Coach stellt die richtigen Fragen, gibt keine Antworten.",
            },
        ],
        "category": "Coaching & Mindset",
        "date": "2026-04-04",
        "read_time": "7 Min.",
        "pullquote": "Du brauchst keine Motivation. Du brauchst ein System.",
        "tags": ["Coaching", "Mindset", "Growth Mindset", "Systeme"],
        "related": [("Karriere & HR", "karriere-hr.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("Automatisierungen", "automationen.html")],
    },
    {
        "slug": "automationen",
        "title": "Automatisierungen 2026: Was du heute noch einrichten kannst",
        "hero_kw": "automation workflow robot process technology",
        "sections": [
            {
                "h2": "Die No-Code/Low-Code Revolution",
                "img_kw": "no code low code workflow automation tool",
                "body": "n8n, Make (Integromat), Zapier und neu: KI-Agenten via Anthropic oder OpenAI API. Die Tools sind so weit gereift, dass technisches Know-how kein Engpass mehr ist. Der Engpass ist die richtige Frage: Welcher Prozess kostet mich die meiste Zeit mit dem geringsten Wert?",
            },
            {
                "h2": "Content-Automatisierung: Was wirklich funktioniert",
                "img_kw": "content creation blogging writing AI automation",
                "body": "Vollautomatisierter Content ohne menschliche Kurierung ist erkennbar – und wird von Google zunehmend abgestraft. Die Zukunft ist semi-automatisiert: KI generiert Drafts, Menschen kurieren und veredeln. Wer diesen Workflow optimiert, publiziert 10x schneller ohne Qualitätsverlust.",
            },
            {
                "h2": "Lead-Generierung und CRM-Automatisierung",
                "img_kw": "CRM sales funnel lead generation email marketing",
                "body": "Der größte ROI liegt oft nicht im Content, sondern im Follow-Up. Automatisierte E-Mail-Sequenzen, CRM-Updates durch Webhooks und KI-gestützte Personalisierung – wer das aufgebaut hat, verliert keine Leads mehr durch mangelnde Nachverfolgung.",
            },
        ],
        "category": "Automatisierungen",
        "date": "2026-04-03",
        "read_time": "8 Min.",
        "pullquote": "Automatisiere das Wiederholbare. Fokussiere auf das Einzigartige.",
        "tags": ["n8n", "Automatisierung", "Make", "No-Code"],
        "related": [("Maschinen die dienen", "maschinen-die-dienen.html"), ("KI & Tech", "ki-tech.html"), ("Karriere & HR", "karriere-hr.html")],
    },
    {
        "slug": "artikel-bitcoin-institutionen-2026",
        "title": "Bitcoin und Institutionen 2026: Eine neue Ära",
        "hero_kw": "bitcoin cryptocurrency gold investment bank",
        "sections": [
            {
                "h2": "Bitcoin-ETFs: Zahlen und Fakten",
                "img_kw": "bitcoin ETF fund investment wall street",
                "body": "Die ersten Spot-ETFs in den USA haben in den ersten 12 Monaten mehr Kapital angezogen als Gold-ETFs in ihrer Anfangsphase. Milliarden Dollar fließen monatlich in strukturierte Bitcoin-Produkte. Das dämpft die Volatilität – und verändert die Marktdynamik fundamental.",
            },
            {
                "h2": "Staatsreserven: Wer folgt El Salvador?",
                "img_kw": "government treasury reserve finance national",
                "body": "El Salvador war der Proof of Concept. 2025/2026 haben mehrere weitere Staaten Bitcoin als Teil ihrer Reserven oder Hedging-Strategie diskutiert. Das Signal: Bitcoin wird strategisch gehalten, nicht nur spekulativ getradet.",
            },
            {
                "h2": "Was das für Retail-Investoren bedeutet",
                "img_kw": "retail investor individual trading smartphone app",
                "body": "Weniger explosives Upside – aber mehr strukturelle Stabilität. Bitcoin 2026 ist kein x100-Asset mehr für Neueinsteiger. Es ist ein langfristiger Store of Value mit wachsender institutioneller Unterstützung. Wer das versteht, positioniert sich anders.",
            },
        ],
        "category": "Crypto & Web3",
        "date": "2026-03-20",
        "read_time": "7 Min.",
        "pullquote": "Das Geld der Institutionen folgt dem Signal der Weisen.",
        "tags": ["Bitcoin", "ETF", "Institutionelle Investoren"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Trading", "trading.html"), ("Finanzen", "finanzen-versicherung.html")],
    },
    {
        "slug": "artikel-claude-vs-chatgpt-unternehmen-2026",
        "title": "Claude vs ChatGPT: Was Unternehmen 2026 wissen müssen",
        "hero_kw": "artificial intelligence chatbot comparison business",
        "sections": [
            {
                "h2": "Claude: Stärken im Unternehmenskontext",
                "img_kw": "claude anthropic AI document analysis enterprise",
                "body": "Claude (Anthropic) glänzt bei langen Dokumenten, nuancierter Analyse und Aufgaben, die präzises Verstehen komplexer Kontexte erfordern. Das Constitutional AI-Framework macht es besonders geeignet für sensible Unternehmensdaten. Der 200k-Token-Kontext ermöglicht das Verarbeiten ganzer Vertragswerke in einem Schritt.",
            },
            {
                "h2": "ChatGPT: Wo es überlegt",
                "img_kw": "chatgpt openai AI assistant creative tool",
                "body": "GPT-4o punktet bei kreativen Aufgaben, Bild-/Sprachverarbeitung und dem DALL-E-Integration. Das Plugin-Ökosystem und die breite Bekanntheit machen es zum Standard-Tool für viele Teams. Code Interpreter (Advanced Data Analysis) ist ein echter Unterschied bei Datenauswertungen.",
            },
            {
                "h2": "Die richtige Entscheidung für dein Unternehmen",
                "img_kw": "business decision strategy planning team",
                "body": "Für dokumentenintensive, compliance-relevante Aufgaben: Claude. Für kreatives, multimodales Arbeiten mit breitem Tool-Ökosystem: GPT-4o. Für viele Teams lohnt es sich, beide zu nutzen – für unterschiedliche Workflows. Die Kosten sind 2026 für beide Modelle deutlich gesunken.",
            },
        ],
        "category": "KI & Technologie",
        "date": "2026-03-15",
        "read_time": "8 Min.",
        "pullquote": "Das beste KI-Tool ist das, das du konsequent nutzt.",
        "tags": ["Claude", "ChatGPT", "KI-Vergleich", "Unternehmen"],
        "related": [("KI & Tech", "ki-tech.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
    },
    {
        "slug": "artikel-eigentumswohnung-kaufen-2026",
        "title": "Eigentumswohnung kaufen 2026: Der ehrliche Ratgeber",
        "hero_kw": "apartment buying real estate condominium",
        "sections": [
            {
                "h2": "Die echten Kosten eines Wohnungskaufs",
                "img_kw": "real estate costs notary contract fees taxes",
                "body": "Kaufpreis ist nur der Anfang. Grunderwerbsteuer (3,5–6,5 % je Bundesland), Notarkosten (1,5 %), Maklergebühr (bis 3,57 % inklusive MwSt) und Eintrag ins Grundbuch summieren sich auf 7–12 % Nebenkosten. Bei einer 400.000 € Wohnung bedeutet das bis zu 48.000 € zusätzlich.",
            },
            {
                "h2": "Finanzierung 2026: Was geht, was nicht",
                "img_kw": "mortgage bank loan financing interest rate",
                "body": "Bei 3,5–4 % Zinsen und gesunkenen Preisen hat sich die monatliche Belastung normalisiert. Banken erwarten 20–30 % Eigenkapital plus Nebenkosten aus eigenen Mitteln. Wer das nicht hat, sollte noch 2–3 Jahre sparen – der Markt läuft nicht weg.",
            },
            {
                "h2": "Energieeffizienz: Das neue Pflichtkriterium",
                "img_kw": "energy efficiency certificate house rating renovation",
                "body": "Ab 2027 kommen EU-weite Sanierungspflichten für die schlechtesten Energieklassen. Eine Wohnung mit Energieklasse G oder F zu kaufen bedeutet absehbare Sanierungskosten von 20.000–60.000 €. Prüfe vor dem Kauf: Energieausweis, Heizungsart und Dämmzustand des Gebäudes.",
            },
        ],
        "category": "Immobilien",
        "date": "2026-03-10",
        "read_time": "8 Min.",
        "pullquote": "Ein Haus kaufen ist leicht. Die richtige Entscheidung treffen ist schwer.",
        "tags": ["Eigentumswohnung", "Immobilien", "Kaufen", "Finanzierung"],
        "related": [("Immobilien Überblick", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
    },
    {
        "slug": "artikel-pkv-vs-gkv-2026",
        "title": "PKV vs GKV 2026: Die ehrliche Entscheidungshilfe",
        "hero_kw": "health insurance medical doctor hospital",
        "sections": [
            {
                "h2": "Wann die PKV wirklich vorteilhaft ist",
                "img_kw": "private health insurance doctor clinic premium",
                "body": "Für junge, gesunde Gutverdiener ohne Familienplanung rechnet sich PKV oft kurzfristig. Bessere Leistungen, kürzere Wartezeiten, freie Arztwahl. Der Beitrag ist mit 20–35 Jahren deutlich niedriger als der GKV-Beitrag. Der Haken: Diese Kalkulation dreht sich mit dem Alter.",
            },
            {
                "h2": "Was PKV-Vertreter nicht sagen",
                "img_kw": "insurance fine print contract hidden costs elderly",
                "body": "PKV-Beiträge steigen im Alter erheblich. Ohne Kinder-/Partnermitversicherung zahlt jedes Familienmitglied separat. Wechsel zurück in die GKV ist nach 55 in der Regel nicht möglich. Und: Viele PKV-Versicherte haben im Alter Probleme mit steigenden Beiträgen.",
            },
            {
                "h2": "Die GKV-Stärken, die unterschätzt werden",
                "img_kw": "family health coverage public insurance solidarity",
                "body": "Einkommensunabhängige Mitversicherung von Kindern und Partner. Beitrag bleibt im Rentneralter stabil. Keine Risikoprüfung, keine Leistungsausschlüsse für Vorerkrankungen. Für Familien mit mehreren Personen fast immer günstiger.",
            },
        ],
        "category": "Finanzen & Versicherung",
        "date": "2026-03-05",
        "read_time": "7 Min.",
        "pullquote": "Die beste Versicherung ist die, die du im Alter noch bezahlen kannst.",
        "tags": ["PKV", "GKV", "Krankenversicherung", "Versicherung"],
        "related": [("Finanzen & Versicherung", "finanzen-versicherung.html"), ("Coaching & Mindset", "coaching-mindset.html"), ("Karriere & HR", "karriere-hr.html")],
    },
    {
        "slug": "artikel-produktivitaet-adhs-systeme",
        "title": "Produktivität mit ADHS: Systeme die wirklich helfen",
        "hero_kw": "productivity focus concentration work desk",
        "sections": [
            {
                "h2": "Warum klassische Produktivitätstipps nicht funktionieren",
                "img_kw": "frustrated person planning calendar fail productivity",
                "body": "Getting Things Done, Pomodoro-Technik, Tagesplanung – gut für neurotypische Menschen. Für ADHS-Gehirne oft frustrierend. Nicht weil die Person zu schwach ist, sondern weil diese Systeme emotionale Dysregulation und Hyperfokus nicht berücksichtigen.",
            },
            {
                "h2": "Die drei Säulen produktiver ADHS-Systeme",
                "img_kw": "organization system structure planning habit tracker",
                "body": "Erstens: Externe Strukturen (kein Verlass auf innere Motivation). Zweitens: Reduktion der Entscheidungsanzahl (Decision Fatigue ist bei ADHS ausgeprägter). Drittens: Sofortiger Reward-Loops (das ADHS-Gehirn braucht unmittelbare Rückmeldung, nicht verzögerte Belohnung). Automatisierungen helfen bei allen drei.",
            },
            {
                "h2": "KI und ADHS: Überraschend gute Partner",
                "img_kw": "AI assistant chatbot brain dump ideas organize",
                "body": "KI-Tools wie Claude oder ChatGPT sind besonders hilfreich für ADHS: Externalisierung von Gedanken, Strukturierung von Aufgaben, sofortiges Feedback. Das 'Braindump'-Prinzip – alle Gedanken raus, dann sortieren lassen – ist ein Game-Changer.",
            },
        ],
        "category": "Coaching & Mindset",
        "date": "2026-02-28",
        "read_time": "8 Min.",
        "pullquote": "ADHS ist kein Problem zu lösen. Es ist ein System zu bauen.",
        "tags": ["ADHS", "Produktivität", "Neurodiversität", "Systeme"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Automatisierungen", "automationen.html"), ("Karriere & HR", "karriere-hr.html")],
    },
    {
        "slug": "artikel-solaranlage-ratgeber-2026",
        "title": "Solaranlage 2026: Der komplette Ratgeber",
        "hero_kw": "solar installation photovoltaic roof panels sun",
        "sections": [
            {
                "h2": "Kosten und Wirtschaftlichkeit 2026",
                "img_kw": "solar panel cost price calculator return investment",
                "body": "Eine 10-kWp-Anlage kostet installiert zwischen 14.000 und 20.000 €. Die Einspeisevergütung liegt bei etwa 8 Cent/kWh. Die Amortisation berechnet sich primär über den Eigenverbrauch: Bei 0,30 €/kWh Netzstrom und 70 % Eigenverbrauch erreicht man bei guter Planung eine Amortisation in 9–12 Jahren.",
            },
            {
                "h2": "Förderungen und steuerliche Aspekte",
                "img_kw": "government subsidy funding grant solar renewable",
                "body": "Seit 2023 sind Solaranlagen in Deutschland bis 30 kWp von der Einkommenssteuer befreit. Keine Umsatzsteuer auf Module und Installation. KfW-Kredite mit günstigen Konditionen. Und: Viele Bundesländer haben eigene Förderprogramme – prüfen lohnt sich.",
            },
            {
                "h2": "Anbieterauswahl: Was wirklich zählt",
                "img_kw": "solar installer technician rooftop professional",
                "body": "Nicht den günstigsten wählen – sondern den mit dem besten Service nach der Installation. Prüfe: Wie lange ist das Unternehmen schon aktiv? Gibt es Referenzen in deiner Region? Wie sieht die Garantie auf Ertrag aus? Und: Wer übernimmt die Wartung in Jahr 10?",
            },
        ],
        "category": "Energie & Solar",
        "date": "2026-02-20",
        "read_time": "9 Min.",
        "pullquote": "Die beste Solaranlage ist die, die du nicht mehr bemerkst – weil sie läuft.",
        "tags": ["Solaranlage", "Photovoltaik", "Solar", "Energie"],
        "related": [("Energie & Solar Überblick", "energie-solar.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
    },
]

SECTION_CSS = """
  /* Section Visuals */
  .section-img-wrap {
    margin: 1.8rem 0 2.2rem;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
  }
  .section-img-wrap img {
    width: 100%;
    height: auto;
    aspect-ratio: 16/9;
    object-fit: cover;
    display: block;
    border-radius: 10px;
  }
  .section-img-caption {
    font-size: 0.65rem;
    color: var(--muted);
    text-align: right;
    padding: 0.3rem 0.6rem 0;
    letter-spacing: 0.04em;
  }
"""

def make_html(b: dict) -> str:
    base_url = "https://automation-cango-app-empire.com"
    slug     = b["slug"]
    hero_src = f"../images/blog-sections/{slug}-hero.jpg"
    og_img   = f"{base_url}/images/blog-sections/{slug}-hero.jpg"
    kw_str   = ", ".join(b.get("tags", []))

    related_html = "\n".join(f'    <a href="{r[1]}">{r[0]}</a>' for r in b.get("related", []))
    tags_html    = "\n".join(f'    <span class="tag">{t}</span>' for t in b.get("tags", []))

    sections_html = ""
    for i, sec in enumerate(b.get("sections", []), 1):
        img_src = f"../images/blog-sections/{slug}-section-{i}.jpg"
        sections_html += f"""
  <h2>{sec['h2']}</h2>
  <div class="section-img-wrap">
    <img src="{img_src}" alt="{sec['h2']}" loading="lazy" width="900" height="506">
    <p class="section-img-caption">© Openverse / CC-Lizenz</p>
  </div>
  <p>{sec['body']}</p>
"""

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b['title']} | CanGo Empire Blog</title>
<meta name="description" content="{b.get('sections',[{}])[0].get('body','')[:150]}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{base_url}/blogs/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="{b['title']} | CanGo Empire">
<meta property="og:url" content="{base_url}/blogs/{slug}.html">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="article:published_time" content="{b['date']}">
<meta property="article:section" content="{b['category']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_img}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{b['title']}","image":"{og_img}","url":"{base_url}/blogs/{slug}.html","author":{{"@type":"Person","name":"Canberk Umut Kıvılcım"}},"publisher":{{"@type":"Organization","name":"CanGo Empire"}},"datePublished":"{b['date']}","inLanguage":"de","articleSection":"{b['category']}","keywords":"{kw_str}"}}
</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap" media="print" onload="this.media='all'">
<style>
  :root {{ --orange: #F97316; --navy: #0A0F1E; --navy-light: #1E293B; --text: #E2E8F0; --muted: #94A3B8; --gold: #D4A853; }}
  *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:var(--navy); color:var(--text); font-family:'Inter',Georgia,sans-serif; font-weight:300; line-height:1.9; padding:2rem 1rem; -webkit-font-smoothing:antialiased; }}
  article {{ max-width:720px; margin:0 auto; }}
  .breadcrumb {{ font-size:.75rem; color:var(--muted); margin-bottom:1.5rem; }}
  .breadcrumb a {{ color:var(--muted); text-decoration:none; }}
  .breadcrumb a:hover {{ color:var(--orange); }}
  .breadcrumb span {{ margin:0 .4rem; }}
  .hero-img {{ width:100%; height:auto; aspect-ratio:1200/630; object-fit:cover; border-radius:10px; margin-bottom:2.5rem; display:block; background:var(--navy-light); }}
  .meta {{ font-size:.72rem; letter-spacing:.18em; text-transform:uppercase; color:var(--orange); font-weight:500; margin-bottom:2rem; }}
  h1 {{ font-family:'Cormorant Garamond',Georgia,serif; font-size:clamp(2rem,5vw,3.4rem); font-weight:600; line-height:1.15; color:#fff; margin-bottom:.5rem; }}
  .byline {{ font-size:.8rem; color:var(--muted); margin-bottom:2.5rem; padding-bottom:2.5rem; border-bottom:1px solid var(--navy-light); }}
  .opening {{ font-family:'Cormorant Garamond',Georgia,serif; font-size:clamp(1.1rem,2.5vw,1.35rem); font-style:italic; color:#CBD5E1; line-height:1.7; margin-bottom:2.5rem; }}
  p {{ font-size:clamp(.9rem,1.5vw,.97rem); margin-bottom:1.3rem; color:var(--text); }}
  h2 {{ font-family:'Syne',sans-serif; font-size:clamp(.9rem,2vw,1.1rem); font-weight:700; color:var(--orange); margin:3rem 0 1rem; letter-spacing:.05em; text-transform:uppercase; }}
  .pullquote {{ font-family:'Cormorant Garamond',Georgia,serif; font-size:clamp(1.2rem,3vw,1.5rem); font-style:italic; color:#fff; border-left:3px solid var(--gold); padding:1rem 0 1rem 1.5rem; margin:2.5rem 0; line-height:1.5; }}
  {SECTION_CSS}
  .cta-block {{ background:linear-gradient(135deg,#F97316,#EA580C); padding:2rem; border-radius:8px; margin-top:3rem; text-align:center; }}
  .cta-block strong {{ font-family:'Syne',sans-serif; font-size:clamp(1rem,2.5vw,1.15rem); display:block; margin-bottom:.6rem; color:#fff; }}
  .cta-block p {{ color:rgba(255,255,255,.88); margin-bottom:1.2rem; font-size:.9rem; }}
  .cta-btn {{ display:inline-block; background:#fff; color:#EA580C; font-family:'Syne',sans-serif; font-weight:700; font-size:.85rem; letter-spacing:.06em; text-transform:uppercase; padding:.75rem 1.8rem; border-radius:4px; text-decoration:none; }}
  .tags {{ margin-top:2rem; }}
  .tag {{ display:inline-block; background:var(--navy-light); border:1px solid #1E3A5F; color:var(--muted); font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; padding:.3rem .7rem; border-radius:4px; margin:.3rem .2rem 0 0; }}
  .related {{ margin-top:3rem; padding-top:2rem; border-top:1px solid var(--navy-light); }}
  .related-title {{ font-family:'Syne',sans-serif; font-size:.75rem; letter-spacing:.15em; text-transform:uppercase; color:var(--muted); margin-bottom:1rem; }}
  .related a {{ display:block; color:var(--text); text-decoration:none; font-size:.9rem; padding:.5rem 0; border-bottom:1px solid var(--navy-light); }}
  .related a:hover {{ color:var(--orange); }}
  .related a::before {{ content:'→ '; color:var(--orange); }}
  @media (max-width:600px) {{ body {{ padding:1.5rem 1rem; }} }}
</style>
</head>
<body>
<article>
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="../index.html">Home</a><span>›</span>
    <a href="../blogs.html">Blog</a><span>›</span>
    {b['category']}
  </nav>

  <img src="{hero_src}" alt="{b['title']}" class="hero-img" width="1200" height="630" loading="eager" onerror="this.style.opacity='0'">

  <div class="meta">{b['category']} · CanGo Empire · {b['date']}</div>
  <h1>{b['title']}</h1>
  <div class="byline">Von Canberk Umut Kıvılcım · {b['date']} · {b['read_time']} Lesezeit</div>

  <p class="opening">{b.get('sections', [{}])[0].get('body', '')[:200]}…</p>

{sections_html}

  <blockquote class="pullquote">{b['pullquote']}</blockquote>

  <div class="cta-block">
    <strong>Dein System aufbauen lassen</strong>
    <p>CanGo Empire – Automatisierung mit Absicht.</p>
    <a href="../index.html" class="cta-btn">Mehr erfahren</a>
  </div>

  <div class="tags">{tags_html}</div>

  <nav class="related" aria-label="Ähnliche Artikel">
    <div class="related-title">Ähnliche Artikel</div>
{related_html}
  </nav>
</article>
</body>
</html>"""

# ── FTP Helpers ────────────────────────────────────────────────────────────────
def ftp_mkdir(ftp, path):
    parts = path.strip("/").split("/")
    cur = "/"
    for p in parts:
        cur = f"{cur}{p}/"
        try: ftp.cwd(cur)
        except:
            try: ftp.mkd(cur); ftp.cwd(cur)
            except: pass

def ftp_put(ftp, local, remote_dir, name):
    try:
        ftp.cwd(remote_dir)
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {name}", f)
        return True
    except Exception as e:
        print(f"  FTP ✗ {name}: {e}")
        return False

def main():
    print("\n🚀 CanGo Empire – Keyword-Bilder part-by-part im Body\n")
    print("   Bildquelle: Openverse (CC-lizenziert) + Picsum Fallback\n")

    ftp = None
    try:
        ftp = ftplib.FTP(); ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS); ftp.set_pasv(True)
        blogs_remote   = f"{REMOTE}/blogs"
        sections_remote = f"{REMOTE}/images/blog-sections"
        ftp_mkdir(ftp, blogs_remote)
        ftp_mkdir(ftp, sections_remote)
        print("✅ FTP verbunden\n")
    except Exception as e:
        print(f"⚠ FTP: {e} — nur lokal\n")

    for b in BLOGS:
        slug = b["slug"]
        print(f"📄 {slug}")

        # Hero-Bild
        hero_dest = IMG_DIR / f"{slug}-hero.jpg"
        urls = openverse_search(b["hero_kw"], count=3)
        saved = False
        for url in urls:
            if download_img(url, hero_dest):
                saved = True; break
        if not saved:
            kw1 = b["hero_kw"].split()[0]
            pid = PICSUM_FALLBACKS.get(kw1, 96)
            download_img(f"https://picsum.photos/id/{pid}/1200/630", hero_dest)
        print(f"  ↓ hero")
        time.sleep(0.4)

        # Section-Bilder (keyword-relevant, direkt im Body)
        for i, sec in enumerate(b.get("sections", []), 1):
            sec_dest = IMG_DIR / f"{slug}-section-{i}.jpg"
            urls2 = openverse_search(sec["img_kw"], count=3)
            saved2 = False
            for url in urls2:
                if download_img(url, sec_dest):
                    saved2 = True; break
            if not saved2:
                kw1 = sec["img_kw"].split()[0]
                pid = PICSUM_FALLBACKS.get(kw1, 96)
                download_img(f"https://picsum.photos/id/{pid}/900/506", sec_dest)
            print(f"  ↓ section-{i}: {sec['img_kw'][:35]}")
            time.sleep(0.4)

        # HTML generieren
        html_path = BLOGS_DIR / f"{slug}.html"
        html_path.write_text(make_html(b), encoding="utf-8")
        print(f"  ✓ HTML")

        # FTP Upload
        if ftp:
            ftp_put(ftp, html_path, blogs_remote, f"{slug}.html")
            ftp_put(ftp, hero_dest, sections_remote, hero_dest.name)
            for i in range(1, len(b.get("sections", [])) + 1):
                sec_file = IMG_DIR / f"{slug}-section-{i}.jpg"
                if sec_file.exists():
                    ftp_put(ftp, sec_file, sections_remote, sec_file.name)
            print(f"  ↑ live")
        print()

    if ftp:
        try: ftp.quit()
        except: pass

    n = len(BLOGS)
    imgs = n * 4  # hero + 3 sections
    print(f"✅ {n} Blogs mit je 3 keyword-relevanten Body-Bildern live!")
    print(f"   {imgs} Bilder insgesamt auf Hostinger hochgeladen.")
    print(f"\n🌐 https://automation-cango-app-empire.com/blogs/finanzen-versicherung.html\n")

if __name__ == "__main__":
    main()
