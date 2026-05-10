#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Blogs mit Unsplash-Fotos (kein API Key nötig)
Direkte Foto-IDs von Unsplash, thematisch 1:1 passend.
Bilder erscheinen part-by-part nach jeder h2 im Body.
"""
import ftplib, time, urllib.request
from pathlib import Path

ROOT      = Path(__file__).parent.parent
BLOGS_DIR = ROOT / "website" / "blogs"
IMG_DIR   = ROOT / "website" / "images" / "blog-sections"
IMG_DIR.mkdir(parents=True, exist_ok=True)

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"
REMOTE   = "/docker/nginx-proxy-manager-5tiw/www"

# ── Unsplash Direct URL ────────────────────────────────────────────────────────
def unsplash(photo_id: str, w: int = 900, h: int = 506) -> str:
    return f"https://images.unsplash.com/photo-{photo_id}?w={w}&h={h}&q=85&auto=format&fit=crop"

def download(url: str, dest: Path, label: str) -> bool:
    if dest.exists() and dest.stat().st_size > 15_000:
        print(f"  ✓ {label} (cached)")
        return True
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; CanGoEmpire/1.0)"
        })
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 5_000:
            print(f"  ✗ {label} (zu klein: {len(data)} Bytes)")
            return False
        dest.write_bytes(data)
        print(f"  ↓ {label}")
        return True
    except Exception as e:
        print(f"  ✗ {label}: {e}")
        return False

# ── Kuratierte Unsplash Foto-IDs (thematisch präzise) ─────────────────────────
# Format: "slug": {"hero": "id", "s1": "id", "s2": "id", "s3": "id"}
PHOTOS = {
    "finanzen-versicherung": {
        "hero": "1554224155-6726b3ff858f",   # Goldmünzen / Geld
        "s1":   "1450101499163-c8848c66ca85", # Vertrag unterschreiben
        "s2":   "1611974789855-9c2a0a7236a3", # Börse / Charts
        "s3":   "1579621970563-ebec7560ff3e", # Sparschwein / Sparkasse
    },
    "crypto-web3": {
        "hero": "1518546305927-5a555bb7020d", # Bitcoin physische Münze
        "s1":   "1640161704729-cbe966a08476", # Bitcoin/Crypto Trading
        "s2":   "1563986768494-4dee2763ff3f", # Ethereum / Blockchain Tech
        "s3":   "1519389950473-47ba0277781c", # Dezentrales Netzwerk Tech
    },
    "energie-solar": {
        "hero": "1509391366360-2e959784a276", # Solarpanele auf Dach
        "s1":   "1508514177221-188b1cf16e9d", # Photovoltaik Anlage
        "s2":   "1548337138-e87d889cc369",    # Batteriespeicher / Energie
        "s3":   "1593941707882-a5bba14938c7", # Elektroauto laden
    },
    "immobilien": {
        "hero": "1560518883-ce09059eeffa",    # Haus / Immobilie Exterior
        "s1":   "1582268611958-ebfd161ef9cf", # Haus Kaufen Schild
        "s2":   "1586023492125-27b2c045efd7", # Moderne Wohnung Innenraum
        "s3":   "1574362848149-11496d93a7c7", # Renovierung / Sanierung Dämmung
    },
    "ki-tech": {
        "hero": "1677442135703-1787eea5ce01", # KI / Roboter Zukunft
        "s1":   "1620712943543-bcc4688e7485", # Neuronales Netz / KI Konzept
        "s2":   "1600880292203-757bb62b4baf", # Team Meeting / Technologie
        "s3":   "1499951360447-b19be8fe80f5", # Home Office / Laptop
    },
    "trading": {
        "hero": "1611974789855-9c2a0a7236a3", # Börse Charts / Trading
        "s1":   "1611974789855-9c2a0a7236a3", # Roter Kurs / Verlust Chart
        "s2":   "1642790106117-e829e14a795f", # Trading Monitore Candlestick
        "s3":   "1499209974431-9dddcece7f88", # Meditation / Ruhe / Fokus
    },
    "karriere-hr": {
        "hero": "1551836022-d5d88e9218df",    # Business Handshake / Interview
        "s1":   "1516321318423-f06f85e504b3", # Workshop / Training Skills
        "s2":   "1497032628192-86f99bcd76bc", # Home Office Schreibtisch
        "s3":   "1507003211169-0a1dd7228f2d", # Selbstständig / Freelancer
    },
    "coaching-mindset": {
        "hero": "1552664730-d307ca884978",    # Coaching Team / Erfolg
        "s1":   "1589939705384-5185137a7f0f",    # Lernen / Wachstum / Entwicklung
        "s2":   "1484480974693-6ca0a78fb36b", # Planer / Gewohnheit / Journal
        "s3":   "1573497491765-dccce02b29df", # Mentor / Gespräch / Zuhören
    },
    "automationen": {
        "hero": "1518770660439-4636190af475",  # Technologie / Automatisierung
        "s1":   "1519389950473-47ba0277781c",  # Software Interface / Workflow
        "s2":   "1455390582262-044cdead277a",  # Schreiben / Tastatur / Content
        "s3":   "1563986768494-4dee2763ff3f",  # E-Mail Marketing / CRM
    },
    "artikel-bitcoin-institutionen-2026": {
        "hero": "1601597111158-2fceff292cdc",  # Bitcoin Gold Barren / Bank
        "s1":   "1518546305927-5a555bb7020d",  # Bitcoin ETF / Investment
        "s2":   "1541872705-1f73c6400ec9",     # Parlament / Regierung
        "s3":   "1611974789855-9c2a0a7236a3",  # Smartphone Trading App
    },
    "artikel-claude-vs-chatgpt-unternehmen-2026": {
        "hero": "1677442135703-1787eea5ce01",  # KI Chatbot / Computer Screen
        "s1":   "1620712943543-bcc4688e7485",  # KI Dokumentenanalyse Enterprise
        "s2":   "1620712943543-bcc4688e7485",  # Chatbot Interface / Kreativ
        "s3":   "1600880292203-757bb62b4baf",  # Business Strategie Meeting
    },
    "artikel-eigentumswohnung-kaufen-2026": {
        "hero": "1560518883-ce09059eeffa",    # Eigentumswohnung / Schlüssel
        "s1":   "1450101499163-c8848c66ca85", # Notar Vertrag Unterschrift
        "s2":   "1579621970795-87facc2f976d",    # Hypothek Bank Finanzierung
        "s3":   "1574362848149-11496d93a7c7", # Energieeffizienz Sanierung
    },
    "artikel-pkv-vs-gkv-2026": {
        "hero": "1559757148-5c350d0d3c56",    # Arzt Stethoskop Medizin
        "s1":   "1576091160399-112ba8d25d1d", # Privatklinik Arzt Premium
        "s2":   "1450101499163-c8848c66ca85", # Versicherungsvertrag Kleingedrucktes
        "s3":   "1476703993599-0035a21b17a9", # Familie Gesundheit Solidarität
    },
    "artikel-produktivitaet-adhs-systeme": {
        "hero": "1499209974431-9dddcece7f88", # Produktivität Fokus Schreibtisch
        "s1":   "1586473219010-2ffc57b0d282", # Stress Ablenkung Multitasking
        "s2":   "1484480974693-6ca0a78fb36b", # Planer Kalender Organisation
        "s3":   "1677442135703-1787eea5ce01", # KI Assistent Interface ADHS
    },
    "artikel-solaranlage-ratgeber-2026": {
        "hero": "1509391366360-2e959784a276", # Solaranlage Haus Dach
        "s1":   "1508514177221-188b1cf16e9d", # Solar kWh Kosten Strom
        "s2":   "1546435770-a3e426bf472b",     # Förderung Erneuerbare Solar
        "s3":   "1508514177221-188b1cf16e9d", # Solartechniker Dach Montage
    },
}

# ── Blog-Definitionen ──────────────────────────────────────────────────────────
BLOGS = [
    {
        "slug": "finanzen-versicherung",
        "title": "Finanzen & Versicherung 2026: Was wirklich zählt",
        "category": "Finanzen & Versicherung",
        "date": "2026-04-10", "read_time": "6 Min.",
        "pullquote": "Finanzielle Freiheit ist keine Zahl. Sie ist ein Zustand.",
        "tags": ["ETF", "Versicherung", "Finanzen", "Rücklage"],
        "related": [("Immobilien", "immobilien.html"), ("Trading", "trading.html"), ("PKV vs GKV", "artikel-pkv-vs-gkv-2026.html")],
        "sections": [
            {"h2": "Warum Versicherungen neu gedacht werden müssen",
             "body": "Die klassische Vollkasko-Mentalität stirbt langsam aus. Verbraucher wollen verstehen, wofür sie zahlen. Modulare Tarife, digitale Schadensmeldung und KI-gestützte Risikoanalyse verändern die Branche grundlegend. Wer heute abschließt, sollte auf Flexibilität achten – nicht auf maximale Absicherung gegen unwahrscheinliche Szenarien."},
            {"h2": "ETF-Sparplan vs. aktiv gemanagter Fonds",
             "body": "Die Daten sprechen seit Jahren eine klare Sprache: Über 80 % der aktiv gemanagten Fonds schlagen ihren Vergleichsindex nicht. Ein diversifizierter ETF-Sparplan – monatlich, automatisiert, kostengünstig – ist für die meisten Menschen die überlegene Strategie."},
            {"h2": "Notfallgroschen, Rücklage, Vermögen – die drei Schichten",
             "body": "Finanziell resilient zu sein bedeutet nicht reich zu sein. Es bedeutet, strukturiert vorzugehen: drei Monatsgehälter liquid halten, dann Schulden tilgen, dann Vermögen aufbauen. Diese Reihenfolge klingt banal – wird aber von den meisten nicht eingehalten."},
        ],
    },
    {
        "slug": "crypto-web3",
        "title": "Crypto & Web3 2026: Was bleibt, was kommt",
        "category": "Crypto & Web3",
        "date": "2026-04-11", "read_time": "7 Min.",
        "pullquote": "Die beste Technologie verschwindet in der Infrastruktur.",
        "tags": ["Bitcoin", "Ethereum", "Web3", "DeFi"],
        "related": [("Bitcoin Institutionen", "artikel-bitcoin-institutionen-2026.html"), ("Trading", "trading.html"), ("KI & Tech", "ki-tech.html")],
        "sections": [
            {"h2": "Bitcoin als Reserveasset – Realität oder Wunschdenken?",
             "body": "Wenn BlackRock, Fidelity und staatliche Pensionsfonds Bitcoin halten, ist die Diskussion über seine Legitimität beendet. 2026 sehen wir die erste Welle echter Integration in traditionelle Portfolios. Das bedeutet weniger Volatilität, aber auch weniger explosive Renditen. Bitcoin wird Infrastruktur."},
            {"h2": "Ethereum: Wo steht das Ökosystem?",
             "body": "Layer-2-Lösungen wie Arbitrum und Base haben das Skalierungsproblem gelöst. Gas-Gebühren unter einem Cent sind Realität. Was fehlt, ist die Killer-App – die Anwendung, die normale Menschen täglich nutzen."},
            {"h2": "Web3 jenseits des Hypes",
             "body": "Die interessantesten Web3-Projekte 2026 sind die unspektakulären: digitale Identität, dezentrale Datenspeicherung, tokenisierte Real-World-Assets. Sie lösen echte Probleme, ohne dass die Nutzer wissen müssen, dass sie auf einer Blockchain laufen."},
        ],
    },
    {
        "slug": "energie-solar",
        "title": "Energie & Solar 2026: Der Eigenverbrauch-Boom",
        "category": "Energie & Solar",
        "date": "2026-04-09", "read_time": "6 Min.",
        "pullquote": "Energie erzeugen ist Freiheit. Energie sparen ist Strategie.",
        "tags": ["Solar", "Photovoltaik", "Speicher", "Wärmepumpe"],
        "related": [("Solaranlage Ratgeber", "artikel-solaranlage-ratgeber-2026.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Solaranlage 2026 – Rechnet es sich noch?",
             "body": "Ja – mit Einschränkungen. Die Einspeisevergütung ist gesunken, aber die Modulpreise auch. Entscheidend ist jetzt der Eigenverbrauchsanteil: Wer 60–70 % selbst verbraucht (z.B. durch E-Auto oder Wärmepumpe), amortisiert die Anlage in 8–10 Jahren."},
            {"h2": "Batteriespeicher: Wann ist er sinnvoll?",
             "body": "Ein Speicher lohnt sich, wenn dein Eigenverbrauch unter 40 % liegt und du ihn damit auf 70–80 % heben kannst. Die Preise für Heimspeicher sind 2025/2026 deutlich gefallen – 5–10 kWh sind jetzt für 4.000–7.000 € realistisch."},
            {"h2": "Der ganzheitliche Energiehaushalt",
             "body": "Solar + Speicher + Wärmepumpe + E-Auto ist das Quadruple-Play der Energiewende. Wer alle vier Komponenten optimiert und intelligent vernetzt, kann theoretisch nahezu energieautark leben."},
        ],
    },
    {
        "slug": "immobilien",
        "title": "Immobilien 2026: Kaufen, Mieten oder Warten?",
        "category": "Immobilien",
        "date": "2026-04-08", "read_time": "7 Min.",
        "pullquote": "Immobilien sind kein Investment. Sie sind Infrastruktur.",
        "tags": ["Immobilien", "Kaufen", "Mieten", "Zinsen"],
        "related": [("Eigentumswohnung kaufen", "artikel-eigentumswohnung-kaufen-2026.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
        "sections": [
            {"h2": "Wo stehen die Preise wirklich?",
             "body": "In B- und C-Städten sind Preise teilweise 15–25 % unter dem Peak 2022. In Top-7-Städten nur 8–12 %. Das klingt nach Einstiegsgelegenheit – aber die Kaufnebenkosten (7–12 %), gestiegene Zinsen (3,5–4 %) und höhere Anforderungen an die Energieeffizienz ändern die Kalkulation fundamental."},
            {"h2": "Eigennutzung vs. Kapitalanlage",
             "body": "Wer zur Eigennutzung kauft, denkt in Jahrzehnten – und das ist richtig. Wer als Investition kauft, muss mit realistischen Mietrenditen kalkulieren. In vielen Lagen liegt die Bruttomietrendite unter 3 % – nach Verwaltung, Instandhaltung und Finanzierung oft im negativen Bereich."},
            {"h2": "Was 2026 wirklich zählt beim Kauf",
             "body": "Lage, Energieeffizienz und Finanzierungsstruktur. Ein Haus mit Energieklasse G ist 2026 nicht mehr verkäuflich ohne erhebliche Abschläge – und bis 2030 kommen Sanierungspflichten."},
        ],
    },
    {
        "slug": "ki-tech",
        "title": "KI & Tech 2026: Was jetzt wirklich passiert",
        "category": "KI & Technologie",
        "date": "2026-04-07", "read_time": "8 Min.",
        "pullquote": "KI gibt dir nicht mehr Ideen. Sie gibt dir mehr Zeit für die richtigen.",
        "tags": ["KI", "Künstliche Intelligenz", "ChatGPT", "Automatisierung"],
        "related": [("Claude vs ChatGPT", "artikel-claude-vs-chatgpt-unternehmen-2026.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
        "sections": [
            {"h2": "Von ChatGPT zur KI-Infrastruktur",
             "body": "Der Markt hat sich konsolidiert. Anthropic, OpenAI, Google und Meta liefern Foundation Models, auf denen Tausende Anwendungen aufbauen. Wer heute KI als Werkzeug nutzt, hat einen Produktivitätsvorteil. Wer KI in seine Systeme integriert, hat einen strukturellen Vorteil."},
            {"h2": "Was Unternehmen jetzt tun sollten",
             "body": "Nicht 'Was kann KI?' – sondern 'Welche unserer Prozesse kosten am meisten Zeit mit dem geringsten Wert?' Das ist die richtige Frage. Content-Erstellung, Kundenservice, Datenanalyse und interne Dokumentation sind die vier Bereiche mit dem besten ROI bei KI-Integration."},
            {"h2": "KI für Einzelpersonen: Der Hebel ist riesig",
             "body": "Ein Solopreneur mit KI-Tools kann heute die Kapazität eines kleinen Teams erreichen. Content-Pipelines, automatisiertes Outreach, Marktrecherche, Code-Generierung – alles machbar ohne Programmierkenntnisse."},
        ],
    },
    {
        "slug": "trading",
        "title": "Trading 2026: Strategien die funktionieren",
        "category": "Trading",
        "date": "2026-04-06", "read_time": "6 Min.",
        "pullquote": "Ein schlechtes System konsequent angewandt schlägt kein System.",
        "tags": ["Trading", "Börse", "Aktien", "Strategie"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Finanzen", "finanzen-versicherung.html"), ("Bitcoin", "artikel-bitcoin-institutionen-2026.html")],
        "sections": [
            {"h2": "Warum 90 % der Trader verlieren",
             "body": "Nicht weil der Markt gegen sie ist. Weil sie ohne Edge handeln, zu groß positionieren und emotional reagieren. Der Markt transferiert Kapital von Ungeduld zu Geduld. Wer das versteht, beginnt anders zu denken."},
            {"h2": "Systemisches Trading vs. diskretionäres Trading",
             "body": "Systemisches Trading (regelbasiert, automatisiert) schlägt diskretionäres Trading im Durchschnitt – nicht weil Regeln besser sind als Intuition, sondern weil Regeln konsistent sind. Backtesting, klare Entry/Exit-Kriterien und Risk-Management sind keine Optionen. Sie sind das Fundament."},
            {"h2": "Der psychologische Vorteil",
             "body": "Wer sein System kennt und vertraut, handelt entspannter. Entspanntes Trading ist besseres Trading. Die wichtigste Fähigkeit ist nicht die Analyse – es ist die Disziplin, das System auch dann zu folgen, wenn der Markt sich falsch anfühlt."},
        ],
    },
    {
        "slug": "karriere-hr",
        "title": "Karriere & HR 2026: Der neue Arbeitsmarkt",
        "category": "Karriere & HR",
        "date": "2026-04-05", "read_time": "6 Min.",
        "pullquote": "Der wertvollste Mitarbeiter 2026 ist der, der KI orchestriert.",
        "tags": ["Karriere", "HR", "Remote Work", "Fachkräfte"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("KI & Tech", "ki-tech.html")],
        "sections": [
            {"h2": "Welche Skills 2026 wirklich gefragt sind",
             "body": "KI-Kompetenz ist Pflicht, nicht Kür. Prompt Engineering, Datenanalyse, Systemdenken und die Fähigkeit, KI-Tools sinnvoll zu orchestrieren, sind die Schlüsselqualifikationen. Dazu kommen unverrückbar menschliche Skills: Kommunikation, Führung, Kreativität und Empathie."},
            {"h2": "Remote Work: Was wirklich bleibt",
             "body": "Hybrid ist der Standard geworden. Vollständiges Remote ist für viele Unternehmen verhandelt – Ausnahme sind Tech-Unternehmen und internationale Teams. Wer remote arbeiten will, braucht nicht nur die Fähigkeit, sondern auch den Beweis, dass er eigenverantwortlich liefert."},
            {"h2": "Selbstständigkeit und Portfolio-Karriere",
             "body": "Immer mehr Hochqualifizierte verlassen die Festanstellung – nicht aus Not, sondern aus Kalkül. Mehrere Einkommensquellen, Kontrolle über Zeit und Projekte, weniger Organisationspolitik."},
        ],
    },
    {
        "slug": "coaching-mindset",
        "title": "Coaching & Mindset: Die innere Architektur des Erfolgs",
        "category": "Coaching & Mindset",
        "date": "2026-04-04", "read_time": "7 Min.",
        "pullquote": "Du brauchst keine Motivation. Du brauchst ein System.",
        "tags": ["Coaching", "Mindset", "Growth Mindset", "Systeme"],
        "related": [("Karriere & HR", "karriere-hr.html"), ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"), ("Automatisierungen", "automationen.html")],
        "sections": [
            {"h2": "Growth Mindset ist mehr als Buzzword",
             "body": "Carol Dwecks Forschung ist eindeutig: Menschen mit Growth Mindset erzielen langfristig bessere Ergebnisse. Nicht weil sie härter arbeiten, sondern weil sie anders auf Rückschläge reagieren. Fehler sind Feedback, keine Urteile."},
            {"h2": "Systeme schlagen Willenskraft",
             "body": "Willenskraft ist eine endliche Ressource. Wer sich auf sie verlässt, scheitert systematisch an schlechten Tagen. Systeme – Routinen, Umgebungsdesign, Automatisierungen – funktionieren auch wenn die Motivation niedrig ist."},
            {"h2": "Coaching: Wann macht es Sinn?",
             "body": "Coaching ist kein Allheilmittel – aber in den richtigen Momenten der effektivste Hebel. Wann es Sinn macht: bei Übergängen (Job, Beziehung, Projekt), bei wiederkehrenden Mustern und wenn du weißt was zu tun ist, aber es nicht tust."},
        ],
    },
    {
        "slug": "automationen",
        "title": "Automatisierungen 2026: Was du heute noch einrichten kannst",
        "category": "Automatisierungen",
        "date": "2026-04-03", "read_time": "8 Min.",
        "pullquote": "Automatisiere das Wiederholbare. Fokussiere auf das Einzigartige.",
        "tags": ["n8n", "Automatisierung", "Make", "No-Code"],
        "related": [("Maschinen die dienen", "maschinen-die-dienen.html"), ("KI & Tech", "ki-tech.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Die No-Code/Low-Code Revolution",
             "body": "n8n, Make (Integromat), Zapier und neu: KI-Agenten via Anthropic oder OpenAI API. Die Tools sind so weit gereift, dass technisches Know-how kein Engpass mehr ist. Der Engpass ist die richtige Frage: Welcher Prozess kostet mich die meiste Zeit mit dem geringsten Wert?"},
            {"h2": "Content-Automatisierung: Was wirklich funktioniert",
             "body": "Vollautomatisierter Content ohne menschliche Kurierung ist erkennbar – und wird von Google zunehmend abgestraft. Die Zukunft ist semi-automatisiert: KI generiert Drafts, Menschen kurieren und veredeln. Wer diesen Workflow optimiert, publiziert 10x schneller ohne Qualitätsverlust."},
            {"h2": "Lead-Generierung und CRM-Automatisierung",
             "body": "Der größte ROI liegt oft nicht im Content, sondern im Follow-Up. Automatisierte E-Mail-Sequenzen, CRM-Updates durch Webhooks und KI-gestützte Personalisierung – wer das aufgebaut hat, verliert keine Leads mehr durch mangelnde Nachverfolgung."},
        ],
    },
    {
        "slug": "artikel-bitcoin-institutionen-2026",
        "title": "Bitcoin und Institutionen 2026: Eine neue Ära",
        "category": "Crypto & Web3",
        "date": "2026-03-20", "read_time": "7 Min.",
        "pullquote": "Das Geld der Institutionen folgt dem Signal der Weisen.",
        "tags": ["Bitcoin", "ETF", "Institutionelle Investoren"],
        "related": [("Crypto & Web3", "crypto-web3.html"), ("Trading", "trading.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Bitcoin-ETFs: Zahlen und Fakten",
             "body": "Die ersten Spot-ETFs in den USA haben in den ersten 12 Monaten mehr Kapital angezogen als Gold-ETFs in ihrer Anfangsphase. Milliarden Dollar fließen monatlich in strukturierte Bitcoin-Produkte."},
            {"h2": "Staatsreserven: Wer folgt El Salvador?",
             "body": "El Salvador war der Proof of Concept. 2025/2026 haben mehrere weitere Staaten Bitcoin als Teil ihrer Reserven oder Hedging-Strategie diskutiert. Das Signal: Bitcoin wird strategisch gehalten, nicht nur spekulativ getradet."},
            {"h2": "Was das für Retail-Investoren bedeutet",
             "body": "Weniger explosives Upside – aber mehr strukturelle Stabilität. Bitcoin 2026 ist kein x100-Asset mehr für Neueinsteiger. Es ist ein langfristiger Store of Value mit wachsender institutioneller Unterstützung."},
        ],
    },
    {
        "slug": "artikel-claude-vs-chatgpt-unternehmen-2026",
        "title": "Claude vs ChatGPT: Was Unternehmen 2026 wissen müssen",
        "category": "KI & Technologie",
        "date": "2026-03-15", "read_time": "8 Min.",
        "pullquote": "Das beste KI-Tool ist das, das du konsequent nutzt.",
        "tags": ["Claude", "ChatGPT", "KI-Vergleich", "Unternehmen"],
        "related": [("KI & Tech", "ki-tech.html"), ("Automatisierungen", "automationen.html"), ("Maschinen die dienen", "maschinen-die-dienen.html")],
        "sections": [
            {"h2": "Claude: Stärken im Unternehmenskontext",
             "body": "Claude (Anthropic) glänzt bei langen Dokumenten, nuancierter Analyse und Aufgaben, die präzises Verstehen komplexer Kontexte erfordern. Das Constitutional AI-Framework macht es besonders geeignet für sensible Unternehmensdaten."},
            {"h2": "ChatGPT: Wo es überlegt",
             "body": "GPT-4o punktet bei kreativen Aufgaben, Bild-/Sprachverarbeitung und dem DALL-E-Integration. Das Plugin-Ökosystem und die breite Bekanntheit machen es zum Standard-Tool für viele Teams."},
            {"h2": "Die richtige Entscheidung für dein Unternehmen",
             "body": "Für dokumentenintensive, compliance-relevante Aufgaben: Claude. Für kreatives, multimodales Arbeiten mit breitem Tool-Ökosystem: GPT-4o. Für viele Teams lohnt es sich, beide zu nutzen – für unterschiedliche Workflows."},
        ],
    },
    {
        "slug": "artikel-eigentumswohnung-kaufen-2026",
        "title": "Eigentumswohnung kaufen 2026: Der ehrliche Ratgeber",
        "category": "Immobilien",
        "date": "2026-03-10", "read_time": "8 Min.",
        "pullquote": "Ein Haus kaufen ist leicht. Die richtige Entscheidung treffen ist schwer.",
        "tags": ["Eigentumswohnung", "Immobilien", "Kaufen", "Finanzierung"],
        "related": [("Immobilien Überblick", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html"), ("Energie & Solar", "energie-solar.html")],
        "sections": [
            {"h2": "Die echten Kosten eines Wohnungskaufs",
             "body": "Kaufpreis ist nur der Anfang. Grunderwerbsteuer (3,5–6,5 % je Bundesland), Notarkosten (1,5 %), Maklergebühr (bis 3,57 % inklusive MwSt) und Eintrag ins Grundbuch summieren sich auf 7–12 % Nebenkosten."},
            {"h2": "Finanzierung 2026: Was geht, was nicht",
             "body": "Bei 3,5–4 % Zinsen und gesunkenen Preisen hat sich die monatliche Belastung normalisiert. Banken erwarten 20–30 % Eigenkapital plus Nebenkosten aus eigenen Mitteln."},
            {"h2": "Energieeffizienz: Das neue Pflichtkriterium",
             "body": "Ab 2027 kommen EU-weite Sanierungspflichten für die schlechtesten Energieklassen. Eine Wohnung mit Energieklasse G oder F zu kaufen bedeutet absehbare Sanierungskosten von 20.000–60.000 €."},
        ],
    },
    {
        "slug": "artikel-pkv-vs-gkv-2026",
        "title": "PKV vs GKV 2026: Die ehrliche Entscheidungshilfe",
        "category": "Finanzen & Versicherung",
        "date": "2026-03-05", "read_time": "7 Min.",
        "pullquote": "Die beste Versicherung ist die, die du im Alter noch bezahlen kannst.",
        "tags": ["PKV", "GKV", "Krankenversicherung", "Versicherung"],
        "related": [("Finanzen & Versicherung", "finanzen-versicherung.html"), ("Coaching & Mindset", "coaching-mindset.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Wann die PKV wirklich vorteilhaft ist",
             "body": "Für junge, gesunde Gutverdiener ohne Familienplanung rechnet sich PKV oft kurzfristig. Bessere Leistungen, kürzere Wartezeiten, freie Arztwahl. Der Beitrag ist mit 20–35 Jahren deutlich niedriger als der GKV-Beitrag."},
            {"h2": "Was PKV-Vertreter nicht sagen",
             "body": "PKV-Beiträge steigen im Alter erheblich. Ohne Kinder-/Partnermitversicherung zahlt jedes Familienmitglied separat. Wechsel zurück in die GKV ist nach 55 in der Regel nicht möglich."},
            {"h2": "Die GKV-Stärken, die unterschätzt werden",
             "body": "Einkommensunabhängige Mitversicherung von Kindern und Partner. Beitrag bleibt im Rentneralter stabil. Keine Risikoprüfung, keine Leistungsausschlüsse für Vorerkrankungen."},
        ],
    },
    {
        "slug": "artikel-produktivitaet-adhs-systeme",
        "title": "Produktivität mit ADHS: Systeme die wirklich helfen",
        "category": "Coaching & Mindset",
        "date": "2026-02-28", "read_time": "8 Min.",
        "pullquote": "ADHS ist kein Problem zu lösen. Es ist ein System zu bauen.",
        "tags": ["ADHS", "Produktivität", "Neurodiversität", "Systeme"],
        "related": [("Coaching & Mindset", "coaching-mindset.html"), ("Automatisierungen", "automationen.html"), ("Karriere & HR", "karriere-hr.html")],
        "sections": [
            {"h2": "Warum klassische Produktivitätstipps nicht funktionieren",
             "body": "Getting Things Done, Pomodoro-Technik, Tagesplanung – gut für neurotypische Menschen. Für ADHS-Gehirne oft frustrierend. Nicht weil die Person zu schwach ist, sondern weil diese Systeme emotionale Dysregulation und Hyperfokus nicht berücksichtigen."},
            {"h2": "Die drei Säulen produktiver ADHS-Systeme",
             "body": "Erstens: Externe Strukturen (kein Verlass auf innere Motivation). Zweitens: Reduktion der Entscheidungsanzahl. Drittens: Sofortiger Reward-Loops (das ADHS-Gehirn braucht unmittelbare Rückmeldung, nicht verzögerte Belohnung)."},
            {"h2": "KI und ADHS: Überraschend gute Partner",
             "body": "KI-Tools wie Claude oder ChatGPT sind besonders hilfreich für ADHS: Externalisierung von Gedanken, Strukturierung von Aufgaben, sofortiges Feedback. Das 'Braindump'-Prinzip ist ein Game-Changer."},
        ],
    },
    {
        "slug": "artikel-solaranlage-ratgeber-2026",
        "title": "Solaranlage 2026: Der komplette Ratgeber",
        "category": "Energie & Solar",
        "date": "2026-02-20", "read_time": "9 Min.",
        "pullquote": "Die beste Solaranlage ist die, die du nicht mehr bemerkst – weil sie läuft.",
        "tags": ["Solaranlage", "Photovoltaik", "Solar", "Energie"],
        "related": [("Energie & Solar Überblick", "energie-solar.html"), ("Immobilien", "immobilien.html"), ("Finanzen", "finanzen-versicherung.html")],
        "sections": [
            {"h2": "Kosten und Wirtschaftlichkeit 2026",
             "body": "Eine 10-kWp-Anlage kostet installiert zwischen 14.000 und 20.000 €. Die Amortisation berechnet sich primär über den Eigenverbrauch: Bei 0,30 €/kWh Netzstrom und 70 % Eigenverbrauch erreicht man bei guter Planung eine Amortisation in 9–12 Jahren."},
            {"h2": "Förderungen und steuerliche Aspekte",
             "body": "Seit 2023 sind Solaranlagen in Deutschland bis 30 kWp von der Einkommenssteuer befreit. Keine Umsatzsteuer auf Module und Installation. KfW-Kredite mit günstigen Konditionen."},
            {"h2": "Anbieterauswahl: Was wirklich zählt",
             "body": "Nicht den günstigsten wählen – sondern den mit dem besten Service nach der Installation. Prüfe: Wie lange ist das Unternehmen schon aktiv? Gibt es Referenzen in deiner Region? Wie sieht die Garantie auf Ertrag aus?"},
        ],
    },
]

# ── CSS ────────────────────────────────────────────────────────────────────────
SECTION_CSS = """
  .section-visual { margin: 0 0 2rem; border-radius: 12px; overflow: hidden; }
  .section-visual img { width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover; display: block; transition: transform .4s ease; }
  .section-visual:hover img { transform: scale(1.02); }
  .section-visual figcaption { font-size: .62rem; color: var(--muted); text-align: right; padding: .3rem .5rem; }
"""

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
    <figcaption>© Unsplash / CC0-Lizenz</figcaption>
  </figure>
  <p>{s['body']}</p>
"""
    related = "\n".join(f'    <a href="{r[1]}">{r[0]}</a>' for r in b.get("related", []))
    tags    = "\n".join(f'    <span class="tag">{t}</span>' for t in b.get("tags", []))
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
{SECTION_CSS}
.pullquote{{border-left:3px solid var(--orange);padding:1.5rem 1.5rem 1.5rem 2rem;margin:3rem 0;background:var(--navy-light);border-radius:0 12px 12px 0;font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.1rem,2.5vw,1.3rem);font-style:italic;color:var(--gold);line-height:1.6;}}
.cta-block{{background:linear-gradient(135deg,var(--navy-light) 0%,#1a2332 100%);border:1px solid var(--orange);border-radius:16px;padding:2.5rem;margin:4rem 0;text-align:center;}}
.cta-block h3{{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(1.4rem,3vw,1.8rem);color:#fff;margin-bottom:1rem;}}
.cta-block p{{color:var(--muted);margin-bottom:1.5rem;font-size:.9rem;}}
.cta-btn{{display:inline-block;background:var(--orange);color:#fff;padding:.9rem 2.5rem;border-radius:50px;text-decoration:none;font-family:'Syne',sans-serif;font-weight:700;font-size:.9rem;letter-spacing:.05em;transition:transform .2s,box-shadow .2s;}}
.cta-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(249,115,22,.35);}}
.related-articles{{margin-top:4rem;padding-top:2rem;border-top:1px solid var(--navy-light);}}
.related-articles h4{{font-family:'Syne',sans-serif;font-size:.75rem;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:1rem;}}
.related-articles a{{display:block;color:var(--text);text-decoration:none;padding:.6rem 0;border-bottom:1px solid var(--navy-light);font-size:.88rem;transition:color .2s;}}
.related-articles a:hover{{color:var(--orange);}}
.tags{{margin-top:3rem;display:flex;flex-wrap:wrap;gap:.5rem;}}
.tag{{background:var(--navy-light);color:var(--muted);padding:.3rem .8rem;border-radius:20px;font-size:.72rem;letter-spacing:.05em;}}
footer.blog-footer{{margin-top:4rem;padding-top:2rem;border-top:1px solid var(--navy-light);font-size:.75rem;color:var(--muted);text-align:center;}}
footer.blog-footer a{{color:var(--muted);text-decoration:none;}}
footer.blog-footer a:hover{{color:var(--orange);}}
@media(max-width:600px){{body{{padding:1rem .75rem;}}h1{{font-size:1.9rem;}}}}
</style>
</head>
<body>
<article>
  <nav class="breadcrumb">
    <a href="../index.html">CanGo Empire</a><span>›</span>
    <a href="../blogs.html">Blog</a><span>›</span>
    <span>{b['category']}</span>
  </nav>
  <img src="{hero}" alt="{b['title']}" class="hero-img" width="1200" height="630" loading="eager" onerror="this.style.opacity='0.3'">
  <div class="meta">{b['category']} &nbsp;·&nbsp; {b['date']} &nbsp;·&nbsp; {b['read_time']} Lesezeit</div>
  <h1>{b['title']}</h1>
  <p class="byline">Von <strong>Canberk Umut Kıvılcım</strong> · CanGo Empire</p>
  <p class="opening">{intro}</p>
{secs}
  <blockquote class="pullquote">{b['pullquote']}</blockquote>
  <div class="cta-block">
    <h3>Automatisiere dein Business</h3>
    <p>Erfahre, wie CanGo Empire Unternehmen beim Aufbau von KI-gestützten Systemen unterstützt.</p>
    <a href="../index.html#contact" class="cta-btn">Kostenlose Beratung</a>
  </div>
  <div class="tags">
{tags}
  </div>
  <div class="related-articles">
    <h4>Verwandte Artikel</h4>
{related}
  </div>
  <footer class="blog-footer">
    <p>© 2026 <a href="../index.html">CanGo Empire</a> · <a href="../index.html#impressum">Impressum</a> · <a href="../index.html#datenschutz">Datenschutz</a></p>
  </footer>
</article>
</body>
</html>
"""

# ── FTP ────────────────────────────────────────────────────────────────────────
def ftp_ensure_dir(ftp, path):
    parts = path.strip("/").split("/")
    cur = "/"
    for p in parts:
        cur = f"{cur}{p}/"
        try:
            ftp.cwd(cur)
        except ftplib.error_perm:
            try:
                ftp.mkd(cur)
                ftp.cwd(cur)
            except:
                pass

def ftp_upload(ftp, local, remote):
    try:
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {remote}", f)
        return True
    except Exception as e:
        print(f"  ✗ FTP: {e}")
        return False

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print("\n🚀 CanGo Empire – Unsplash Fotos (thematisch präzise) part-by-part\n")

    # Erstmal alle Bilder lokal löschen (frischer Download)
    for f in IMG_DIR.glob("*.jpg"):
        f.unlink()
    print("  🗑  Alte Bilder gelöscht\n")

    # FTP verbinden
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        print("✅ FTP OK\n")
    except Exception as e:
        print(f"❌ FTP: {e}")
        return

    remote_blogs = f"{REMOTE}/blogs"
    remote_imgs  = f"{REMOTE}/images/blog-sections"
    ftp_ensure_dir(ftp, remote_imgs)

    total_ok = 0
    total_fail = 0

    for b in BLOGS:
        slug = b["slug"]
        ids = PHOTOS.get(slug, {})
        print(f"📄 {slug}")

        # Hero
        hero_id = ids.get("hero", "1554224155-6726b3ff858f")
        hero_dest = IMG_DIR / f"{slug}-hero.jpg"
        ok = download(unsplash(hero_id, 1200, 630), hero_dest, "hero")
        if not ok:
            total_fail += 1
        time.sleep(0.2)

        # Sections
        for i, s in enumerate(b["sections"], 1):
            sid = ids.get(f"s{i}", "1554224155-6726b3ff858f")
            dest = IMG_DIR / f"{slug}-section-{i}.jpg"
            ok = download(unsplash(sid, 900, 506), dest, f"s{i}: {s['h2'][:40]}")
            if ok:
                total_ok += 1
            else:
                total_fail += 1
            time.sleep(0.2)

        # HTML
        html_path = BLOGS_DIR / f"{slug}.html"
        html_path.write_text(make_html(b), encoding="utf-8")
        print(f"  ✓ HTML geschrieben")

        # FTP Upload
        ftp_ensure_dir(ftp, remote_blogs)
        ftp.cwd(remote_blogs)
        ftp_upload(ftp, html_path, f"{slug}.html")

        ftp_ensure_dir(ftp, remote_imgs)
        ftp.cwd(remote_imgs)
        for fname in [f"{slug}-hero.jpg"] + [f"{slug}-section-{i}.jpg" for i in range(1, len(b["sections"]) + 1)]:
            lf = IMG_DIR / fname
            if lf.exists() and lf.stat().st_size > 5000:
                ftp_upload(ftp, lf, fname)

        print(f"  ↑ FTP live\n")

    ftp.quit()
    print(f"✅ Fertig – {total_ok} Bilder · {total_fail} Fehler")
    print("🌐 https://automation-cango-app-empire.com/blogs/energie-solar.html")

if __name__ == "__main__":
    main()
