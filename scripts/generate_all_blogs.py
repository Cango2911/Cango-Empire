#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Alle Blog-Artikel generieren + Bilder + Upload
Erstellt alle fehlenden Blog-Seiten und lädt sie auf Hostinger hoch.
"""
import ftplib, re, time, urllib.request
from pathlib import Path

from cango_env import ftp_credentials

ROOT       = Path(__file__).parent.parent
BLOGS_DIR  = ROOT / "website" / "blogs"
IMG_DIR    = ROOT / "website" / "images" / "blog-real"
BLOGS_HTML = ROOT / "website" / "blogs.html"

BLOGS_DIR.mkdir(parents=True, exist_ok=True)
IMG_DIR.mkdir(parents=True, exist_ok=True)

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()
REMOTE     = "/docker/nginx-proxy-manager-5tiw/www"

# ── Blog-Definitionen ──────────────────────────────────────────────────────────
BLOGS = [
    {
        "slug": "finanzen-versicherung",
        "title": "Finanzen & Versicherung 2026: Was wirklich zählt",
        "meta_desc": "Die wichtigsten Entscheidungen rund um Finanzen und Versicherung 2026 – strukturiert, klar und ohne Fachjargon erklärt.",
        "category": "Finanzen & Versicherung",
        "date": "2026-04-10",
        "read_time": "6 Min.",
        "hero_id": 210,
        "s1_id": 172, "s2_id": 534, "s3_id": 260,
        "opening": "Wer seine Finanzen nicht aktiv gestaltet, lässt sie passiv schrumpfen. Inflation, Zinswende und neue Versicherungsmodelle – 2026 ist kein Jahr für Abwarten.",
        "sections": [
            ("Warum Versicherungen neu gedacht werden müssen",
             "Die klassische Vollkasko-Mentalität stirbt langsam aus. Verbraucher wollen verstehen, wofür sie zahlen. Modulare Tarife, digitale Schadensmeldung und KI-gestützte Risikoanalyse verändern die Branche grundlegend. Wer heute abschließt, sollte auf Flexibilität achten – nicht auf maximale Absicherung gegen unwahrscheinliche Szenarien."),
            ("ETF-Sparplan vs. aktiv gemanagter Fonds",
             "Die Daten sprechen seit Jahren eine klare Sprache: Über 80 % der aktiv gemanagten Fonds schlagen ihren Vergleichsindex nicht. Ein diversifizierter ETF-Sparplan – monatlich, automatisiert, kostengünstig – ist für die meisten Menschen die überlegene Strategie. Der CanGo Empire Ansatz: erst Grundabsicherung aufbauen, dann investieren, dann optimieren."),
            ("Notfallgroschen, Rücklage, Vermögen – die drei Schichten",
             "Finanziell resilient zu sein bedeutet nicht reich zu sein. Es bedeutet, strukturiert vorzugehen: drei Monatsgehälter liquid halten, dann Schulden tilgen, dann Vermögen aufbauen. Diese Reihenfolge klingt banal – wird aber von den meisten nicht eingehalten. Das ist der eigentliche Hebel."),
        ],
        "pullquote": "Finanzielle Freiheit ist keine Zahl. Sie ist ein Zustand.",
        "cta_text": "Finanzstrukturen automatisieren lassen",
        "tags": ["ETF", "Versicherung", "Finanzen", "Rücklage", "CanGo Empire"],
        "related": [
            ("Immobilien kaufen 2026", "immobilien.html"),
            ("Trading Grundlagen", "trading.html"),
            ("PKV vs GKV", "artikel-pkv-vs-gkv-2026.html"),
        ],
    },
    {
        "slug": "crypto-web3",
        "title": "Crypto & Web3 2026: Was bleibt, was kommt",
        "meta_desc": "Eine nüchterne Analyse des Krypto-Marktes 2026 – Bitcoin, Ethereum, DeFi und welche Projekte echten Wert schaffen.",
        "category": "Crypto & Web3",
        "date": "2026-04-11",
        "read_time": "7 Min.",
        "hero_id": 730,
        "s1_id": 180, "s2_id": 325, "s3_id": 442,
        "opening": "Nach dem Hype-Zyklus 2021 und dem Crash 2022 ist der Markt 2026 erwachsener geworden. Institutionelle Investoren sind da. Die Frage ist nicht mehr ob – sondern wie.",
        "sections": [
            ("Bitcoin als Reserveasset – Realität oder Wunschdenken?",
             "Wenn BlackRock, Fidelity und staatliche Pensionsfonds Bitcoin halten, ist die Diskussion über seine Legitimität beendet. 2026 sehen wir die erste Welle echter Integration in traditionelle Portfolios. Das bedeutet weniger Volatilität, aber auch weniger explosive Renditen. Bitcoin wird Infrastruktur."),
            ("Ethereum: Wo steht das Ökosystem?",
             "Layer-2-Lösungen wie Arbitrum und Base haben das Skalierungsproblem gelöst. Gas-Gebühren unter einem Cent sind Realität. Was fehlt, ist die Killer-App – die Anwendung, die normale Menschen täglich nutzen. DeFi, NFTs und Gaming haben Pionierarbeit geleistet, aber der breite Durchbruch steht noch aus."),
            ("Web3 jenseits des Hypes",
             "Die interessantesten Web3-Projekte 2026 sind die unspektakulären: digitale Identität, dezentrale Datenspeicherung, tokenisierte Real-World-Assets. Sie lösen echte Probleme, ohne dass die Nutzer wissen müssen, dass sie auf einer Blockchain laufen. Das ist die Zukunft – unsichtbar, aber wirksam."),
        ],
        "pullquote": "Die beste Technologie verschwindet in der Infrastruktur.",
        "cta_text": "Crypto-Systeme automatisieren",
        "tags": ["Bitcoin", "Ethereum", "Web3", "DeFi", "Blockchain"],
        "related": [
            ("Bitcoin Institutionen 2026", "artikel-bitcoin-institutionen-2026.html"),
            ("Trading Grundlagen", "trading.html"),
            ("KI & Tech", "ki-tech.html"),
        ],
    },
    {
        "slug": "energie-solar",
        "title": "Energie & Solar 2026: Der Eigenverbrauch-Boom",
        "meta_desc": "Solaranlage, Batteriespeicher, Wärmepumpe – was 2026 wirklich lohnt und wie du deine Energiekosten dauerhaft senkst.",
        "category": "Energie & Solar",
        "date": "2026-04-09",
        "read_time": "6 Min.",
        "hero_id": 459,
        "s1_id": 974, "s2_id": 129, "s3_id": 1,
        "opening": "Wer 2026 noch auf volatile Strompreise wartet, wartet vergeblich. Wer dagegen Eigenverbrauch optimiert, zahlt langfristig weniger – und ist unabhängiger.",
        "sections": [
            ("Solaranlage 2026 – Rechnet es sich noch?",
             "Ja – mit Einschränkungen. Die Einspeisevergütung ist gesunken, aber die Modulpreise auch. Entscheidend ist jetzt der Eigenverbrauchsanteil: Wer 60–70 % selbst verbraucht (z.B. durch E-Auto oder Wärmepumpe), amortisiert die Anlage in 8–10 Jahren. Ohne Speicher und ohne große Lasten dauert es länger."),
            ("Batteriespeicher: Wann ist er sinnvoll?",
             "Ein Speicher lohnt sich, wenn dein Eigenverbrauch unter 40 % liegt und du ihn damit auf 70–80 % heben kannst. Die Preise für Heimspeicher sind 2025/2026 deutlich gefallen – 5–10 kWh sind jetzt für 4.000–7.000 € realistisch. Kombiniert mit dynamischen Stromtarifen ist das ein echter Hebel."),
            ("Der ganzheitliche Energiehaushalt",
             "Solar + Speicher + Wärmepumpe + E-Auto ist das Quadruple-Play der Energiewende. Wer alle vier Komponenten optimiert und intelligent vernetzt, kann theoretisch nahezu energieautark leben. Das erfordert Planung, aber keine Kompromisse beim Komfort."),
        ],
        "pullquote": "Energie erzeugen ist Freiheit. Energie sparen ist Strategie.",
        "cta_text": "Energie-Monitoring automatisieren",
        "tags": ["Solar", "Photovoltaik", "Speicher", "Wärmepumpe", "Energiewende"],
        "related": [
            ("Solaranlage Ratgeber 2026", "artikel-solaranlage-ratgeber-2026.html"),
            ("Immobilien kaufen", "immobilien.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
        ],
    },
    {
        "slug": "immobilien",
        "title": "Immobilien 2026: Kaufen, Mieten oder Warten?",
        "meta_desc": "Der Immobilienmarkt 2026 nach Zinswende und Preiskorrektur – wann lohnt der Kauf und was Käufer wissen müssen.",
        "category": "Immobilien",
        "date": "2026-04-08",
        "read_time": "7 Min.",
        "hero_id": 164,
        "s1_id": 547, "s2_id": 129, "s3_id": 1080,
        "opening": "Nach drei Jahren Zinsdruck und Preiskorrektur normalisiert sich der Markt. 2026 ist kein Schnäppchenmarkt – aber für Käufer mit klarem Plan eine Chance.",
        "sections": [
            ("Wo stehen die Preise wirklich?",
             "In B- und C-Städten sind Preise teilweise 15–25 % unter dem Peak 2022. In Top-7-Städten nur 8–12 %. Das klingt nach Einstiegsgelegenheit – aber die Kaufnebenkosten (7–12 %), gestiegene Zinsen (3,5–4 %) und höhere Anforderungen an die Energieeffizienz ändern die Kalkulation fundamental."),
            ("Eigennutzung vs. Kapitalanlage",
             "Wer zur Eigennutzung kauft, denkt in Jahrzehnten – und das ist richtig. Wer als Investition kauft, muss mit realistischen Mietrenditen kalkulieren. In vielen Lagen liegt die Bruttomietrendite unter 3 % – nach Verwaltung, Instandhaltung und Finanzierung oft im negativen Bereich. Die Zeiten des 'Betongold kaufen und warten' sind vorbei."),
            ("Was 2026 wirklich zählt beim Kauf",
             "Lage, Energieeffizienz und Finanzierungsstruktur. Ein Haus mit Energieklasse G ist 2026 nicht mehr verkäuflich ohne erhebliche Abschläge – und bis 2030 kommen Sanierungspflichten. Käufer sollten EPC, Heizungsart und Dämmstand vor dem Kauf prüfen wie früher nur den Grundriss."),
        ],
        "pullquote": "Immobilien sind kein Investment. Sie sind Infrastruktur.",
        "cta_text": "Immobilien-Recherche automatisieren",
        "tags": ["Immobilien", "Kaufen", "Mieten", "Zinsen", "Energieeffizienz"],
        "related": [
            ("Eigentumswohnung kaufen 2026", "artikel-eigentumswohnung-kaufen-2026.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
            ("Energie & Solar", "energie-solar.html"),
        ],
    },
    {
        "slug": "ki-tech",
        "title": "KI & Tech 2026: Was jetzt wirklich passiert",
        "meta_desc": "KI ist kein Hype mehr – sie ist Infrastruktur. Was 2026 für Unternehmen, Freelancer und Privatpersonen bedeutet.",
        "category": "KI & Technologie",
        "date": "2026-04-07",
        "read_time": "8 Min.",
        "hero_id": 442,
        "s1_id": 325, "s2_id": 180, "s3_id": 730,
        "opening": "2023 war der Hype. 2024 die Ernüchterung. 2025 die Produktivisierung. 2026 ist das Jahr, in dem KI stillschweigend in alles einzieht.",
        "sections": [
            ("Von ChatGPT zur KI-Infrastruktur",
             "Der Markt hat sich konsolidiert. Anthropic, OpenAI, Google und Meta liefern Foundation Models, auf denen Tausende Anwendungen aufbauen. Wer heute KI als Werkzeug nutzt, hat einen Produktivitätsvorteil. Wer KI in seine Systeme integriert, hat einen strukturellen Vorteil."),
            ("Was Unternehmen jetzt tun sollten",
             "Nicht 'Was kann KI?' – sondern 'Welche unserer Prozesse kosten am meisten Zeit mit dem geringsten Wert?' Das ist die richtige Frage. Content-Erstellung, Kundenservice, Datenanalyse und interne Dokumentation sind die vier Bereiche mit dem besten ROI bei KI-Integration."),
            ("KI für Einzelpersonen: Der Hebel ist riesig",
             "Ein Solopreneur mit KI-Tools kann heute die Kapazität eines kleinen Teams erreichen. Content-Pipelines, automatisiertes Outreach, Marktrecherche, Code-Generierung – alles machbar ohne Programmierkenntnisse. Der Engpass ist nicht mehr das Werkzeug, sondern die Strategie."),
        ],
        "pullquote": "KI gibt dir nicht mehr Ideen. Sie gibt dir mehr Zeit für die richtigen.",
        "cta_text": "KI-Automatisierung für dein Business",
        "tags": ["KI", "Künstliche Intelligenz", "ChatGPT", "Claude", "Automatisierung"],
        "related": [
            ("Claude vs ChatGPT", "artikel-claude-vs-chatgpt-unternehmen-2026.html"),
            ("Automatisierungen", "automationen.html"),
            ("Maschinen die dienen", "maschinen-die-dienen.html"),
        ],
    },
    {
        "slug": "trading",
        "title": "Trading 2026: Strategien die funktionieren",
        "meta_desc": "Welche Trading-Strategien 2026 noch funktionieren, was Anfänger wissen müssen und wie du emotionale Entscheidungen vermeidest.",
        "category": "Trading",
        "date": "2026-04-06",
        "read_time": "6 Min.",
        "hero_id": 534,
        "s1_id": 172, "s2_id": 210, "s3_id": 96,
        "opening": "Trading ist kein Glücksspiel – aber es fühlt sich so an, wenn man ohne System handelt. Das System ist der Unterschied zwischen Trader und Spieler.",
        "sections": [
            ("Warum 90 % der Trader verlieren",
             "Nicht weil der Markt gegen sie ist. Weil sie ohne Edge handeln, zu groß positionieren und emotional reagieren. Der Markt transferiert Kapital von Ungeduld zu Geduld. Wer das versteht, beginnt anders zu denken."),
            ("Systemisches Trading vs. diskretionäres Trading",
             "Systemisches Trading (regelbasiert, automatisiert) schlägt diskretionäres Trading im Durchschnitt – nicht weil Regeln besser sind als Intuition, sondern weil Regeln konsistent sind. Backtesting, klare Entry/Exit-Kriterien und Risk-Management sind keine Optionen. Sie sind das Fundament."),
            ("Der psychologische Vorteil",
             "Wer sein System kennt und vertraut, handelt entspannter. Entspanntes Trading ist besseres Trading. Die wichtigste Fähigkeit ist nicht die Analyse – es ist die Disziplin, das System auch dann zu folgen, wenn der Markt sich falsch anfühlt."),
        ],
        "pullquote": "Ein schlechtes System konsequent angewandt schlägt kein System.",
        "cta_text": "Trading-Monitoring automatisieren",
        "tags": ["Trading", "Börse", "Aktien", "Strategie", "Risikomanagement"],
        "related": [
            ("Crypto & Web3", "crypto-web3.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
            ("Bitcoin Institutionen", "artikel-bitcoin-institutionen-2026.html"),
        ],
    },
    {
        "slug": "karriere-hr",
        "title": "Karriere & HR 2026: Der neue Arbeitsmarkt",
        "meta_desc": "Fachkräftemangel, Remote Work und KI-Disruption – was den Arbeitsmarkt 2026 prägt und wie du dich positionierst.",
        "category": "Karriere & HR",
        "date": "2026-04-05",
        "read_time": "6 Min.",
        "hero_id": 375,
        "s1_id": 210, "s2_id": 260, "s3_id": 399,
        "opening": "Der Arbeitsmarkt 2026 ist gespalten: Riesige Nachfrage nach spezifischen Skills – und gleichzeitig KI-Verdrängung in bestimmten Bereichen. Wer weiß wo er steht, kann navigieren.",
        "sections": [
            ("Welche Skills 2026 wirklich gefragt sind",
             "KI-Kompetenz ist Pflicht, nicht Kür. Prompt Engineering, Datenanalyse, Systemdenken und die Fähigkeit, KI-Tools sinnvoll zu orchestrieren, sind die Schlüsselqualifikationen. Dazu kommen unverrückbar menschliche Skills: Kommunikation, Führung, Kreativität und Empathie."),
            ("Remote Work: Was wirklich bleibt",
             "Hybrid ist der Standard geworden. Vollständiges Remote ist für viele Unternehmen verhandelt – Ausnahme sind Tech-Unternehmen und internationale Teams. Wer remote arbeiten will, braucht nicht nur die Fähigkeit, sondern auch den Beweis, dass er eigenverantwortlich liefert."),
            ("Selbstständigkeit und Portfolio-Karriere",
             "Immer mehr Hochqualifizierte verlassen die Festanstellung – nicht aus Not, sondern aus Kalkül. Mehrere Einkommensquellen, Kontrolle über Zeit und Projekte, weniger Organisationspolitik. Das ist der eigentliche Trend hinter 'The Great Resignation'."),
        ],
        "pullquote": "Der wertvollste Mitarbeiter 2026 ist der, der KI orchestriert – nicht der, der von ihr orchestriert wird.",
        "cta_text": "HR-Prozesse mit KI optimieren",
        "tags": ["Karriere", "HR", "Remote Work", "Fachkräfte", "KI"],
        "related": [
            ("Coaching & Mindset", "coaching-mindset.html"),
            ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"),
            ("KI & Tech", "ki-tech.html"),
        ],
    },
    {
        "slug": "coaching-mindset",
        "title": "Coaching & Mindset: Die innere Architektur des Erfolgs",
        "meta_desc": "Warum Mindset kein Buzzword ist, sondern die Grundlage – und welche konkreten Frameworks wirklich helfen.",
        "category": "Coaching & Mindset",
        "date": "2026-04-04",
        "read_time": "7 Min.",
        "hero_id": 1090,
        "s1_id": 399, "s2_id": 260, "s3_id": 1024,
        "opening": "Mindset ist das meistbenutzte und am wenigsten verstandene Wort in der Selbstoptimierungsbranche. Was es wirklich bedeutet: Wie du auf Herausforderungen reagierst, wenn niemand zuschaut.",
        "sections": [
            ("Growth Mindset ist mehr als Buzzword",
             "Carol Dwecks Forschung ist eindeutig: Menschen mit Growth Mindset – der Überzeugung, dass Fähigkeiten entwickelbar sind – erzielen langfristig bessere Ergebnisse. Nicht weil sie härter arbeiten, sondern weil sie anders auf Rückschläge reagieren. Fehler sind Feedback, keine Urteile."),
            ("Systeme schlagen Willenskraft",
             "Willenskraft ist eine endliche Ressource. Wer sich auf sie verlässt, scheitert systematisch an schlechten Tagen. Systeme – Routinen, Umgebungsdesign, Automatisierungen – funktionieren auch wenn die Motivation niedrig ist. Das ist der Kern des CanGo Empire Ansatzes: Baue Systeme, die dich auch dann voranbringen, wenn du es nicht aktiv tust."),
            ("Coaching: Wann macht es Sinn?",
             "Coaching ist kein Allheilmittel – aber in den richtigen Momenten der effektivste Hebel. Wann es Sinn macht: bei Übergängen (Job, Beziehung, Projekt), bei wiederkehrenden Mustern und wenn du weißt was zu tun ist, aber es nicht tust. Ein guter Coach stellt die richtigen Fragen, gibt keine Antworten."),
        ],
        "pullquote": "Du brauchst keine Motivation. Du brauchst ein System, das auch ohne sie funktioniert.",
        "cta_text": "Dein persönliches System aufbauen",
        "tags": ["Coaching", "Mindset", "Growth Mindset", "Systeme", "Persönlichkeitsentwicklung"],
        "related": [
            ("Karriere & HR", "karriere-hr.html"),
            ("Produktivität & ADHS", "artikel-produktivitaet-adhs-systeme.html"),
            ("Automatisierungen", "automationen.html"),
        ],
    },
    {
        "slug": "automationen",
        "title": "Automatisierungen 2026: Was du heute noch einrichten kannst",
        "meta_desc": "Welche Automatisierungen 2026 den größten Impact haben – von n8n über Make bis zu KI-Agenten, praxisnah erklärt.",
        "category": "Automatisierungen",
        "date": "2026-04-03",
        "read_time": "8 Min.",
        "hero_id": 1036,
        "s1_id": 442, "s2_id": 325, "s3_id": 96,
        "opening": "Automatisierung ist keine Frage der Unternehmensgröße mehr. Mit n8n, Make und KI-Agenten kann jeder Solopreneur heute die Kapazität eines kleinen Teams abbilden.",
        "sections": [
            ("Die No-Code/Low-Code Revolution",
             "n8n, Make (Integromat), Zapier und neu: KI-Agenten via Anthropic oder OpenAI API. Die Tools sind so weit gereift, dass technisches Know-how kein Engpass mehr ist. Der Engpass ist die richtige Frage: Welcher Prozess kostet mich die meiste Zeit mit dem geringsten Wert?"),
            ("Content-Automatisierung: Was wirklich funktioniert",
             "Vollautomatisierter Content ohne menschliche Kurierung ist erkennbar – und wird von Google zunehmend abgestraft. Die Zukunft ist semi-automatisiert: KI generiert Drafts, Menschen kurieren und veredeln. Wer diesen Workflow optimiert, publiziert 10x schneller ohne Qualitätsverlust."),
            ("Lead-Generierung und CRM-Automatisierung",
             "Der größte ROI liegt oft nicht im Content, sondern im Follow-Up. Automatisierte E-Mail-Sequenzen, CRM-Updates durch Webhooks und KI-gestützte Personalisierung – wer das aufgebaut hat, verliert keine Leads mehr durch mangelnde Nachverfolgung."),
        ],
        "pullquote": "Automatisiere das Wiederholbare. Fokussiere auf das Einzigartige.",
        "cta_text": "Deine erste Automatisierung aufsetzen",
        "tags": ["n8n", "Automatisierung", "Make", "No-Code", "KI-Agenten"],
        "related": [
            ("Maschinen die dienen", "maschinen-die-dienen.html"),
            ("KI & Tech", "ki-tech.html"),
            ("Karriere & HR", "karriere-hr.html"),
        ],
    },
    {
        "slug": "artikel-bitcoin-institutionen-2026",
        "title": "Bitcoin und Institutionen 2026: Eine neue Ära",
        "meta_desc": "Wie institutionelle Investoren Bitcoin 2026 transformieren – ETFs, Staatsreserven und was das für den Markt bedeutet.",
        "category": "Crypto & Web3",
        "date": "2026-03-20",
        "read_time": "7 Min.",
        "hero_id": 730,
        "s1_id": 325, "s2_id": 180, "s3_id": 534,
        "opening": "Als BlackRock den ersten Bitcoin-ETF auflegte, war das kein Meilenstein – es war ein Paradigmenwechsel. 2026 ist Bitcoin keine Spekulation mehr. Es ist eine Asset-Klasse.",
        "sections": [
            ("Bitcoin-ETFs: Zahlen und Fakten",
             "Die ersten Spot-ETFs in den USA haben in den ersten 12 Monaten mehr Kapital angezogen als Gold-ETFs in ihrer Anfangsphase. Milliarden Dollar fließen monatlich in strukturierte Bitcoin-Produkte. Das dämpft die Volatilität – und verändert die Marktdynamik fundamental."),
            ("Staatsreserven: Wer folgt El Salvador?",
             "El Salvador war der Proof of Concept. 2025/2026 haben mehrere weitere Staaten Bitcoin als Teil ihrer Reserven oder Hedging-Strategie diskutiert. Das Signal: Bitcoin wird strategisch gehalten, nicht nur spekulativ getradet."),
            ("Was das für Retail-Investoren bedeutet",
             "Weniger explosives Upside – aber mehr strukturelle Stabilität. Bitcoin 2026 ist kein x100-Asset mehr für Neueinsteiger. Es ist ein langfristiger Store of Value mit wachsender institutioneller Unterstützung. Wer das versteht, positioniert sich anders."),
        ],
        "pullquote": "Das Geld der Institutionen folgt dem Signal der Weisen.",
        "cta_text": "Crypto-Portfolio analysieren lassen",
        "tags": ["Bitcoin", "ETF", "Institutionelle Investoren", "Blockchain", "Krypto"],
        "related": [
            ("Crypto & Web3", "crypto-web3.html"),
            ("Trading", "trading.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
        ],
    },
    {
        "slug": "artikel-claude-vs-chatgpt-unternehmen-2026",
        "title": "Claude vs ChatGPT: Was Unternehmen 2026 wissen müssen",
        "meta_desc": "Ein direkter Vergleich von Claude und ChatGPT für den Unternehmenseinsatz 2026 – Stärken, Schwächen und konkrete Use Cases.",
        "category": "KI & Technologie",
        "date": "2026-03-15",
        "read_time": "8 Min.",
        "hero_id": 442,
        "s1_id": 325, "s2_id": 96, "s3_id": 573,
        "opening": "Die Frage ist nicht mehr 'Nutze ich KI?' Die Frage ist 'Welches Modell für welchen Zweck?' Claude und ChatGPT sind unterschiedliche Werkzeuge – mit unterschiedlichen Stärken.",
        "sections": [
            ("Claude: Stärken im Unternehmenskontext",
             "Claude (Anthropic) glänzt bei langen Dokumenten, nuancierter Analyse und Aufgaben, die präzises Verstehen komplexer Kontexte erfordern. Das Constitutional AI-Framework macht es besonders geeignet für sensible Unternehmensdaten. Der 200k-Token-Kontext ermöglicht das Verarbeiten ganzer Vertragswerke in einem Schritt."),
            ("ChatGPT: Wo es überlegt",
             "GPT-4o punktet bei kreativen Aufgaben, Bild-/Sprachverarbeitung und dem DALL-E-Integration. Das Plugin-Ökosystem und die breite Bekanntheit machen es zum Standard-Tool für viele Teams. Code Interpreter (Advanced Data Analysis) ist ein echter Unterschied bei Datenauswertungen."),
            ("Die richtige Entscheidung für dein Unternehmen",
             "Für dokumentenintensive, compliance-relevante Aufgaben: Claude. Für kreatives, multimodales Arbeiten mit breitem Tool-Ökosystem: GPT-4o. Für viele Teams lohnt es sich, beide zu nutzen – für unterschiedliche Workflows. Die Kosten sind 2026 für beide Modelle deutlich gesunken."),
        ],
        "pullquote": "Das beste KI-Tool ist das, das du konsequent nutzt.",
        "cta_text": "KI-Integration für dein Business",
        "tags": ["Claude", "ChatGPT", "KI-Vergleich", "Unternehmen", "Anthropic"],
        "related": [
            ("KI & Tech", "ki-tech.html"),
            ("Automatisierungen", "automationen.html"),
            ("Maschinen die dienen", "maschinen-die-dienen.html"),
        ],
    },
    {
        "slug": "artikel-eigentumswohnung-kaufen-2026",
        "title": "Eigentumswohnung kaufen 2026: Der ehrliche Ratgeber",
        "meta_desc": "Was Käufer einer Eigentumswohnung 2026 wirklich wissen müssen – Finanzierung, Nebenkosten, Energieeffizienz und häufige Fehler.",
        "category": "Immobilien",
        "date": "2026-03-10",
        "read_time": "8 Min.",
        "hero_id": 164,
        "s1_id": 547, "s2_id": 129, "s3_id": 1080,
        "opening": "Der Traum von der eigenen Wohnung ist unverändert stark. Die Realität des Kaufprozesses ist komplexer geworden. Wer vorbereitet reingeht, trifft bessere Entscheidungen.",
        "sections": [
            ("Die echten Kosten eines Wohnungskaufs",
             "Kaufpreis ist nur der Anfang. Grunderwerbsteuer (3,5–6,5 % je Bundesland), Notarkosten (1,5 %), Maklergebühr (bis 3,57 % inklusive MwSt) und Eintrag ins Grundbuch summieren sich auf 7–12 % Nebenkosten. Bei einer 400.000 € Wohnung bedeutet das bis zu 48.000 € zusätzlich – die du liquide haben musst."),
            ("Finanzierung 2026: Was geht, was nicht",
             "Bei 3,5–4 % Zinsen und gesunkenen Preisen hat sich die monatliche Belastung normalisiert. Banken erwarten 20–30 % Eigenkapital plus Nebenkosten aus eigenen Mitteln. Wer das nicht hat, sollte noch 2–3 Jahre sparen – der Markt läuft nicht weg."),
            ("Energieeffizienz: Das neue Pflichtkriterium",
             "Ab 2027 kommen EU-weite Sanierungspflichten für die schlechtesten Energieklassen. Eine Wohnung mit Energieklasse G oder F zu kaufen bedeutet absehbare Sanierungskosten von 20.000–60.000 €. Prüfe vor dem Kauf: Energieausweis, Heizungsart und Dämmzustand des Gebäudes."),
        ],
        "pullquote": "Ein Haus kaufen ist leicht. Die richtige Entscheidung treffen ist schwer.",
        "cta_text": "Immobiliensuche automatisieren",
        "tags": ["Eigentumswohnung", "Immobilien", "Kaufen", "Finanzierung", "Energieeffizienz"],
        "related": [
            ("Immobilien Überblick", "immobilien.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
            ("Energie & Solar", "energie-solar.html"),
        ],
    },
    {
        "slug": "artikel-pkv-vs-gkv-2026",
        "title": "PKV vs GKV 2026: Die ehrliche Entscheidungshilfe",
        "meta_desc": "Private oder gesetzliche Krankenversicherung 2026 – wann lohnt die PKV wirklich und was oft verschwiegen wird.",
        "category": "Finanzen & Versicherung",
        "date": "2026-03-05",
        "read_time": "7 Min.",
        "hero_id": 375,
        "s1_id": 260, "s2_id": 399, "s3_id": 1090,
        "opening": "PKV oder GKV – diese Entscheidung hängt von mehr ab als nur dem Einkommen. Wer die Langzeitkonsequenzen kennt, entscheidet informierter.",
        "sections": [
            ("Wann die PKV wirklich vorteilhaft ist",
             "Für junge, gesunde Gutverdiener ohne Familienplanung rechnet sich PKV oft kurzfristig. Bessere Leistungen, kürzere Wartezeiten, freie Arztwahl. Der Beitrag ist mit 20–35 Jahren deutlich niedriger als der GKV-Beitrag. Der Haken: Diese Kalkulation dreht sich mit dem Alter."),
            ("Was PKV-Vertreter nicht sagen",
             "PKV-Beiträge steigen im Alter erheblich. Ohne Kinder-/Partnermitversicherung zahlt jedes Familienmitglied separat. Wechsel zurück in die GKV ist nach 55 in der Regel nicht möglich. Und: Viele PKV-Versicherte haben im Alter Probleme mit steigenden Beiträgen ohne entsprechende Einkommenssteigerung."),
            ("Die GKV-Stärken, die unterschätzt werden",
             "Einkommensunabhängige Mitversicherung von Kindern und Partner. Beitrag bleibt im Rentneralter stabil. Keine Risikoprüfung, keine Leistungsausschlüsse für Vorerkrankungen. Für Familien mit mehreren Personen fast immer günstiger. Für viele Menschen ist GKV die deutlich sicherere Langzeitstrategie."),
        ],
        "pullquote": "Die beste Versicherung ist die, die du im Alter noch bezahlen kannst.",
        "cta_text": "Versicherungsanalyse automatisieren",
        "tags": ["PKV", "GKV", "Krankenversicherung", "Versicherung", "Finanzen"],
        "related": [
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
            ("Coaching & Mindset", "coaching-mindset.html"),
            ("Karriere & HR", "karriere-hr.html"),
        ],
    },
    {
        "slug": "artikel-produktivitaet-adhs-systeme",
        "title": "Produktivität mit ADHS: Systeme die wirklich helfen",
        "meta_desc": "Wie Menschen mit ADHS trotz oder gerade wegen ihrer Neurodiversität produktiv werden – mit konkreten Systemen, nicht Willenskraft.",
        "category": "Coaching & Mindset",
        "date": "2026-02-28",
        "read_time": "8 Min.",
        "hero_id": 1090,
        "s1_id": 260, "s2_id": 399, "s3_id": 573,
        "opening": "ADHS ist kein Defizit an Aufmerksamkeit. Es ist eine andere Verteilung. Wer das versteht, baut Systeme die mit dem Gehirn arbeiten – nicht gegen es.",
        "sections": [
            ("Warum klassische Produktivitätstipps nicht funktionieren",
             "Getting Things Done, Pomodoro-Technik, Tagesplanung – gut für neurotypische Menschen. Für ADHS-Gehirne oft frustrierend. Nicht weil die Person zu schwach ist, sondern weil diese Systeme emotionale Dysregulation und Hyperfokus nicht berücksichtigen. Das richtige System ist neurodiversitäts-bewusst."),
            ("Die drei Säulen produktiver ADHS-Systeme",
             "Erstens: Externe Strukturen (kein Verlass auf innere Motivation). Zweitens: Reduktion der Entscheidungsanzahl (Decision Fatigue ist bei ADHS ausgeprägter). Drittens: Sofortiger Reward-Loops (das ADHS-Gehirn braucht unmittelbare Rückmeldung, nicht verzögerte Belohnung). Automatisierungen helfen bei allen drei."),
            ("KI und ADHS: Überraschend gute Partner",
             "KI-Tools wie Claude oder ChatGPT sind besonders hilfreich für ADHS: Externalisierung von Gedanken, Strukturierung von Aufgaben, sofortiges Feedback. Das 'Braindump'-Prinzip – alle Gedanken raus, dann sortieren lassen – ist ein Game-Changer für Menschen, die im Kopf ständig übervolle Tabs haben."),
        ],
        "pullquote": "ADHS ist kein Problem zu lösen. Es ist ein System zu bauen.",
        "cta_text": "Dein individuelles Produktivitätssystem",
        "tags": ["ADHS", "Produktivität", "Neurodiversität", "Systeme", "KI"],
        "related": [
            ("Coaching & Mindset", "coaching-mindset.html"),
            ("Automatisierungen", "automationen.html"),
            ("Karriere & HR", "karriere-hr.html"),
        ],
    },
    {
        "slug": "artikel-solaranlage-ratgeber-2026",
        "title": "Solaranlage 2026: Der komplette Ratgeber",
        "meta_desc": "Alles über Solaranlagen 2026 – Kosten, Förderungen, Anbietervergleich und was bei Planung und Installation wirklich wichtig ist.",
        "category": "Energie & Solar",
        "date": "2026-02-20",
        "read_time": "9 Min.",
        "hero_id": 459,
        "s1_id": 974, "s2_id": 129, "s3_id": 1,
        "opening": "Eine Solaranlage ist eine der wenigen Investitionen, die gleichzeitig Kosten senkt, Unabhängigkeit schafft und einen positiven ökologischen Impact hat. Aber nur wenn sie richtig geplant ist.",
        "sections": [
            ("Kosten und Wirtschaftlichkeit 2026",
             "Eine 10-kWp-Anlage kostet installiert zwischen 14.000 und 20.000 €. Die Einspeisevergütung liegt bei etwa 8 Cent/kWh. Die Amortisation berechnet sich primär über den Eigenverbrauch: Bei 0,30 €/kWh Netzstrom und 70 % Eigenverbrauch erreicht man bei guter Planung eine Amortisation in 9–12 Jahren."),
            ("Förderungen und steuerliche Aspekte",
             "Seit 2023 sind Solaranlagen in Deutschland bis 30 kWp von der Einkommenssteuer befreit (§ 3 Nr. 72 EStG). Keine Umsatzsteuer auf Module und Installation. KfW-Kredite (270/271) mit aktuell günstigen Konditionen. Und: Viele Bundesländer haben eigene Förderprogramme – prüfen lohnt sich."),
            ("Anbieterauswahl: Was wirklich zählt",
             "Nicht den günstigsten wählen – sondern den mit dem besten Service nach der Installation. Prüfe: Wie lange ist das Unternehmen schon aktiv? Gibt es Referenzen in deiner Region? Wie sieht die Garantie auf Ertrag aus? Und: Wer übernimmt die Wartung in Jahr 10? Diese Fragen trennen seriöse Anbieter von Schnellinstallateuren."),
        ],
        "pullquote": "Die beste Solaranlage ist die, die du nicht mehr bemerkst – weil sie einfach läuft.",
        "cta_text": "Energiehaushalt analysieren lassen",
        "tags": ["Solaranlage", "Photovoltaik", "Solar", "Energie", "Förderung"],
        "related": [
            ("Energie & Solar Überblick", "energie-solar.html"),
            ("Immobilien kaufen", "immobilien.html"),
            ("Finanzen & Versicherung", "finanzen-versicherung.html"),
        ],
    },
]

# ── HTML-Template ──────────────────────────────────────────────────────────────
def make_html(b: dict) -> str:
    related_html = "\n".join(
        f'    <a href="{r[1]}">{r[0]}</a>' for r in b.get("related", [])
    )
    tags_html = "\n".join(
        f'    <span class="tag">{t}</span>' for t in b.get("tags", [])
    )
    sections_html = ""
    for h2, para in b.get("sections", []):
        sections_html += f"""
  <h2>{h2}</h2>
  <p>{para}</p>
"""
    base_url = "https://automation-cango-app-empire.com"
    hero_src = f"../images/blog-real/{b['slug']}-hero.jpg"
    og_image = f"{base_url}/images/blog-real/{b['slug']}-hero.jpg"
    kw_str   = ", ".join(b.get("tags", []))

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{b['title']} | CanGo Empire Blog</title>
<meta name="description" content="{b['meta_desc']}">
<meta name="author" content="Canberk Umut Kıvılcım">
<meta name="keywords" content="{kw_str}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{base_url}/blogs/{b['slug']}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="{b['title']} | CanGo Empire">
<meta property="og:description" content="{b['meta_desc']}">
<meta property="og:url" content="{base_url}/blogs/{b['slug']}.html">
<meta property="og:site_name" content="CanGo Empire">
<meta property="og:locale" content="de_DE">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{b['title']}">
<meta property="article:published_time" content="{b['date']}">
<meta property="article:section" content="{b['category']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{b['title']}">
<meta name="twitter:description" content="{b['meta_desc']}">
<meta name="twitter:image" content="{og_image}">
<meta name="twitter:site" content="@cangoempire">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{b['title']}",
  "description": "{b['meta_desc']}",
  "image": "{og_image}",
  "url": "{base_url}/blogs/{b['slug']}.html",
  "author": {{"@type": "Person", "name": "Canberk Umut Kıvılcım"}},
  "publisher": {{"@type": "Organization", "name": "CanGo Empire", "url": "{base_url}"}},
  "datePublished": "{b['date']}",
  "inLanguage": "de",
  "articleSection": "{b['category']}",
  "keywords": "{kw_str}"
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap" media="print" onload="this.media='all'">
<style>
  :root {{
    --orange: #F97316; --navy: #0A0F1E; --navy-light: #1E293B;
    --text: #E2E8F0; --muted: #94A3B8; --gold: #D4A853;
    --link-underline: rgba(249,115,22,0.35);
  }}
  *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html {{ font-size: 16px; scroll-behavior: smooth; }}
  body {{ background: var(--navy); color: var(--text); font-family: 'Inter', Georgia, sans-serif;
    font-weight: 300; line-height: 1.9; padding: 2rem 1rem; -webkit-font-smoothing: antialiased; }}
  article {{ max-width: 720px; margin: 0 auto; }}
  .breadcrumb {{ font-size: .75rem; color: var(--muted); margin-bottom: 1.5rem; letter-spacing: .05em; }}
  .breadcrumb a {{ color: var(--muted); text-decoration: none; }}
  .breadcrumb a:hover {{ color: var(--orange); }}
  .breadcrumb span {{ margin: 0 .4rem; }}
  .hero-img {{ width: 100%; height: auto; aspect-ratio: 1200/630; object-fit: cover;
    border-radius: 8px; margin-bottom: 2.5rem; display: block; background: var(--navy-light); }}
  .meta {{ font-size: .72rem; letter-spacing: .18em; text-transform: uppercase;
    color: var(--orange); font-weight: 500; margin-bottom: 2rem; }}
  h1 {{ font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(2rem,5vw,3.4rem);
    font-weight: 600; line-height: 1.15; color: #fff; margin-bottom: .5rem; }}
  h1 em {{ color: var(--orange); font-style: italic; }}
  .byline {{ font-size: .8rem; color: var(--muted); letter-spacing: .08em; margin-bottom: 2.5rem;
    padding-bottom: 2.5rem; border-bottom: 1px solid var(--navy-light); }}
  .opening {{ font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(1.1rem,2.5vw,1.35rem);
    font-style: italic; color: #CBD5E1; line-height: 1.7; margin-bottom: 2.5rem; }}
  p {{ font-size: clamp(.9rem,1.5vw,.97rem); margin-bottom: 1.3rem; color: var(--text); }}
  h2 {{ font-family: 'Syne', sans-serif; font-size: clamp(.9rem,2vw,1.1rem); font-weight: 700;
    color: var(--orange); margin: 3rem 0 1rem; letter-spacing: .05em; text-transform: uppercase; }}
  .pullquote {{ font-family: 'Cormorant Garamond', Georgia, serif; font-size: clamp(1.2rem,3vw,1.5rem);
    font-style: italic; color: #fff; border-left: 3px solid var(--gold); padding: 1rem 0 1rem 1.5rem;
    margin: 2.5rem 0; line-height: 1.5; }}
  strong {{ color: #fff; font-weight: 500; }}
  .bento-grid {{ display: grid; grid-template-columns: repeat(3,1fr); gap: .6rem; margin: 2rem 0 3rem; }}
  .bento-item {{ position: relative; border-radius: 8px; overflow: hidden; aspect-ratio: 4/3;
    background: var(--navy-light); }}
  .bento-item:first-child {{ grid-column: 1/-1; aspect-ratio: 16/7; }}
  .bento-item img {{ width: 100%; height: 100%; object-fit: cover; display: block; transition: transform .4s; }}
  .bento-item:hover img {{ transform: scale(1.04); }}
  .bento-item figcaption {{ position: absolute; bottom: 0; right: 0;
    background: rgba(10,15,30,.65); color: rgba(148,163,184,.8); font-size: .6rem;
    padding: .2rem .45rem; border-radius: 8px 0 0 0; }}
  .cta-block {{ background: linear-gradient(135deg,#F97316,#EA580C); padding: 2rem;
    border-radius: 8px; margin-top: 3rem; text-align: center; }}
  .cta-block strong {{ font-family: 'Syne', sans-serif; font-size: clamp(1rem,2.5vw,1.15rem);
    display: block; margin-bottom: .6rem; color: #fff; }}
  .cta-block p {{ color: rgba(255,255,255,.88); margin-bottom: 1.2rem; font-size: .9rem; }}
  .cta-btn {{ display: inline-block; background: #fff; color: #EA580C; font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: .85rem; letter-spacing: .06em; text-transform: uppercase;
    padding: .75rem 1.8rem; border-radius: 4px; text-decoration: none; transition: opacity .2s; }}
  .cta-btn:hover {{ opacity: .9; }}
  .tags {{ margin-top: 2rem; }}
  .tag {{ display: inline-block; background: var(--navy-light); border: 1px solid #1E3A5F;
    color: var(--muted); font-size: .7rem; letter-spacing: .1em; text-transform: uppercase;
    padding: .3rem .7rem; border-radius: 4px; margin: .3rem .2rem 0 0; }}
  .related {{ margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--navy-light); }}
  .related-title {{ font-family: 'Syne', sans-serif; font-size: .75rem; letter-spacing: .15em;
    text-transform: uppercase; color: var(--muted); margin-bottom: 1rem; }}
  .related a {{ display: block; color: var(--text); text-decoration: none; font-size: .9rem;
    padding: .5rem 0; border-bottom: 1px solid var(--navy-light); transition: color .2s; }}
  .related a:hover {{ color: var(--orange); }}
  .related a::before {{ content: '→ '; color: var(--orange); }}
  @media (max-width: 600px) {{
    .bento-grid {{ grid-template-columns: 1fr; }}
    .bento-item:first-child {{ aspect-ratio: 16/9; }}
  }}
</style>
</head>
<body>
<article>
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="../index.html">Home</a><span>›</span>
    <a href="../blogs.html">Blog</a><span>›</span>
    {b['category']}
  </nav>

  <img src="{hero_src}" alt="{b['title']}" class="hero-img"
    width="1200" height="630" loading="eager" onerror="this.style.opacity='0'">

  <div class="meta">{b['category']} · CanGo Empire</div>
  <h1>{b['title']}</h1>
  <div class="byline">Von Canberk Umut Kıvılcım · {b['date']} · {b['read_time']} Lesezeit</div>

  <p class="opening">{b['opening']}</p>

  <section class="bento-grid" aria-label="Bildergalerie">
    <figure class="bento-item">
      <img src="../images/blog-real/{b['slug']}-hero.jpg" alt="{b['title']} Visual" loading="lazy">
      <figcaption>© Unsplash via Picsum</figcaption>
    </figure>
    <figure class="bento-item">
      <img src="../images/blog-real/{b['slug']}-s1.jpg" alt="{b['title']} Visual 2" loading="lazy">
      <figcaption>© Unsplash via Picsum</figcaption>
    </figure>
    <figure class="bento-item">
      <img src="../images/blog-real/{b['slug']}-s2.jpg" alt="{b['title']} Visual 3" loading="lazy">
      <figcaption>© Unsplash via Picsum</figcaption>
    </figure>
    <figure class="bento-item">
      <img src="../images/blog-real/{b['slug']}-s3.jpg" alt="{b['title']} Visual 4" loading="lazy">
      <figcaption>© Unsplash via Picsum</figcaption>
    </figure>
  </section>

{sections_html}

  <blockquote class="pullquote">{b['pullquote']}</blockquote>

  <div class="cta-block">
    <strong>{b['cta_text']}</strong>
    <p>CanGo Empire – Automatisierung mit Absicht.</p>
    <a href="../index.html" class="cta-btn">Mehr erfahren</a>
  </div>

  <div class="tags">
{tags_html}
  </div>

  <nav class="related" aria-label="Ähnliche Artikel">
    <div class="related-title">Ähnliche Artikel</div>
{related_html}
  </nav>

</article>
</body>
</html>"""

def picsum(pid: int, w: int, h: int) -> str:
    return f"https://picsum.photos/id/{pid}/{w}/{h}"

def dl(url, dest):
    if dest.exists() and dest.stat().st_size > 5000:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CanGoEmpire/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            dest.write_bytes(r.read())
        return True
    except:
        return False

def ftp_mkdir(ftp, path):
    parts = path.strip("/").split("/")
    cur = "/"
    for p in parts:
        cur = f"{cur}{p}/"
        try: ftp.cwd(cur)
        except:
            try: ftp.mkd(cur); ftp.cwd(cur)
            except: pass

def ftp_upload(ftp, local, remote_dir, name):
    try:
        ftp.cwd(remote_dir)
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {name}", f)
        return True
    except Exception as e:
        print(f"  FTP ✗ {name}: {e}")
        return False

def main():
    print("\n🚀 CanGo Empire – Blog-Generierung + Bilder + Upload\n")

    # FTP verbinden
    print("📡 FTP-Verbindung aufbauen...")
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        print("✅ FTP verbunden\n")
    except Exception as e:
        print(f"❌ FTP Fehler: {e}")
        ftp = None

    blogs_remote  = f"{REMOTE}/blogs"
    images_remote = f"{REMOTE}/images/blog-real"

    if ftp:
        ftp_mkdir(ftp, blogs_remote)
        ftp_mkdir(ftp, images_remote)

    created = 0
    for b in BLOGS:
        slug = b["slug"]
        html_path = BLOGS_DIR / f"{slug}.html"
        print(f"📄 {slug}")

        # HTML generieren
        html = make_html(b)
        html_path.write_text(html, encoding="utf-8")
        print(f"  ✓ HTML erstellt")

        # Bilder herunterladen
        pairs = [
            (b["hero_id"], 1200, 630, f"{slug}-hero.jpg"),
            (b["s1_id"],   800, 600, f"{slug}-s1.jpg"),
            (b["s2_id"],   800, 600, f"{slug}-s2.jpg"),
            (b["s3_id"],   800, 600, f"{slug}-s3.jpg"),
        ]
        for pid, w, h, fname in pairs:
            dest = IMG_DIR / fname
            if dl(picsum(pid, w, h), dest):
                print(f"  ↓ {fname}")
            time.sleep(0.15)

        # FTP-Upload
        if ftp:
            ftp_upload(ftp, html_path, blogs_remote, f"{slug}.html")
            for _, _, _, fname in pairs:
                ftp_upload(ftp, IMG_DIR / fname, images_remote, fname)
            print(f"  ↑ FTP live")

        created += 1
        print()

    # blogs.html aktualisieren
    update_blogs_listing(ftp)

    if ftp:
        try: ftp.quit()
        except: pass

    print(f"✅ {created} Blogs erstellt und live!")
    print("🌐 https://automation-cango-app-empire.com/blogs.html\n")

def update_blogs_listing(ftp):
    """Fügt alle Blogs zur blogs.html hinzu."""
    content = BLOGS_HTML.read_text(encoding="utf-8")

    # Alle vorhandenen Blog-Slugs sammeln
    all_slugs = set(re.findall(r'href="blogs/([^"]+\.html)"', content))

    new_cards = []
    for b in BLOGS:
        slug = b["slug"]
        fname = f"{slug}.html"
        if fname not in all_slugs:
            card = f"""
      <a class="blog-card" href="blogs/{fname}">
        <div class="card-img" style="background:url('../images/blog-real/{slug}-hero.jpg') center/cover no-repeat; aspect-ratio:16/9; border-radius:6px 6px 0 0;"></div>
        <div class="card-body" style="padding:1rem;">
          <div class="card-meta" style="font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;color:#F97316;margin-bottom:.5rem;">{b['category']}</div>
          <h3 style="font-size:1rem;color:#fff;margin-bottom:.4rem;">{b['title']}</h3>
          <p style="font-size:.82rem;color:#94A3B8;line-height:1.5;">{b['meta_desc'][:100]}…</p>
        </div>
      </a>"""
            new_cards.append(card)

    if new_cards:
        # Vor </main> oder vor dem letzten </section> einfügen
        insert_marker = "</main>"
        if insert_marker not in content:
            insert_marker = "</body>"
        cards_block = "\n    <!-- NEUE BLOG-CARDS -->\n" + "\n".join(new_cards) + "\n    <!-- /NEUE BLOG-CARDS -->\n    "
        content = content.replace(insert_marker, cards_block + insert_marker, 1)
        BLOGS_HTML.write_text(content, encoding="utf-8")
        print(f"  ✏ blogs.html um {len(new_cards)} Einträge erweitert")

        if ftp:
            ftp_upload(ftp, BLOGS_HTML, REMOTE, "blogs.html")
            print(f"  ↑ blogs.html FTP live")

if __name__ == "__main__":
    main()
