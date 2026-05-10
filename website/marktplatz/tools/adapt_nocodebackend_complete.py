#!/usr/bin/env python3
"""
Vollständige Anpassung von nocodebackend.html
Alle Sections werden systematisch angepasst für NoCodeBackend
"""

import re
import sys

# NoCodeBackend Daten aus ki-tech.html
NOCODEBACKEND_DATA = {
    'name': 'NoCodeBackend',
    'badge': 'BACKEND-AS-A-SERVICE',
    'description': 'No-Code Backend-Plattform. Erstelle APIs und Backends ohne Code für deine Apps und Websites.',
    'features': [
        {
            'title': 'No-Code Backend',
            'description': 'Erstelle APIs und Backends ohne Code. Vollständige Backend-Lösung für deine Apps und Websites.',
            'icon': 'server'
        },
        {
            'title': 'API Builder',
            'description': 'Visueller API-Builder für REST-APIs. Erstelle APIs mit Drag-and-Drop Interface.',
            'icon': 'code'
        },
        {
            'title': 'Database Management',
            'description': 'Integriertes Datenbank-Management für deine App-Daten. Einfache Datenverwaltung.',
            'icon': 'database'
        },
        {
            'title': 'Authentication',
            'description': 'Built-in Authentication für Benutzer-Anmeldung. OAuth, JWT und mehr.',
            'icon': 'shield'
        },
        {
            'title': 'Cloud Hosting',
            'description': 'Cloud-basiertes Hosting für deine Backends. Automatische Skalierung und Deployment.',
            'icon': 'cloud'
        },
        {
            'title': 'API Integration',
            'description': 'Einfache Integration in deine Apps. REST API für nahtlose Verbindung.',
            'icon': 'link'
        }
    ],
    'price': 'Freemium / Pro',
    'logo': 'https://cdn.simpleicons.org/server/FF6B6B',
    'keywords': 'NoCodeBackend, Backend as a Service, No-Code Backend, API Builder, Database Management'
}

def adapt_file(file_path):
    """Vollständige Anpassung der nocodebackend.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Make besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {NOCODEBACKEND_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der No-Code Backend-Plattform.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: No-Code Backend
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: API Builder
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Database Management
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Authentication
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><circle cx="12" cy="10" r="3"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Cloud Hosting
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: API Integration
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{NOCODEBACKEND_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{NOCODEBACKEND_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {NOCODEBACKEND_DATA["name"]}?</h3>
          <p>
            {NOCODEBACKEND_DATA["name"]} ist eine No-Code Backend-Plattform. Mit visueller API-Erstellung und Datenbank-Management erstellst du vollständige Backends für deine Apps und Websites – ganz ohne Code.
          </p>
          <p>
            Im Gegensatz zu traditionellen Backend-Entwicklung bietet {NOCODEBACKEND_DATA["name"]} eine vollständige No-Code-Lösung für APIs, Datenbanken und Authentication. Das macht {NOCODEBACKEND_DATA["name"]} zur ersten Wahl für No-Code-Entwickler und Startups.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Erstelle APIs und Backends ohne Code
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Visueller API-Builder für REST-APIs
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Integriertes Datenbank-Management
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: NoCodeBackend Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {NOCODEBACKEND_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: App Development
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📱</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">App Development</h3>\n            <p class="usecase-description">Erstelle Backends für deine Apps ohne Code. Vollständige Backend-Lösung für Mobile und Web Apps.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: API Creation
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🔌</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">API Creation</h3>\n            <p class="usecase-description">Erstelle REST-APIs mit visueller API-Erstellung. Perfekt für Integrationen und Automatisierungen.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Database Management
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">💾</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Database Management</h3>\n            <p class="usecase-description">Verwalte deine App-Daten effizient. Integriertes Datenbank-Management für einfache Datenverwaltung.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {NOCODEBACKEND_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die No-Code Backend-Plattform.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">API Builder Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Database Management</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Authentication</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Cloud Hosting</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{NOCODEBACKEND_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{NOCODEBACKEND_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. No-Code Backend, API Builder, Database Management und Authentication.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>No-Code Backend</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>API Builder</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Database Management</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Authentication</div>\n        </div>\n        <a href="#" class="btn btn-primary">{NOCODEBACKEND_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>No-Code Backend</strong> – Erstelle APIs und Backends ohne Code</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>API Builder</strong> – Visueller API-Builder für REST-APIs</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Database Management</strong> – Integriertes Datenbank-Management für deine App-Daten</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Authentication</strong> – Built-in Authentication für Benutzer-Anmeldung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Cloud Hosting</strong> – Cloud-basiertes Hosting mit automatischer Skalierung</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Lernkurve</strong> – API-Erstellung erfordert etwas Einarbeitung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Feature-Limits</strong> – Einige Features nur in höheren Plänen verfügbar</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Vendor Lock-in</strong> – Abhängig von der Plattform, Migration kann schwierig sein</span></li>',
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
        f'<h2 class="section-title">{NOCODEBACKEND_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{NOCODEBACKEND_DATA["name"]}</th><th>Firebase</th><th>Supabase</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {NOCODEBACKEND_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle Backends ohne Code mit visueller API-Erstellung und Datenbank-Management.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'nocode-backend.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
