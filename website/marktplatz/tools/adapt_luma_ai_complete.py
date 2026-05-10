#!/usr/bin/env python3
"""
Vollständige Anpassung von luma-ai.html
Alle Sections werden systematisch angepasst für Luma AI
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Luma AI Daten aus ki-tech.html
LUMA_AI_DATA = {
    'name': 'Luma AI',
    'badge': 'VIDEO AI',
    'description': 'AI-powered Video Generation. Erstelle professionelle Videos mit KI-gestützter Animation und Motion Graphics.',
    'features': [
        {
            'title': 'AI Video Generation',
            'description': 'AI-powered Video Generation für professionelle Videos. KI-gestützte Animation und Motion Graphics.',
            'icon': 'video'
        },
        {
            'title': '3D Animation',
            'description': '3D Animation mit KI-Unterstützung. Erstelle animierte 3D-Grafiken automatisch.',
            'icon': 'box'
        },
        {
            'title': 'Motion Graphics',
            'description': 'Professionelle Motion Graphics mit KI-Unterstützung. Erstelle animierte Grafiken automatisch.',
            'icon': 'sparkles'
        },
        {
            'title': 'Render Options',
            'description': 'Vielseitige Render-Optionen für verschiedene Formate. HD, 4K und Social Media Formate.',
            'icon': 'download'
        },
        {
            'title': 'Cloud-based',
            'description': 'Cloud-basierte Plattform für nahtlose Zusammenarbeit. Arbeite von überall aus.',
            'icon': 'cloud'
        },
        {
            'title': 'Easy Export',
            'description': 'Einfacher Export für verschiedene Plattformen. Perfekt für Social Media und Marketing.',
            'icon': 'share'
        }
    ],
    'price': 'Freemium / Pro',
    'logo': 'https://cdn.simpleicons.org/video/FF6B6B',
    'keywords': 'Luma AI, Video AI, AI Video Generation, 3D Animation, Motion Graphics, Video Editing'
}

def adapt_file(file_path):
    """Vollständige Anpassung der luma-ai.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section - Titel und Subtitle anpassen, aber Platzhalter behalten
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{LUMA_AI_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {LUMA_AI_DATA["name"]} AI-powered Video Generation und 3D Animation erstellst.</p>',
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
        r'(<h2 class="section-title">Was macht Luma AI besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {LUMA_AI_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der AI-powered Video Generation.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: AI Video Generation
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: 3D Animation
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Motion Graphics
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Render Options
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Cloud-based
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Easy Export
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{LUMA_AI_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{LUMA_AI_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {LUMA_AI_DATA["name"]}?</h3>
          <p>
            {LUMA_AI_DATA["name"]} ist eine AI-powered Video Generation-Plattform für professionelle Videos. Mit KI-gestützter Animation, 3D Animation und Motion Graphics erstellst du professionelle Videos automatisch – perfekt für Content-Creator und Marketing-Teams.
          </p>
          <p>
            Im Gegensatz zu traditionellen Video-Editoren verwendet {LUMA_AI_DATA["name"]} KI, um automatisch animierte Grafiken und professionelle Videos zu erstellen. Das macht {LUMA_AI_DATA["name"]} zur ersten Wahl für alle, die schnell hochwertige Videos produzieren wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-powered Video Generation für professionelle Videos
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              3D Animation mit KI-Unterstützung
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Professionelle Motion Graphics mit KI-Unterstützung
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Luma AI Dashboard</span>',
        content
    )
    
    # 4. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {LUMA_AI_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Social Media Videos
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📱</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Social Media Videos</h3>\n            <p class="usecase-description">Erstelle virale Social Media Videos mit AI-powered Video Generation. Perfekt für TikTok, Instagram und YouTube.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Marketing Videos
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📺</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Marketing Videos</h3>\n            <p class="usecase-description">Professionelle Marketing Videos mit 3D Animation und Motion Graphics. Erstelle animierte Werbevideos automatisch.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Content Creation
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🎬</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Content Creation</h3>\n            <p class="usecase-description">Beschleunige deine Content-Produktion. Erstelle professionelle Videos schneller mit AI-powered Video Generation.</p>\n          </div>\n        </div>',
        content
    )
    
    # 5. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {LUMA_AI_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die AI-powered Video Generation-Plattform.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Video Editor Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">3D Animation</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Motion Graphics</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Render Options</div>', content)
    
    # 6. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{LUMA_AI_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 7. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{LUMA_AI_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. AI Video Generation, 3D Animation, Motion Graphics und Render Options.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>AI Video Generation</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>3D Animation</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Motion Graphics</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Render Options</div>\n        </div>\n        <a href="#" class="btn btn-primary">{LUMA_AI_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 8. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>AI-powered</strong> – KI-gestützte Video Generation für professionelle Ergebnisse</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>3D Animation</strong> – 3D Animation mit KI-Unterstützung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Motion Graphics</strong> – Professionelle Motion Graphics mit KI-Unterstützung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Render Options</strong> – Vielseitige Render-Optionen für verschiedene Formate</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Cloud-based</strong> – Cloud-basierte Plattform für nahtlose Zusammenarbeit</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Preis steigt schnell</strong> – Höhere Preise für größere Volumen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Render-Zeit</strong> – Größere Videos benötigen mehr Render-Zeit</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Feature-Limits</strong> – Einige Features nur in höheren Plänen verfügbar</span></li>',
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
        f'<h2 class="section-title">{LUMA_AI_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{LUMA_AI_DATA["name"]}</th><th>Runway</th><th>Descript</th></tr>',
        content
    )
    
    # 10. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {LUMA_AI_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle professionelle Videos mit AI-powered Video Generation, 3D Animation und Motion Graphics.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'luma-ai.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
