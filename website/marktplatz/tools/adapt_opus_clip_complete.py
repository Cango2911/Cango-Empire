#!/usr/bin/env python3
"""
Vollständige Anpassung von opus-clip.html
Alle Sections werden systematisch angepasst für Opus Clip
"""

import re
import sys

# Opus Clip Daten aus ki-tech.html
OPUS_CLIP_DATA = {
    'name': 'Opus Clip',
    'badge': 'VIDEO CLIPPER',
    'description': 'AI-basierte Video-Klip-Generierung. Automatisches Clipping von Long-Form-Videos in viral-würdige Shorts.',
    'features': [
        {
            'title': 'Auto-Video-Clipping',
            'description': 'Automatisches Clipping von Long-Form-Videos in viral-würdige Shorts. AI-basierte Video-Klip-Generierung.',
            'icon': 'scissors'
        },
        {
            'title': 'Viral-Moment Detection',
            'description': 'Intelligente Erkennung von viral-würdigen Momenten. Finde die besten Clips für maximale Reichweite.',
            'icon': 'trending-up'
        },
        {
            'title': 'Auto-Captions',
            'description': 'Automatische Untertitel-Generierung für alle Clips. Verbessere die Zugänglichkeit und Reichweite.',
            'icon': 'message-square'
        },
        {
            'title': 'Multi-Format Export',
            'description': 'Exportiere Clips in verschiedenen Formaten. Perfekt für TikTok, Instagram, YouTube Shorts und mehr.',
            'icon': 'download'
        },
        {
            'title': 'AI-basierte Generierung',
            'description': 'KI-gestützte Video-Analyse und Clip-Generierung. Automatische Erkennung der besten Momente.',
            'icon': 'sparkles'
        },
        {
            'title': 'Schnelle Verarbeitung',
            'description': 'Schnelle Video-Verarbeitung für sofortige Ergebnisse. Effiziente KI-Engine für optimale Performance.',
            'icon': 'zap'
        }
    ],
    'price': 'ab 19$ / Monat',
    'logo': 'https://cdn.simpleicons.org/opus/FF6B6B',
    'keywords': 'Opus Clip, Video Clipper, AI Video Clipping, Viral Moments, Shorts Generator, Video Editing'
}

def adapt_file(file_path):
    """Vollständige Anpassung der opus-clip.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Opus Clip besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {OPUS_CLIP_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der AI-basierten Video-Klip-Generierung.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Auto-Video-Clipping
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Viral-Moment Detection
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Auto-Captions
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Multi-Format Export
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: AI-basierte Generierung
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Schnelle Verarbeitung
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{OPUS_CLIP_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{OPUS_CLIP_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Opus Clip\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {OPUS_CLIP_DATA["name"]}?</h3>
          <p>
            {OPUS_CLIP_DATA["name"]} ist eine AI-basierte Video-Klip-Generierungsplattform. Mit automatischem Clipping konvertiert {OPUS_CLIP_DATA["name"]} Long-Form-Videos in viral-würdige Shorts – perfekt für Social Media Marketing.
          </p>
          <p>
            Im Gegensatz zu traditionellen Video-Editoren verwendet {OPUS_CLIP_DATA["name"]} KI, um automatisch die besten Momente zu finden und in viral-würdige Clips zu verwandeln. Das macht {OPUS_CLIP_DATA["name"]} zur ersten Wahl für Content-Creator und Social Media Manager.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatisches Clipping von Long-Form-Videos in Shorts
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-basierte Erkennung von viral-würdigen Momenten
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatische Untertitel-Generierung für alle Clips
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Opus Clip Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {OPUS_CLIP_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Social Media Marketing
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📱</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Social Media Marketing</h3>\n            <p class="usecase-description">Erstelle virale Shorts für TikTok, Instagram und YouTube. Automatisches Clipping von Long-Form-Videos in viral-würdige Clips.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Content Creation
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🎬</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Content Creation</h3>\n            <p class="usecase-description">Vervielfältige deine Content-Ausgabe. Konvertiere ein Long-Form-Video in mehrere virale Shorts automatisch.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Video Marketing
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📺</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Video Marketing</h3>\n            <p class="usecase-description">Maximiere die Reichweite deiner Videos. Erstelle mehrere Clips aus einem Video für verschiedene Plattformen.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {OPUS_CLIP_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die AI-basierte Video-Klip-Generierung.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Video Clipping Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Viral-Moment Detection</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Auto-Captions</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Multi-Format Export</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{OPUS_CLIP_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Opus Clip Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Opus Clip Core holen</a>)',
        f'<h2 class="package-title">{OPUS_CLIP_DATA["name"]} Pro</h2>\n        <div class="package-price">ab 19$/Monat</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Auto-Video-Clipping, Viral-Moment Detection, Auto-Captions und Multi-Format Export.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Auto-Video-Clipping</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Viral-Moment Detection</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Auto-Captions</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Multi-Format Export</div>\n        </div>\n        <a href="#" class="btn btn-primary">{OPUS_CLIP_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>AI-basiertes Clipping</strong> – Automatisches Clipping von Long-Form-Videos in Shorts</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Viral-Moment Detection</strong> – Intelligente Erkennung von viral-würdigen Momenten</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Auto-Captions</strong> – Automatische Untertitel-Generierung für alle Clips</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Multi-Format Export</strong> – Exportiere Clips für TikTok, Instagram, YouTube Shorts</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Schnelle Verarbeitung</strong> – Effiziente KI-Engine für optimale Performance</span></li>',
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
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Video-Qualität</strong> – Abhängig von der Qualität der Quellvideos</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Verarbeitungszeit</strong> – Größere Videos benötigen mehr Verarbeitungszeit</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Plattform-Limits</strong> – Export-Limits können bei großen Projekten einschränkend sein</span></li>',
        content
    )
    
    # 8. Comparison
    content = re.sub(
        r'(<h2 class="section-title">Opus Clip vs\. Konkurrenz</h2>)',
        f'<h2 class="section-title">{OPUS_CLIP_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Opus Clip</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{OPUS_CLIP_DATA["name"]}</th><th>Descript</th><th>Runway</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {OPUS_CLIP_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle virale Shorts aus deinen Long-Form-Videos mit AI-basiertem Clipping.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'opus-clip.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
