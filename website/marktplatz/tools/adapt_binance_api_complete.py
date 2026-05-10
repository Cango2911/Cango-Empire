#!/usr/bin/env python3
"""
Vollständige Anpassung von binance-api.html
Alle Sections werden systematisch angepasst für Binance API
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Binance API Daten aus ki-tech.html
BINANCE_API_DATA = {
    'name': 'Binance API',
    'badge': 'CRYPTO API',
    'description': 'Cryptocurrency Trading API. Real-time Market Data, Trading-Bots und Portfolio-Management für Automation.',
    'features': [
        {
            'title': 'Real-time Market Data',
            'description': 'Real-time Market Data für alle Kryptowährungen. Aktuelle Kurse und Marktdaten.',
            'icon': 'trending-up'
        },
        {
            'title': 'Trading API',
            'description': 'Vollständige Trading API für automatisierten Handel. Spot, Futures und mehr.',
            'icon': 'activity'
        },
        {
            'title': 'WebSocket Streams',
            'description': 'WebSocket Streams für Live-Daten. Real-time Updates für Marktdaten und Orders.',
            'icon': 'radio'
        },
        {
            'title': 'Futures & Spot',
            'description': 'Unterstützung für Futures und Spot Trading. Vollständige Handelsplattform-Integration.',
            'icon': 'layers'
        },
        {
            'title': 'Portfolio Management',
            'description': 'Portfolio-Management für deine Assets. Überwache deine Kryptowährungen.',
            'icon': 'pie-chart'
        },
        {
            'title': 'Kostenlos',
            'description': 'Kostenlose API-Nutzung mit Rate Limits. Perfekt für Entwickler und Trader.',
            'icon': 'check-circle'
        }
    ],
    'price': 'Kostenlos',
    'logo': 'https://cdn.simpleicons.org/binance/F0B90B',
    'keywords': 'Binance API, Crypto API, Trading API, Real-time Market Data, WebSocket Streams, Cryptocurrency'
}

def adapt_file(file_path):
    """Vollständige Anpassung der binance-api.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section - Titel und Subtitle anpassen, aber Platzhalter behalten
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{BINANCE_API_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {BINANCE_API_DATA["name"]} Real-time Market Data und Trading API für automatisierten Handel nutzt.</p>',
        content
    )
    
    # Video Placeholder Text anpassen
    content = re.sub(
        r'(<p>Klicken um Video zu laden</p>|<p>Video wird später integriert</p>)',
        '<p>Video wird später integriert</p>',
        content
    )
    
    # 2. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Binance API besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {BINANCE_API_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Cryptocurrency Trading API.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Real-time Market Data
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Trading API
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: WebSocket Streams
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="M12 8v8"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Futures & Spot
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Portfolio Management
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Kostenlos
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{BINANCE_API_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{BINANCE_API_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {BINANCE_API_DATA["name"]}?</h3>
          <p>
            {BINANCE_API_DATA["name"]} ist eine Cryptocurrency Trading API für Real-time Market Data und automatisierten Handel. Mit WebSocket Streams und vollständiger Trading API erstellst du Trading-Bots und Portfolio-Management-Tools – perfekt für Krypto-Trader und Entwickler.
          </p>
          <p>
            Im Gegensatz zu manuellen Trading-Plattformen bietet {BINANCE_API_DATA["name"]} vollständige API-Integration für automatisierten Handel. Das macht {BINANCE_API_DATA["name"]} zur ersten Wahl für alle, die Trading-Bots erstellen wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Real-time Market Data für alle Kryptowährungen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Vollständige Trading API für automatisierten Handel
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              WebSocket Streams für Live-Daten
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Binance API Dashboard</span>',
        content
    )
    
    # 4. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {BINANCE_API_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Trading Bots
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🤖</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Trading Bots</h3>\n            <p class="usecase-description">Erstelle Trading-Bots für automatisierten Handel. Real-time Market Data und Trading API für professionelle Bots.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Portfolio Management
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📊</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Portfolio Management</h3>\n            <p class="usecase-description">Verwalte dein Krypto-Portfolio automatisch. Überwache deine Assets mit Real-time Market Data.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Market Analysis
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📈</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Market Analysis</h3>\n            <p class="usecase-description">Analysiere Krypto-Märkte mit Real-time Daten. WebSocket Streams für Live-Marktanalyse.</p>\n          </div>\n        </div>',
        content
    )
    
    # 5. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {BINANCE_API_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die Cryptocurrency Trading API.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">API Dashboard</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Real-time Market Data</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Trading API</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">WebSocket Streams</div>', content)
    
    # 6. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{BINANCE_API_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 7. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{BINANCE_API_DATA["name"]} Free</h2>\n        <div class="package-price">Kostenlos</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Real-time Market Data, Trading API, WebSocket Streams und Futures & Spot – kostenlos mit Rate Limits.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Real-time Market Data</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Trading API</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>WebSocket Streams</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Futures & Spot</div>\n        </div>\n        <a href="#" class="btn btn-primary">{BINANCE_API_DATA["name"]} kostenlos nutzen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 8. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Real-time Market Data</strong> – Aktuelle Kurse und Marktdaten für alle Kryptowährungen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Trading API</strong> – Vollständige Trading API für automatisierten Handel</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>WebSocket Streams</strong> – WebSocket Streams für Live-Daten</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Futures & Spot</strong> – Unterstützung für Futures und Spot Trading</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Kostenlos</strong> – Kostenlose API-Nutzung mit Rate Limits</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Lernkurve</strong> – API-Integration erfordert technische Kenntnisse</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Rate Limits</strong> – Rate Limits können bei hohem Volumen einschränkend sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>API-Updates</strong> – API-Updates können Breaking Changes mit sich bringen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Dokumentation</strong> – Dokumentation könnte ausführlicher sein</span></li>',
        content
    )
    
    # 9. Comparison
    content = re.sub(
        r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)',
        f'<h2 class="section-title">{BINANCE_API_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{BINANCE_API_DATA["name"]}</th><th>Coinbase API</th><th>Kraken API</th></tr>',
        content
    )
    
    # 10. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {BINANCE_API_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und nutze Real-time Market Data und Trading API für automatisierten Handel und Trading-Bots.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'binance-api.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
