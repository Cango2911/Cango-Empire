#!/usr/bin/env python3
"""
Vollständige Anpassung von hostinger.html
Alle Sections werden systematisch angepasst für Hostinger
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Hostinger Daten aus ki-tech.html
HOSTINGER_DATA = {
    'name': 'Hostinger',
    'badge': 'HOSTING',
    'description': 'VPS-Hosting für Self-Hosted Anwendungen. Global Locations, SSD Storage und 24/7 Support.',
    'features': [
        {
            'title': 'VPS Hosting',
            'description': 'Professionelles VPS-Hosting für Self-Hosted Anwendungen. Volle Kontrolle über deine Server.',
            'icon': 'server'
        },
        {
            'title': 'Global Locations',
            'description': 'Server-Standorte weltweit für optimale Performance. Wähle den besten Standort für dich.',
            'icon': 'globe'
        },
        {
            'title': 'SSD Storage',
            'description': 'Schnelle SSD Storage für optimale Performance. NVMe SSDs für maximale Geschwindigkeit.',
            'icon': 'database'
        },
        {
            'title': '24/7 Support',
            'description': 'Rund um die Uhr Support für deine Anwendungen. Professionelle Hilfe bei Problemen.',
            'icon': 'headphones'
        },
        {
            'title': 'Scalable Infrastructure',
            'description': 'Skalierbare Infrastruktur für wachsende Projekte. Upgrade deine Ressourcen jederzeit.',
            'icon': 'layers'
        },
        {
            'title': 'Affordable Pricing',
            'description': 'Günstige Preise ab 3.99$ / Monat. Perfekt für Startups und kleine Projekte.',
            'icon': 'dollar-sign'
        }
    ],
    'price': 'ab 3.99$ / Monat',
    'logo': 'https://cdn.simpleicons.org/hostinger/673DE6',
    'keywords': 'Hostinger, VPS Hosting, Web Hosting, Server, Cloud Hosting, SSD Storage'
}

def adapt_file(file_path):
    """Vollständige Anpassung der hostinger.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section - Titel und Subtitle anpassen, aber Platzhalter behalten
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{HOSTINGER_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {HOSTINGER_DATA["name"]} VPS-Hosting für Self-Hosted Anwendungen nutzt.</p>',
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
        r'(<h2 class="section-title">Was macht Hostinger besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {HOSTINGER_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile des VPS-Hostings für Self-Hosted Anwendungen.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: VPS Hosting
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Global Locations
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: SSD Storage
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: 24/7 Support
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Scalable Infrastructure
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Affordable Pricing
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{HOSTINGER_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{HOSTINGER_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {HOSTINGER_DATA["name"]}?</h3>
          <p>
            {HOSTINGER_DATA["name"]} ist ein VPS-Hosting-Provider für Self-Hosted Anwendungen. Mit Global Locations, SSD Storage und 24/7 Support hostest du deine Anwendungen professionell – perfekt für Entwickler und Unternehmen.
          </p>
          <p>
            Im Gegensatz zu Shared Hosting bietet {HOSTINGER_DATA["name"]} volle Kontrolle über deine Server mit VPS-Hosting. Das macht {HOSTINGER_DATA["name"]} zur ersten Wahl für alle, die Self-Hosted Anwendungen betreiben wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Professionelles VPS-Hosting für Self-Hosted Anwendungen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Server-Standorte weltweit für optimale Performance
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Schnelle SSD Storage für optimale Performance
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Hostinger Dashboard</span>',
        content
    )
    
    # 4. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {HOSTINGER_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Self-Hosted Apps
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🖥️</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Self-Hosted Apps</h3>\n            <p class="usecase-description">Hoste Self-Hosted Anwendungen wie n8n, Make oder eigene APIs. VPS-Hosting für volle Kontrolle.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Web Applications
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🌐</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Web Applications</h3>\n            <p class="usecase-description">Hoste Web-Anwendungen und APIs. Schnelle SSD Storage für optimale Performance.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Database Hosting
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">💾</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Database Hosting</h3>\n            <p class="usecase-description">Hoste Datenbanken für deine Anwendungen. PostgreSQL, MySQL und MongoDB Support.</p>\n          </div>\n        </div>',
        content
    )
    
    # 5. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {HOSTINGER_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf das VPS-Hosting für Self-Hosted Anwendungen.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">VPS Dashboard</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Global Locations</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">SSD Storage</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">24/7 Support</div>', content)
    
    # 6. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{HOSTINGER_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 7. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{HOSTINGER_DATA["name"]} VPS</h2>\n        <div class="package-price">ab 3.99$/Monat</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. VPS Hosting, Global Locations, SSD Storage und 24/7 Support – günstig und zuverlässig.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>VPS Hosting</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Global Locations</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>SSD Storage</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>24/7 Support</div>\n        </div>\n        <a href="#" class="btn btn-primary">{HOSTINGER_DATA["name"]} VPS holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 8. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>VPS Hosting</strong> – Professionelles VPS-Hosting für Self-Hosted Anwendungen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Global Locations</strong> – Server-Standorte weltweit für optimale Performance</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>SSD Storage</strong> – Schnelle SSD Storage für optimale Performance</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>24/7 Support</strong> – Rund um die Uhr Support für deine Anwendungen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Affordable Pricing</strong> – Günstige Preise ab 3.99$ / Monat</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Lernkurve</strong> – VPS-Management erfordert technische Kenntnisse</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Resource Limits</strong> – Resource Limits können bei großen Projekten einschränkend sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Setup-Zeit</strong> – Server-Setup kann etwas Zeit in Anspruch nehmen</span></li>',
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
        f'<h2 class="section-title">{HOSTINGER_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{HOSTINGER_DATA["name"]}</th><th>DigitalOcean</th><th>Linode</th></tr>',
        content
    )
    
    # 10. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {HOSTINGER_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und hoste deine Self-Hosted Anwendungen mit VPS-Hosting, Global Locations und SSD Storage.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'hostinger.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
