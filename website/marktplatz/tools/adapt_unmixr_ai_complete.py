#!/usr/bin/env python3
"""
Vollständige Anpassung von unmixr-ai.html
Alle Sections werden systematisch angepasst für Unmixr AI
"""

import re
import sys

# Unmixr AI Daten aus ki-tech.html
UNMIXR_AI_DATA = {
    'name': 'Unmixr AI',
    'badge': 'AUDIO AI',
    'description': 'Text-to-Speech, Speech-to-Text und Audio/Video Dubbing. Vollständige Audio-Produktion mit AI.',
    'features': [
        {
            'title': 'Text-to-Speech',
            'description': 'AI-powered Text-to-Speech für natürliche Sprachsynthese. Erstelle Voiceovers für deine Videos.',
            'icon': 'volume-2'
        },
        {
            'title': 'Speech-to-Text',
            'description': 'Automatische Speech-to-Text-Konvertierung. Transkribiere Audio- und Video-Dateien.',
            'icon': 'mic'
        },
        {
            'title': 'Audio/Video Dubbing',
            'description': 'AI-gestütztes Audio/Video Dubbing für verschiedene Sprachen. Lokalisiere deine Inhalte.',
            'icon': 'globe'
        },
        {
            'title': 'Voice Cloning',
            'description': 'Voice Cloning für personalisierte Voiceovers. Erstelle Voice-Duplikate mit KI.',
            'icon': 'user'
        },
        {
            'title': 'Audio Editing',
            'description': 'Integrierte Audio-Bearbeitung für professionelle Ergebnisse. Schneide, bearbeite und optimiere Audio.',
            'icon': 'scissors'
        },
        {
            'title': 'Lifetime Deal',
            'description': 'Lifetime Deal verfügbar. Einmalig zahlen, lebenslang nutzen – keine monatlichen Gebühren.',
            'icon': 'check-circle'
        }
    ],
    'price': 'LIFETIME DEAL',
    'logo': 'https://cdn.simpleicons.org/sound/FF6B6B',
    'keywords': 'Unmixr AI, Text-to-Speech, Speech-to-Text, Audio Dubbing, Voice Cloning, Audio AI'
}

def adapt_file(file_path):
    """Vollständige Anpassung der unmixr-ai.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Unmixr AI besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {UNMIXR_AI_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Audio AI-Plattform.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Text-to-Speech
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Speech-to-Text
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Audio/Video Dubbing
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Voice Cloning
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Audio Editing
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Lifetime Deal
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{UNMIXR_AI_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{UNMIXR_AI_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Unmixr AI\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {UNMIXR_AI_DATA["name"]}?</h3>
          <p>
            {UNMIXR_AI_DATA["name"]} ist eine Audio AI-Plattform für Text-to-Speech, Speech-to-Text und Audio/Video Dubbing. Mit KI-gestützter Audio-Produktion erstellst du professionelle Voiceovers und transkribierst Audio-Inhalte – perfekt für Content-Creator und Video-Produzenten.
          </p>
          <p>
            Im Gegensatz zu traditionellen Audio-Tools bietet {UNMIXR_AI_DATA["name"]} vollständige Audio-Produktion mit AI, inklusive Voice Cloning und Dubbing. Das macht {UNMIXR_AI_DATA["name"]} zur ersten Wahl für alle, die Audio-Inhalte effizienter produzieren wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-powered Text-to-Speech für natürliche Sprachsynthese
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatische Speech-to-Text-Konvertierung für Transkriptionen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-gestütztes Audio/Video Dubbing für verschiedene Sprachen
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Unmixr AI Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {UNMIXR_AI_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Video Voiceovers
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🎬</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Video Voiceovers</h3>\n            <p class="usecase-description">Erstelle professionelle Voiceovers für deine Videos. AI-powered Text-to-Speech für natürliche Sprachsynthese.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Audio Transcription
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📝</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Audio Transcription</h3>\n            <p class="usecase-description">Transkribiere Audio- und Video-Dateien automatisch. Automatische Speech-to-Text-Konvertierung für Podcasts und Videos.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Video Localization
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🌍</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Video Localization</h3>\n            <p class="usecase-description">Lokalisiere deine Videos für verschiedene Märkte. AI-gestütztes Audio/Video Dubbing für verschiedene Sprachen.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {UNMIXR_AI_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die Audio AI-Plattform.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Text-to-Speech Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Speech-to-Text</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Audio/Video Dubbing</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Voice Cloning</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{UNMIXR_AI_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{UNMIXR_AI_DATA["name"]} Lifetime</h2>\n        <div class="package-price">LIFETIME DEAL</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Text-to-Speech, Speech-to-Text, Audio/Video Dubbing und Voice Cloning – einmalig zahlen, lebenslang nutzen.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Text-to-Speech</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Speech-to-Text</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Audio/Video Dubbing</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Voice Cloning</div>\n        </div>\n        <a href="#" class="btn btn-primary">{UNMIXR_AI_DATA["name"]} Lifetime holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Text-to-Speech</strong> – AI-powered Text-to-Speech für natürliche Sprachsynthese</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Speech-to-Text</strong> – Automatische Speech-to-Text-Konvertierung für Transkriptionen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Audio/Video Dubbing</strong> – AI-gestütztes Dubbing für verschiedene Sprachen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Voice Cloning</strong> – Voice Cloning für personalisierte Voiceovers</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Lifetime Deal</strong> – Einmalig zahlen, lebenslang nutzen – keine monatlichen Gebühren</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Voice-Qualität</strong> – Abhängig von der Qualität der Quell-Audios</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Verarbeitungszeit</strong> – Größere Audio-Dateien benötigen mehr Verarbeitungszeit</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Feature-Updates</strong> – Feature-Updates können bei Lifetime-Deals langsamer sein</span></li>',
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
        f'<h2 class="section-title">{UNMIXR_AI_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{UNMIXR_AI_DATA["name"]}</th><th>ElevenLabs</th><th>PlayHT</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {UNMIXR_AI_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle professionelle Audio-Inhalte mit Text-to-Speech, Speech-to-Text und Audio/Video Dubbing.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'unmixr-ai.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
