#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Blogs mit Wikimedia-Bildern (keyword-relevant) + Body-Sections
Jedes Bild ist präzise nach dem Abschnittsthema gesucht.
Bilder erscheinen part-by-part direkt nach jeder h2 im Body.
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

IMG_EXTS = {"jpg", "jpeg", "png", "webp"}

# ── Wikimedia Commons Suche ────────────────────────────────────────────────────
def wikimedia_search(query: str, count: int = 5) -> list[tuple[str, str]]:
    """Gibt Liste von (title, thumb_url) für JPG/PNG zurück."""
    q = urllib.parse.quote(query)
    url = (f"https://commons.wikimedia.org/w/api.php"
           f"?action=query&list=search&srsearch={q}&srnamespace=6"
           f"&format=json&srlimit={count}&srprop=")
    req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0 (blog@automation-cango-app-empire.com)"})
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read())
        titles = [s["title"] for s in data.get("query", {}).get("search", [])]
        # Nur Bildformate
        titles = [t for t in titles if t.split(".")[-1].lower() in IMG_EXTS]
        return titles
    except Exception as e:
        print(f"  ⚠ Wikimedia Suche: {e}")
        return []

def wikimedia_url(title: str, width: int = 1200) -> str | None:
    t = urllib.parse.quote(title.replace("File:", "").replace(" ", "_"))
    url = (f"https://commons.wikimedia.org/w/api.php"
           f"?action=query&titles=File:{t}&prop=imageinfo&iiprop=url"
           f"&iiurlwidth={width}&format=json")
    req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        for page in data.get("query", {}).get("pages", {}).values():
            ii = page.get("imageinfo", [{}])
            if ii:
                return ii[0].get("thumburl") or ii[0].get("url")
    except:
        pass
    return None

def download(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 8000:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            dest.write_bytes(r.read())
        return dest.stat().st_size > 5000
    except:
        return False

PICSUM_MAP = {
    "bitcoin": 730, "crypto": 180, "blockchain": 325, "ethereum": 442,
    "solar": 459, "energy": 974, "photovoltaic": 129, "battery": 1,
    "real": 164, "apartment": 547, "house": 1080, "building": 129,
    "finance": 210, "insurance": 260, "money": 172, "savings": 534,
    "artificial": 442, "technology": 96, "computer": 325, "data": 180,
    "trading": 534, "stock": 172, "market": 210, "chart": 96,
    "career": 375, "office": 399, "team": 260, "work": 210,
    "coaching": 573, "mindset": 399, "motivation": 1024, "habit": 260,
    "automation": 1036, "workflow": 442, "crm": 325, "content": 96,
    "health": 375, "doctor": 260, "hospital": 399, "medical": 573,
    "productivity": 260, "focus": 399, "organization": 260, "adhd": 573,
    "default": 96,
}

def fallback_img(keyword: str, dest: Path, w: int, h: int) -> bool:
    k = keyword.lower().split()[0]
    pid = PICSUM_MAP.get(k, PICSUM_MAP["default"])
    return download(f"https://picsum.photos/id/{pid}/{w}/{h}", dest)

def get_img(keyword: str, dest: Path, w: int = 1200, h: int = 675) -> bool:
    """Holt Wikimedia-Bild für Keyword oder Fallback."""
    titles = wikimedia_search(keyword, count=8)
    for t in titles[:4]:
        url = wikimedia_url(t, width=w)
        if url and download(url, dest):
            return True
        time.sleep(0.15)
    return fallback_img(keyword, dest, w, h)

# ── Blog-Definitionen ─────────────────────────────────────────────────────────
BLOGS = [
    {
        "slug": "finanzen-versicherung",
        "title": "Finanzen & Versicherung 2026: Was wirklich zählt",
        "category": "Finanzen & Versicherung",
        "date": "2026-04-10", "read_time": "6 Min.",
        "hero_kw": "personal finance money coins savings",
        "pullquote": "Finanzielle Freiheit ist keine Zahl. Sie ist ein Zustand.",
        "tags": ["ETF", "Versicherung", "Finanzen", "Rücklage"],
        "related": [("Immobilien", "immobilien.html"), ("Trading", "trading.html"), ("PKV vs GKV", "artikel-pkv-vs-gkv-2026.html")],
        "sections": [
            {"h2": "Warum Versicherungen neu gedacht werden müssen",
             "img_kw": "insurance contract document signing",
             "body": "Die klassische Vollkasko-Mentalität stirbt langsam aus. Verbraucher wollen verstehen, wofür sie zahlen. Modulare Tarife, digitale Schadensmeldung und KI-gestützte Risikoanalyse verändern die Branche grundlegend. Wer heute abschließt, sollte auf Flexibilität achten – nicht auf maximale Absicherung gegen unwahrscheinliche Szenarien."},
            {"h2": "ETF-Sparplan vs. aktiv gemanagter Fonds",
             "img_kw": "stock exchange trading floor ETF fund",
             "body": "Die Daten sprechen seit Jahren eine klare Sprache: Über 80 % der aktiv gemanagten Fonds schlagen ihren Vergleichsindex nicht. Ein diversifizierter ETF-Sparplan – monatlich, automatisiert, kostengünstig – ist für die meisten Menschen die überlegene Strategie."},
            {"h2": "Notfallgroschen, Rücklage, Vermögen – die drei Schichten",
             "img_kw": "piggy bank savings money coins jar",
             "body": "Finanziell resilient zu sein bedeutet nicht reich zu sein. Es bedeutet, strukturiert vorzugehen: drei Monatsgehälter liquid halten, dann Schulden tilgen, dann Vermögen aufbauen. Diese Reihenfolge klingt banal – wird aber von den meisten nicht eingehalten. Das ist der eigentliche Hebel."},
        ],
    },
    {
        "slug": "crypto-web3",
        "title": "Crypto & Web3 2026: Was bleibt, was kommt",
        "category": "Crypto & Web3",
        "date": "2026-04-11", "read_time": "7 Min.",
        "hero_kw": "bitcoin cryptocurrency digital coin",
        "pullquote": "Die beste Technologie verschwindet in der Infrastruktur.",
        "tags": ["Bitcoin", "Ethereum", "Web3", "DeFi"],
        "related": [("Bitcoin Institutionen", "artikel-bitcoin-institutionen-2026.html"), ("Trading", "trading.html"), ("KI & Tech", "ki-tech.html")],
        "sections": [
            {"h2": "Bitcoin als Reserveasset – Realität oder Wunschdenken?",
             "img_kw": "bitcoin gold physical coin cryptocurrency",
             "body": "Wenn BlackRock, Fidelity und staatliche Pensionsfonds Bitcoin halten, ist die Diskussion über seine Legitimität beendet. 2026 sehen wir die erste Welle echter Integration in traditionelle Portfolios. Das bedeutet weniger Volatilität, aber auch weniger explosive Renditen. Bitcoin wird Infrastruktur."},
            {"h2": "Ethereum: Wo steht das Ökosystem?",
             "img_kw": "ethereum logo blockchain network",
             "body": "Layer-2-Lösungen wie Arbitrum und Base haben das Skalierungsproblem gelöst. Gas-Gebühren unter einem Cent sind Realität. Was fehlt, ist die Killer-App – die Anwendung, die normale Menschen täglich nutzen. DeFi, NFTs und Gaming haben Pionierarbeit geleistet."},
            {"h2": "Web3 jenseits des Hypes",
             "img_kw": "decentralized network blockchain nodes distributed",
             "body": "Die interessantesten Web3-Projekte 2026 sind die unspektakulären: digitale Identität, dezentrale Datenspeicherung, tokenisierte Real-World-Assets. Sie lösen echte Probleme, ohne dass die Nutzer wissen müssen, dass sie auf einer Blockchain laufen."},
        ],
    },
    {
        "slug": "energie-solar",
        "title": "Energie & Solar 2026: Der Eigenverbrauch-Boom",
        "category": "Energie & Solar",
        "date": "2026-04-09", "read_time": "6 Min.",
        "hero_kw": "solar panels rooftop renewable energy sun",
        "pullquote": "Energie erzeugen ist Freiheit. Energie sparen ist Strategie.",
        "tags": ["Solar", "Photovoltaik", "Speicher", "Wärmepumpe"],
        "related": [("Solaranlage Ratgeber", "artikel-solaranlage-ratgeber-2026.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Solaranlage 2026 – Rechnet es sich noch?",
             "img_kw": "photovoltaic solar panel installation roof",
             "body": "Ja – mit Einschränkungen. Die Einspeisevergütung ist gesunken, aber die Modulpreise auch. Entscheidend ist jetzt der Eigenverbrauchsanteil: Wer 60–70 % selbst verbraucht (z.B. durch E-Auto oder Wärmepumpe), amortisiert die Anlage in 8–10 Jahren."},
            {"h2": "Batteriespeicher: Wann ist er sinnvoll?",
             "img_kw": "home battery energy storage system power",
             "body": "Ein Speicher lohnt sich, wenn dein Eigenverbrauch unter 40 % liegt und du ihn damit auf 70–80 % heben kannst. Die Preise für Heimspeicher sind 2025/2026 deutlich gefallen – 5–10 kWh sind jetzt für 4.000–7.000 € realistisch."},
            {"h2": "Der ganzheitliche Energiehaushalt",
             "img_kw": "electric car charging heat pump smart home",
             "body": "Solar + Speicher + Wärmepumpe + E-Auto ist das Quadruple-Play der Energiewende. Wer alle vier Komponenten optimiert und intelligent vernetzt, kann theoretisch nahezu energieautark leben."},
        ],
    },
    {
        "slug": "immobilien",
        "title": "Immobilien 2026: Kaufen, Mieten oder Warten?",
        "category": "Immobilien",
        "date": "2026-04-08", "read_time": "7 Min.",
        "hero_kw": "apartment building real estate architecture",
        "pullquote": "Immobilien sind kein Investment. Sie sind Infrastruktur.",
        "tags": ["Immobilien", "Kaufen", "Mieten", "Zinsen"],
        "related": [("Eigentumswohnung kaufen", "artikel-eigentumswohnung-kaufen-2026.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
        "sections": [
            {"h2": "Wo stehen die Preise wirklich?",
             "img_kw": "real estate house price for sale sign",
             "body": "In B- und C-Städten sind Preise teilweise 15–25 % unter dem Peak 2022. In Top-7-Städten nur 8–12 %. Das klingt nach Einstiegsgelegenheit – aber die Kaufnebenkosten (7–12 %), gestiegene Zinsen (3,5–4 %) und höhere Anforderungen an die Energieeffizienz ändern die Kalkulation fundamental."},
            {"h2": "Eigennutzung vs. Kapitalanlage",
             "img_kw": "apartment interior living room modern flat",
             "body": "Wer zur Eigennutzung kauft, denkt in Jahrzehnten – und das ist richtig. Wer als Investition kauft, muss mit realistischen Mietrenditen kalkulieren. In vielen Lagen liegt die Bruttomietrendite unter 3 % – nach Verwaltung, Instandhaltung und Finanzierung oft im negativen Bereich."},
            {"h2": "Was 2026 wirklich zählt beim Kauf",
             "img_kw": "building energy certificate renovation insulation",
             "body": "Lage, Energieeffizienz und Finanzierungsstruktur. Ein Haus mit Energieklasse G ist 2026 nicht mehr verkäuflich ohne erhebliche Abschläge – und bis 2030 kommen Sanierungspflichten."},
        ],
    },
    {
        "slug": "ki-tech",
        "title": "KI & Tech 2026: Was jetzt wirklich passiert",
        "category": "KI & Technologie",
        "date": "2026-04-07", "read_time": "8 Min.",
        "hero_kw": "artificial intelligence robot technology future",
        "pullquote": "KI gibt dir nicht mehr Ideen. Sie gibt dir mehr Zeit für die richtigen.",
        "tags": ["KI", "Künstliche Intelligenz", "ChatGPT", "Automatisierung"],
        "related": [("Claude vs ChatGPT", "artikel-claude-vs-chatgpt-unternehmen-2026.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
        "sections": [
            {"h2": "Von ChatGPT zur KI-Infrastruktur",
             "img_kw": "artificial intelligence neural network computer",
             "body": "Der Markt hat sich konsolidiert. Anthropic, OpenAI, Google und Meta liefern Foundation Models, auf denen Tausende Anwendungen aufbauen. Wer heute KI als Werkzeug nutzt, hat einen Produktivitätsvorteil. Wer KI in seine Systeme integriert, hat einen strukturellen Vorteil."},
            {"h2": "Was Unternehmen jetzt tun sollten",
             "img_kw": "office team meeting technology laptop business",
             "body": "Nicht 'Was kann KI?' – sondern 'Welche unserer Prozesse kosten am meisten Zeit mit dem geringsten Wert?' Das ist die richtige Frage. Content-Erstellung, Kundenservice, Datenanalyse und interne Dokumentation sind die vier Bereiche mit dem besten ROI bei KI-Integration."},
            {"h2": "KI für Einzelpersonen: Der Hebel ist riesig",
             "img_kw": "freelancer home office laptop work productivity",
             "body": "Ein Solopreneur mit KI-Tools kann heute die Kapazität eines kleinen Teams erreichen. Content-Pipelines, automatisiertes Outreach, Marktrecherche, Code-Generierung – alles machbar ohne Programmierkenntnisse."},
        ],
    },
    {
        "slug": "trading",
        "title": "Trading 2026: Strategien die funktionieren",
        "category": "Trading",
        "date": "2026-04-06", "read_time": "6 Min.",
        "hero_kw": "stock market trading chart financial",
        "pullquote": "Ein schlechtes System konsequent angewandt schlägt kein System.",
        "tags": ["Trading", "Börse", "Aktien", "Strategie"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Finanzen", "finanzen-versicherung.html"), ("Bitcoin", "artikel-bitcoin-institutionen-2026.html")],
        "sections": [
            {"h2": "Warum 90 % der Trader verlieren",
             "img_kw": "stock market crash red chart decline loss",
             "body": "Nicht weil der Markt gegen sie ist. Weil sie ohne Edge handeln, zu groß positionieren und emotional reagieren. Der Markt transferiert Kapital von Ungeduld zu Geduld. Wer das versteht, beginnt anders zu denken."},
            {"h2": "Systemisches Trading vs. diskretionäres Trading",
             "img_kw": "trading computer screen charts candlestick",
             "body": "Systemisches Trading (regelbasiert, automatisiert) schlägt diskretionäres Trading im Durchschnitt – nicht weil Regeln besser sind als Intuition, sondern weil Regeln konsistent sind. Backtesting, klare Entry/Exit-Kriterien und Risk-Management sind keine Optionen. Sie sind das Fundament."},
            {"h2": "Der psychologische Vorteil",
             "img_kw": "meditation calm focus concentration quiet",
             "body": "Wer sein System kennt und vertraut, handelt entspannter. Entspanntes Trading ist besseres Trading. Die wichtigste Fähigkeit ist nicht die Analyse – es ist die Disziplin, das System auch dann zu folgen, wenn der Markt sich falsch anfühlt."},
        ],
    },
    {
        "slug": "karriere-hr",
        "title": "Karriere & HR 2026: Der neue Arbeitsmarkt",
        "category": "Karriere & HR",
        "date": "2026-04-05", "read_time": "6 Min.",
        "hero_kw": "job interview business professional career",
        "pullquote": "Der wertvollste Mitarbeiter 2026 ist der, der KI orchestriert.",
        "tags": ["Karriere", "HR", "Remote Work", "Fachkräfte"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("KI & Tech", "ki-tech.html")],
        "sections": [
            {"h2": "Welche Skills 2026 wirklich gefragt sind",
             "img_kw": "skills training education learning workshop",
             "body": "KI-Kompetenz ist Pflicht, nicht Kür. Prompt Engineering, Datenanalyse, Systemdenken und die Fähigkeit, KI-Tools sinnvoll zu orchestrieren, sind die Schlüsselqualifikationen. Dazu kommen unverrückbar menschliche Skills: Kommunikation, Führung, Kreativität und Empathie."},
            {"h2": "Remote Work: Was wirklich bleibt",
             "img_kw": "remote work home office desk computer",
             "body": "Hybrid ist der Standard geworden. Vollständiges Remote ist für viele Unternehmen verhandelt – Ausnahme sind Tech-Unternehmen und internationale Teams. Wer remote arbeiten will, braucht nicht nur die Fähigkeit, sondern auch den Beweis, dass er eigenverantwortlich liefert."},
            {"h2": "Selbstständigkeit und Portfolio-Karriere",
             "img_kw": "entrepreneur startup founder business own",
             "body": "Immer mehr Hochqualifizierte verlassen die Festanstellung – nicht aus Not, sondern aus Kalkül. Mehrere Einkommensquellen, Kontrolle über Zeit und Projekte, weniger Organisationspolitik."},
        ],
    },
    {
        "slug": "coaching-mindset",
        "title": "Coaching & Mindset: Die innere Architektur des Erfolgs",
        "category": "Coaching & Mindset",
        "date": "2026-04-04", "read_time": "7 Min.",
        "hero_kw": "motivation success goal achievement mindset",
        "pullquote": "Du brauchst keine Motivation. Du brauchst ein System.",
        "tags": ["Coaching", "Mindset", "Growth Mindset", "Systeme"],
        "related": [("Karriere & HR", "karriere-hr.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("Automatisierungen", "automationen.html")],
        "sections": [
            {"h2": "Growth Mindset ist mehr als Buzzword",
             "img_kw": "learning brain education growth development",
             "body": "Carol Dwecks Forschung ist eindeutig: Menschen mit Growth Mindset – der Überzeugung, dass Fähigkeiten entwickelbar sind – erzielen langfristig bessere Ergebnisse. Nicht weil sie härter arbeiten, sondern weil sie anders auf Rückschläge reagieren. Fehler sind Feedback, keine Urteile."},
            {"h2": "Systeme schlagen Willenskraft",
             "img_kw": "daily routine habit planning notebook calendar",
             "body": "Willenskraft ist eine endliche Ressource. Wer sich auf sie verlässt, scheitert systematisch an schlechten Tagen. Systeme – Routinen, Umgebungsdesign, Automatisierungen – funktionieren auch wenn die Motivation niedrig ist."},
            {"h2": "Coaching: Wann macht es Sinn?",
             "img_kw": "mentor coaching conversation support listening",
             "body": "Coaching ist kein Allheilmittel – aber in den richtigen Momenten der effektivste Hebel. Wann es Sinn macht: bei Übergängen (Job, Beziehung, Projekt), bei wiederkehrenden Mustern und wenn du weißt was zu tun ist, aber es nicht tust."},
        ],
    },
    {
        "slug": "automationen",
        "title": "Automatisierungen 2026: Was du heute noch einrichten kannst",
        "category": "Automatisierungen",
        "date": "2026-04-03", "read_time": "8 Min.",
        "hero_kw": "automation robot industrial machine workflow",
        "pullquote": "Automatisiere das Wiederholbare. Fokussiere auf das Einzigartige.",
        "tags": ["n8n", "Automatisierung", "Make", "No-Code"],
        "related": [("Maschinen die dienen", "maschinen-die-dienen.html"), ("KI & Tech", "ki-tech.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Die No-Code/Low-Code Revolution",
             "img_kw": "software interface workflow drag drop tool",
             "body": "n8n, Make (Integromat), Zapier und neu: KI-Agenten via Anthropic oder OpenAI API. Die Tools sind so weit gereift, dass technisches Know-how kein Engpass mehr ist. Der Engpass ist die richtige Frage: Welcher Prozess kostet mich die meiste Zeit mit dem geringsten Wert?"},
            {"h2": "Content-Automatisierung: Was wirklich funktioniert",
             "img_kw": "blog content writing keyboard publish article",
             "body": "Vollautomatisierter Content ohne menschliche Kurierung ist erkennbar – und wird von Google zunehmend abgestraft. Die Zukunft ist semi-automatisiert: KI generiert Drafts, Menschen kurieren und veredeln. Wer diesen Workflow optimiert, publiziert 10x schneller ohne Qualitätsverlust."},
            {"h2": "Lead-Generierung und CRM-Automatisierung",
             "img_kw": "email marketing funnel sales CRM contact",
             "body": "Der größte ROI liegt oft nicht im Content, sondern im Follow-Up. Automatisierte E-Mail-Sequenzen, CRM-Updates durch Webhooks und KI-gestützte Personalisierung – wer das aufgebaut hat, verliert keine Leads mehr durch mangelnde Nachverfolgung."},
        ],
    },
    {
        "slug": "artikel-bitcoin-institutionen-2026",
        "title": "Bitcoin und Institutionen 2026: Eine neue Ära",
        "category": "Crypto & Web3",
        "date": "2026-03-20", "read_time": "7 Min.",
        "hero_kw": "bitcoin gold bar investment bank safe",
        "pullquote": "Das Geld der Institutionen folgt dem Signal der Weisen.",
        "tags": ["Bitcoin", "ETF", "Institutionelle Investoren"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Trading", "trading.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Bitcoin-ETFs: Zahlen und Fakten",
             "img_kw": "bitcoin ETF exchange traded fund certificate",
             "body": "Die ersten Spot-ETFs in den USA haben in den ersten 12 Monaten mehr Kapital angezogen als Gold-ETFs in ihrer Anfangsphase. Milliarden Dollar fließen monatlich in strukturierte Bitcoin-Produkte."},
            {"h2": "Staatsreserven: Wer folgt El Salvador?",
             "img_kw": "government parliament national reserve treasury",
             "body": "El Salvador war der Proof of Concept. 2025/2026 haben mehrere weitere Staaten Bitcoin als Teil ihrer Reserven oder Hedging-Strategie diskutiert. Das Signal: Bitcoin wird strategisch gehalten, nicht nur spekulativ getradet."},
            {"h2": "Was das für Retail-Investoren bedeutet",
             "img_kw": "individual investor smartphone trading app",
             "body": "Weniger explosives Upside – aber mehr strukturelle Stabilität. Bitcoin 2026 ist kein x100-Asset mehr für Neueinsteiger. Es ist ein langfristiger Store of Value mit wachsender institutioneller Unterstützung."},
        ],
    },
    {
        "slug": "artikel-claude-vs-chatgpt-unternehmen-2026",
        "title": "Claude vs ChatGPT: Was Unternehmen 2026 wissen müssen",
        "category": "KI & Technologie",
        "date": "2026-03-15", "read_time": "8 Min.",
        "hero_kw": "AI chatbot computer screen comparison",
        "pullquote": "Das beste KI-Tool ist das, das du konsequent nutzt.",
        "tags": ["Claude", "ChatGPT", "KI-Vergleich", "Unternehmen"],
        "related": [("KI & Tech", "ki-tech.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
        "sections": [
            {"h2": "Claude: Stärken im Unternehmenskontext",
             "img_kw": "AI document analysis text enterprise software",
             "body": "Claude (Anthropic) glänzt bei langen Dokumenten, nuancierter Analyse und Aufgaben, die präzises Verstehen komplexer Kontexte erfordern. Das Constitutional AI-Framework macht es besonders geeignet für sensible Unternehmensdaten."},
            {"h2": "ChatGPT: Wo es überlegt",
             "img_kw": "chatbot AI assistant creative tool digital",
             "body": "GPT-4o punktet bei kreativen Aufgaben, Bild-/Sprachverarbeitung und dem DALL-E-Integration. Das Plugin-Ökosystem und die breite Bekanntheit machen es zum Standard-Tool für viele Teams."},
            {"h2": "Die richtige Entscheidung für dein Unternehmen",
             "img_kw": "business strategy decision meeting whiteboard",
             "body": "Für dokumentenintensive, compliance-relevante Aufgaben: Claude. Für kreatives, multimodales Arbeiten mit breitem Tool-Ökosystem: GPT-4o. Für viele Teams lohnt es sich, beide zu nutzen – für unterschiedliche Workflows."},
        ],
    },
    {
        "slug": "artikel-eigentumswohnung-kaufen-2026",
        "title": "Eigentumswohnung kaufen 2026: Der ehrliche Ratgeber",
        "category": "Immobilien",
        "date": "2026-03-10", "read_time": "8 Min.",
        "hero_kw": "apartment condominium building purchase keys",
        "pullquote": "Ein Haus kaufen ist leicht. Die richtige Entscheidung treffen ist schwer.",
        "tags": ["Eigentumswohnung", "Immobilien", "Kaufen", "Finanzierung"],
        "related": [("Immobilien Überblick", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
        "sections": [
            {"h2": "Die echten Kosten eines Wohnungskaufs",
             "img_kw": "notary contract signing real estate purchase",
             "body": "Kaufpreis ist nur der Anfang. Grunderwerbsteuer (3,5–6,5 % je Bundesland), Notarkosten (1,5 %), Maklergebühr (bis 3,57 % inklusive MwSt) und Eintrag ins Grundbuch summieren sich auf 7–12 % Nebenkosten."},
            {"h2": "Finanzierung 2026: Was geht, was nicht",
             "img_kw": "mortgage bank loan financing house",
             "body": "Bei 3,5–4 % Zinsen und gesunkenen Preisen hat sich die monatliche Belastung normalisiert. Banken erwarten 20–30 % Eigenkapital plus Nebenkosten aus eigenen Mitteln."},
            {"h2": "Energieeffizienz: Das neue Pflichtkriterium",
             "img_kw": "energy efficiency house certificate insulation renovation",
             "body": "Ab 2027 kommen EU-weite Sanierungspflichten für die schlechtesten Energieklassen. Eine Wohnung mit Energieklasse G oder F zu kaufen bedeutet absehbare Sanierungskosten von 20.000–60.000 €."},
        ],
    },
    {
        "slug": "artikel-pkv-vs-gkv-2026",
        "title": "PKV vs GKV 2026: Die ehrliche Entscheidungshilfe",
        "category": "Finanzen & Versicherung",
        "date": "2026-03-05", "read_time": "7 Min.",
        "hero_kw": "health insurance medical stethoscope doctor",
        "pullquote": "Die beste Versicherung ist die, die du im Alter noch bezahlen kannst.",
        "tags": ["PKV", "GKV", "Krankenversicherung", "Versicherung"],
        "related": [("Finanzen & Versicherung", "finanzen-versicherung.html"), ("Coaching & Mindset", "coaching-mindset.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Wann die PKV wirklich vorteilhaft ist",
             "img_kw": "private clinic doctor hospital premium health",
             "body": "Für junge, gesunde Gutverdiener ohne Familienplanung rechnet sich PKV oft kurzfristig. Bessere Leistungen, kürzere Wartezeiten, freie Arztwahl. Der Beitrag ist mit 20–35 Jahren deutlich niedriger als der GKV-Beitrag."},
            {"h2": "Was PKV-Vertreter nicht sagen",
             "img_kw": "insurance policy fine print reading contract",
             "body": "PKV-Beiträge steigen im Alter erheblich. Ohne Kinder-/Partnermitversicherung zahlt jedes Familienmitglied separat. Wechsel zurück in die GKV ist nach 55 in der Regel nicht möglich."},
            {"h2": "Die GKV-Stärken, die unterschätzt werden",
             "img_kw": "family health care public system solidarity",
             "body": "Einkommensunabhängige Mitversicherung von Kindern und Partner. Beitrag bleibt im Rentneralter stabil. Keine Risikoprüfung, keine Leistungsausschlüsse für Vorerkrankungen."},
        ],
    },
    {
        "slug": "artikel-produktivitaet-adhs-systeme",
        "title": "Produktivität mit ADHS: Systeme die wirklich helfen",
        "category": "Coaching & Mindset",
        "date": "2026-02-28", "read_time": "8 Min.",
        "hero_kw": "productivity focus work desk concentration",
        "pullquote": "ADHS ist kein Problem zu lösen. Es ist ein System zu bauen.",
        "tags": ["ADHS", "Produktivität", "Neurodiversität", "Systeme"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Automatisierungen", "automationen.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Warum klassische Produktivitätstipps nicht funktionieren",
             "img_kw": "stress overwhelmed multitasking distraction",
             "body": "Getting Things Done, Pomodoro-Technik, Tagesplanung – gut für neurotypische Menschen. Für ADHS-Gehirne oft frustrierend. Nicht weil die Person zu schwach ist, sondern weil diese Systeme emotionale Dysregulation und Hyperfokus nicht berücksichtigen."},
            {"h2": "Die drei Säulen produktiver ADHS-Systeme",
             "img_kw": "planner calendar organization task board sticky",
             "body": "Erstens: Externe Strukturen (kein Verlass auf innere Motivation). Zweitens: Reduktion der Entscheidungsanzahl. Drittens: Sofortiger Reward-Loops (das ADHS-Gehirn braucht unmittelbare Rückmeldung, nicht verzögerte Belohnung)."},
            {"h2": "KI und ADHS: Überraschend gute Partner",
             "img_kw": "artificial intelligence assistant chat interface",
             "body": "KI-Tools wie Claude oder ChatGPT sind besonders hilfreich für ADHS: Externalisierung von Gedanken, Strukturierung von Aufgaben, sofortiges Feedback. Das 'Braindump'-Prinzip ist ein Game-Changer für Menschen, die im Kopf ständig übervolle Tabs haben."},
        ],
    },
    {
        "slug": "artikel-solaranlage-ratgeber-2026",
        "title": "Solaranlage 2026: Der komplette Ratgeber",
        "category": "Energie & Solar",
        "date": "2026-02-20", "read_time": "9 Min.",
        "hero_kw": "solar panel installation house rooftop photovoltaic",
        "pullquote": "Die beste Solaranlage ist die, die du nicht mehr bemerkst – weil sie läuft.",
        "tags": ["Solaranlage", "Photovoltaik", "Solar", "Energie"],
        "related": [("Energie & Solar Überblick", "energie-solar.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Kosten und Wirtschaftlichkeit 2026",
             "img_kw": "solar panel cost price kWh electricity meter",
             "body": "Eine 10-kWp-Anlage kostet installiert zwischen 14.000 und 20.000 €. Die Amortisation berechnet sich primär über den Eigenverbrauch: Bei 0,30 €/kWh Netzstrom und 70 % Eigenverbrauch erreicht man bei guter Planung eine Amortisation in 9–12 Jahren."},
            {"h2": "Förderungen und steuerliche Aspekte",
             "img_kw": "government grant subsidy renewable energy funding",
             "body": "Seit 2023 sind Solaranlagen in Deutschland bis 30 kWp von der Einkommenssteuer befreit. Keine Umsatzsteuer auf Module und Installation. KfW-Kredite mit günstigen Konditionen."},
            {"h2": "Anbieterauswahl: Was wirklich zählt",
             "img_kw": "solar technician worker rooftop installation",
             "body": "Nicht den günstigsten wählen – sondern den mit dem besten Service nach der Installation. Prüfe: Wie lange ist das Unternehmen schon aktiv? Gibt es Referenzen in deiner Region? Wie sieht die Garantie auf Ertrag aus?"},
        ],
    },
]

# ── HTML Template ──────────────────────────────────────────────────────────────
def make_html(b: dict) -> str:
    base = "https://automation-cango-app-empire.com"
    slug = b["slug"]
    hero = f"../images/blog-sections/{slug}-hero.jpg"
    og   = f"{base}/images/blog-sections/{slug}-hero.jpg"

    secs = ""
    for i, s in enumerate(b["sections"], 1):
        secs += f"""
  <h2>{s['h2']}</h2>
  <figure class="section-visual">
    <img src="../images/blog-sections/{slug}-section-{i}.jpg"
         alt="{s['h2']}" loading="lazy" width="900" height="506">
    <figcaption>© Wikimedia Commons / CC-Lizenz</figcaption>
  </figure>
  <p>{s['body']}</p>
"""
    related = "\n".join(f'    <a href="{r[1]}">{r[0]}</a>' for r in b.get("related",[]))
    tags    = "\n".join(f'    <span class="tag">{t}</span>' for t in b.get("tags",[]))
    intro   = b["sections"][0]["body"][:200] + "…" if b["sections"] else ""

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{b['title']} | CanGo Empire Blog</title>
<meta name="description" content="{b['sections'][0]['body'][:155] if b['sections'] else ''}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{base}/blogs/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="{b['title']}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{base}/blogs/{slug}.html">
<meta property="article:published_time" content="{b['date']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{b['title']}","image":"{og}","url":"{base}/blogs/{slug}.html","author":{{"@type":"Person","name":"Canberk Umut Kıvılcım"}},"publisher":{{"@type":"Organization","name":"CanGo Empire"}},"datePublished":"{b['date']}","inLanguage":"de","articleSection":"{b['category']}"}}
</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap" media="print" onload="this.media='all'">
<style>
:root{{--orange:#F97316;--navy:#0A0F1E;--navy-light:#1E293B;--text:#E2E8F0;--muted:#94A3B8;--gold:#D4A853;}}
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--navy);color:var(--text);font-family:'Inter',Georgia,sans-serif;font-weight:300;line-height:1.9;padding:2rem 1rem;-webkit-font-smoothing:antialiased;}}
article{{max-width:740px;margin:0 auto;}}
.breadcrumb{{font-size:.75rem;color:var(--muted);margin-bottom:1.5rem;letter-spacing:.05em;}}
.breadcrumb a{{color:var(--muted);text-decoration:none;}}
.breadcrumb a:hover{{color:var(--orange);}}
.breadcrumb span{{margin:0 .4rem;}}
.hero-img{{width:100%;height:auto;aspect-ratio:1200/630;object-fit:cover;border-radius:12px;margin-bottom:2.5rem;display:block;background:var(--navy-light);}}
.meta{{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);font-weight:500;margin-bottom:2rem;}}
h1{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(2rem,5vw,3.4rem);font-weight:600;line-height:1.15;color:#fff;margin-bottom:.5rem;}}
.byline{{font-size:.8rem;color:var(--muted);margin-bottom:2.5rem;padding-bottom:2.5rem;border-bottom:1px solid var(--navy-light);}}
.opening{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.1rem,2.5vw,1.35rem);font-style:italic;color:#CBD5E1;line-height:1.7;margin-bottom:2.5rem;}}
p{{font-size:clamp(.9rem,1.5vw,.97rem);margin-bottom:1.3rem;color:var(--text);}}
h2{{font-family:'Syne',sans-serif;font-size:clamp(.9rem,2vw,1.1rem);font-weight:700;color:var(--orange);margin:3rem 0 1.2rem;letter-spacing:.05em;text-transform:uppercase;}}
/* Section Visual – Bild direkt im Body nach h2 */
.section-visual{{margin:0 0 2rem;border-radius:12px;overflow:hidden;}}
.section-visual img{{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform .4s ease;}}
.section-visual:hover img{{transform:scale(1.02);}}
.section-visual figcaption{{font-size:.62rem;color:var(--muted);text-align:right;padding:.3rem .6rem;background:rgba(10,15,30,.5);}}
.pullquote{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.2rem,3vw,1.5rem);font-style:italic;color:#fff;border-left:3px solid var(--gold);padding:1rem 0 1rem 1.5rem;margin:2.5rem 0;line-height:1.5;}}
.cta-block{{background:linear-gradient(135deg,#F97316,#EA580C);padding:2rem;border-radius:8px;margin-top:3rem;text-align:center;}}
.cta-block strong{{font-family:'Syne',sans-serif;font-size:clamp(1rem,2.5vw,1.15rem);display:block;margin-bottom:.6rem;color:#fff;}}
.cta-block p{{color:rgba(255,255,255,.88);margin-bottom:1.2rem;font-size:.9rem;}}
.cta-btn{{display:inline-block;background:#fff;color:#EA580C;font-family:'Syne',sans-serif;font-weight:700;font-size:.85rem;letter-spacing:.06em;text-transform:uppercase;padding:.75rem 1.8rem;border-radius:4px;text-decoration:none;}}
.tags{{margin-top:2rem;}}
.tag{{display:inline-block;background:var(--navy-light);border:1px solid #1E3A5F;color:var(--muted);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;padding:.3rem .7rem;border-radius:4px;margin:.3rem .2rem 0 0;}}
.related{{margin-top:3rem;padding-top:2rem;border-top:1px solid var(--navy-light);}}
.related-title{{font-family:'Syne',sans-serif;font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:1rem;}}
.related a{{display:block;color:var(--text);text-decoration:none;font-size:.9rem;padding:.5rem 0;border-bottom:1px solid var(--navy-light);}}
.related a:hover{{color:var(--orange);}}
.related a::before{{content:'→ ';color:var(--orange);}}
@media(max-width:600px){{body{{padding:1.5rem 1rem;}}}}
</style>
</head>
<body>
<article>
<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="../index.html">Home</a><span>›</span>
  <a href="../blogs.html">Blog</a><span>›</span>
  {b['category']}
</nav>
<img src="{hero}" alt="{b['title']}" class="hero-img" width="1200" height="630" loading="eager" onerror="this.style.opacity='0'">
<div class="meta">{b['category']} · CanGo Empire · {b['date']}</div>
<h1>{b['title']}</h1>
<div class="byline">Von Canberk Umut Kıvılcım · {b['date']} · {b['read_time']} Lesezeit</div>
<p class="opening">{intro}</p>
{secs}
<blockquote class="pullquote">{b['pullquote']}</blockquote>
<div class="cta-block">
  <strong>Dein System aufbauen lassen</strong>
  <p>CanGo Empire – Automatisierung mit Absicht.</p>
  <a href="../index.html" class="cta-btn">Mehr erfahren</a>
</div>
<div class="tags">{tags}</div>
<nav class="related" aria-label="Ähnliche Artikel">
  <div class="related-title">Ähnliche Artikel</div>
{related}
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
        ftp.cwd(remote_dir);
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {name}", f)
        return True
    except Exception as e:
        print(f"    FTP ✗ {name}: {e}"); return False

def main():
    print("\n🚀 Wikimedia-Bilder (keyword-relevant) part-by-part im Body\n")

    ftp = None
    try:
        ftp = ftplib.FTP(); ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS); ftp.set_pasv(True)
        ftp_mkdir(ftp, f"{REMOTE}/blogs")
        ftp_mkdir(ftp, f"{REMOTE}/images/blog-sections")
        print("✅ FTP OK\n")
    except Exception as e:
        print(f"⚠ FTP: {e}\n")

    for b in BLOGS:
        slug = b["slug"]
        print(f"📄 {slug}")

        # Hero-Bild
        hero_dest = IMG_DIR / f"{slug}-hero.jpg"
        if get_img(b["hero_kw"], hero_dest, 1200, 675):
            print(f"  ✓ hero: {b['hero_kw'][:40]}")

        # Section-Bilder
        for i, sec in enumerate(b["sections"], 1):
            dest = IMG_DIR / f"{slug}-section-{i}.jpg"
            ok = get_img(sec["img_kw"], dest, 900, 506)
            print(f"  {'✓' if ok else '✗'} s{i}: {sec['img_kw'][:45]}")
            time.sleep(0.5)

        # HTML
        html_path = BLOGS_DIR / f"{slug}.html"
        html_path.write_text(make_html(b), encoding="utf-8")
        print(f"  ✓ HTML → {html_path.name}")

        # FTP Upload
        if ftp:
            ftp_put(ftp, html_path, f"{REMOTE}/blogs", f"{slug}.html")
            ftp_put(ftp, hero_dest, f"{REMOTE}/images/blog-sections", hero_dest.name)
            for i in range(1, len(b["sections"])+1):
                f_path = IMG_DIR / f"{slug}-section-{i}.jpg"
                if f_path.exists():
                    ftp_put(ftp, f_path, f"{REMOTE}/images/blog-sections", f_path.name)
            print(f"  ↑ FTP live")
        print()

    if ftp:
        try: ftp.quit()
        except: pass

    print(f"✅ {len(BLOGS)} Blogs fertig — Wikimedia-Bilder part-by-part im Body")
    print(f"🌐 https://automation-cango-app-empire.com/blogs/energie-solar.html\n")

if __name__ == "__main__":
    main()
