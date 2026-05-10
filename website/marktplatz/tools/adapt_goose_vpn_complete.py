#!/usr/bin/env python3
"""
Vollständige Anpassung von goose-vpn.html
Alle Sections werden systematisch angepasst für GOOSE VPN
"""

import re
import sys

# GOOSE VPN Daten aus ki-tech.html
GOOSE_VPN_DATA = {
    'name': 'GOOSE VPN',
    'badge': 'VPN',
    'description': 'Sicherer VPN-Service. Schutz deiner Privatsphäre und Anonymität im Internet.',
    'features': [
        {
            'title': 'Sicherer VPN',
            'description': 'Sicherer VPN-Service für deine Privatsphäre und Anonymität. Verschlüsselte Verbindungen.',
            'icon': 'shield'
        },
        {
            'title': 'Multi-Server',
            'description': 'Große Auswahl an Servern in verschiedenen Ländern. Wähle den besten Server für dich.',
            'icon': 'globe'
        },
        {
            'title': 'Kill Switch',
            'description': 'Automatischer Kill Switch für sichere Verbindungen. Schutz vor Datenlecks.',
            'icon': 'alert-triangle'
        },
        {
            'title': 'No-Log Policy',
            'description': 'Strikte No-Log Policy für maximale Privatsphäre. Keine Speicherung deiner Daten.',
            'icon': 'lock'
        },
        {
            'title': 'Multi-Platform',
            'description': 'Unterstützung für verschiedene Plattformen. Windows, macOS, iOS, Android und mehr.',
            'icon': 'layers'
        },
        {
            'title': 'Schnelle Verbindung',
            'description': 'Schnelle Verbindungsgeschwindigkeiten für nahtloses Surfen. Optimierte Server.',
            'icon': 'zap'
        }
    ],
    'price': 'Freemium / Pro',
    'logo': 'https://cdn.simpleicons.org/vpn/FF6B6B',
    'keywords': 'GOOSE VPN, VPN Service, Privacy, Security, Anonymity, Kill Switch, No-Log Policy'
}

def adapt_file(file_path):
    """Vollständige Anpassung der goose-vpn.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Make besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {GOOSE_VPN_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile des sicheren VPN-Services.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Sicherer VPN
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><circle cx="12" cy="10" r="3"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Multi-Server
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Kill Switch
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: No-Log Policy
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Multi-Platform
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Schnelle Verbindung
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{GOOSE_VPN_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{GOOSE_VPN_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {GOOSE_VPN_DATA["name"]}?</h3>
          <p>
            {GOOSE_VPN_DATA["name"]} ist ein sicherer VPN-Service für deine Privatsphäre und Anonymität im Internet. Mit verschlüsselten Verbindungen und strikter No-Log Policy schützt {GOOSE_VPN_DATA["name"]} deine Daten – perfekt für Privatnutzer und Unternehmen.
          </p>
          <p>
            Im Gegensatz zu unverschlüsselten Verbindungen bietet {GOOSE_VPN_DATA["name"]} vollständige Verschlüsselung deiner Internet-Verbindungen. Das macht {GOOSE_VPN_DATA["name"]} zur ersten Wahl für alle, die ihre Privatsphäre schützen wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Sicherer VPN-Service für deine Privatsphäre und Anonymität
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Große Auswahl an Servern in verschiedenen Ländern
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Strikte No-Log Policy für maximale Privatsphäre
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: GOOSE VPN Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {GOOSE_VPN_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Privacy Protection
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🔒</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Privacy Protection</h3>\n            <p class="usecase-description">Schütze deine Privatsphäre im Internet. Verschlüsselte Verbindungen für sichere Datenübertragung.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Geo-Unblocking
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🌍</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Geo-Unblocking</h3>\n            <p class="usecase-description">Greife auf geo-beschränkte Inhalte zu. Wähle Server in verschiedenen Ländern für Zugriff.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Public WiFi Security
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📶</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Public WiFi Security</h3>\n            <p class="usecase-description">Schütze dich auf öffentlichen WiFi-Netzwerken. Verschlüsselte Verbindungen für sichere Kommunikation.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {GOOSE_VPN_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf den sicheren VPN-Service.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">VPN Client Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Server-Auswahl</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Kill Switch</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Multi-Platform</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{GOOSE_VPN_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{GOOSE_VPN_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Sicherer VPN, Multi-Server, Kill Switch und No-Log Policy.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Sicherer VPN</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Multi-Server</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Kill Switch</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>No-Log Policy</div>\n        </div>\n        <a href="#" class="btn btn-primary">{GOOSE_VPN_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Sicherer VPN</strong> – Verschlüsselte Verbindungen für deine Privatsphäre</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Multi-Server</strong> – Große Auswahl an Servern in verschiedenen Ländern</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Kill Switch</strong> – Automatischer Kill Switch für sichere Verbindungen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>No-Log Policy</strong> – Strikte No-Log Policy für maximale Privatsphäre</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Multi-Platform</strong> – Unterstützung für verschiedene Plattformen</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Geschwindigkeit</strong> – VPN kann die Internet-Geschwindigkeit reduzieren</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Server-Auswahl</strong> – Begrenzte Server-Auswahl in einigen Ländern</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Setup</strong> – Einrichtung erfordert etwas technisches Verständnis</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Dokumentation</strong> – Dokumentation könnte ausführlicher sein</span></li>',
        content
    )
    
    # 8. Comparison
    content = re.sub(
        r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)',
        f'<h2 class="section-title">{GOOSE_VPN_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{GOOSE_VPN_DATA["name"]}</th><th>NordVPN</th><th>ExpressVPN</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {GOOSE_VPN_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und schütze deine Privatsphäre im Internet mit sicherem VPN und verschlüsselten Verbindungen.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'goose-vpn.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
