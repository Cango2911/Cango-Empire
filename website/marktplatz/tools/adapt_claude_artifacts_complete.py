#!/usr/bin/env python3
"""
Vollständige Anpassung von claude-artifacts.html
Alle Sections werden systematisch angepasst für Claude Artifacts
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Claude Artifacts Daten aus ki-tech.html
CLAUDE_ARTIFACTS_DATA = {
    'name': 'Claude Artifacts',
    'badge': 'CODE GEN',
    'description': 'Interaktive Code-Generierung in Claude. Live-Preview von HTML, React und Python-Code direkt im Chat.',
    'features': [
        {
            'title': 'Live Code-Preview',
            'description': 'Live-Preview von generiertem Code direkt im Chat. Sieh sofort die Ergebnisse deines Codes.',
            'icon': 'monitor'
        },
        {
            'title': 'Multi-Language Support',
            'description': 'Unterstützung für verschiedene Programmiersprachen. HTML, React, Python, JavaScript und mehr.',
            'icon': 'code'
        },
        {
            'title': 'Iterative Editing',
            'description': 'Iteratives Bearbeiten von Code mit direktem Feedback. Passe deinen Code schrittweise an.',
            'icon': 'edit'
        },
        {
            'title': 'Export-Funktionen',
            'description': 'Exportiere deinen generierten Code. Speichere HTML, React und Python-Dateien direkt.',
            'icon': 'download'
        },
        {
            'title': 'Context Awareness',
            'description': 'Kontextbewusste Code-Generierung. Verstehe Zusammenhänge für bessere Ergebnisse.',
            'icon': 'brain'
        },
        {
            'title': 'Claude Pro',
            'description': 'Inklusive in Claude Pro. Nutze alle Features mit deinem Claude Pro Abonnement.',
            'icon': 'check-circle'
        }
    ],
    'price': 'Inkl. Claude Pro',
    'logo': 'https://cdn.simpleicons.org/anthropic/FF6B6B',
    'keywords': 'Claude Artifacts, Code Generation, Live Preview, Code Editor, Claude Pro, AI Code'
}

def adapt_file(file_path):
    """Vollständige Anpassung der claude-artifacts.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section - Titel und Subtitle anpassen, aber Platzhalter behalten
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{CLAUDE_ARTIFACTS_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {CLAUDE_ARTIFACTS_DATA["name"]} interaktive Code-Generierung mit Live-Preview nutzt.</p>',
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
        r'(<h2 class="section-title">Was macht Claude Artifacts besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {CLAUDE_ARTIFACTS_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der interaktiven Code-Generierung mit Live-Preview.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Live Code-Preview
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Multi-Language Support
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Iterative Editing
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Export-Funktionen
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Context Awareness
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44L2 22v-1.5A2.5 2.5 0 0 1 4.5 18h1.5"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44L22 22v-1.5A2.5 2.5 0 0 0 19.5 18H18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Claude Pro
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{CLAUDE_ARTIFACTS_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{CLAUDE_ARTIFACTS_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {CLAUDE_ARTIFACTS_DATA["name"]}?</h3>
          <p>
            {CLAUDE_ARTIFACTS_DATA["name"]} ist eine interaktive Code-Generierungs-Funktion in Claude. Mit Live-Preview von generiertem Code siehst du sofort die Ergebnisse deines Codes – perfekt für Entwickler und Programmierer.
          </p>
          <p>
            Im Gegensatz zu statischen Code-Generatoren bietet {CLAUDE_ARTIFACTS_DATA["name"]} Live-Preview und iteratives Bearbeiten für bessere Ergebnisse. Das macht {CLAUDE_ARTIFACTS_DATA["name"]} zur ersten Wahl für alle, die Code effizienter generieren wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Live-Preview von generiertem Code direkt im Chat
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Unterstützung für verschiedene Programmiersprachen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Iteratives Bearbeiten von Code mit direktem Feedback
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Claude Artifacts Interface</span>',
        content
    )
    
    # 4. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {CLAUDE_ARTIFACTS_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Web Development
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">💻</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Web Development</h3>\n            <p class="usecase-description">Erstelle Web-Anwendungen mit Live-Preview. HTML, React und JavaScript direkt im Chat generieren und testen.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Prototyping
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🎨</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Prototyping</h3>\n            <p class="usecase-description">Erstelle Prototypen schnell mit iterativem Bearbeiten. Teste deine Ideen direkt im Chat mit Live-Preview.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Code Learning
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📚</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Code Learning</h3>\n            <p class="usecase-description">Lerne Programmieren mit Live-Preview. Sieh sofort die Ergebnisse deines Codes und verstehe Zusammenhänge besser.</p>\n          </div>\n        </div>',
        content
    )
    
    # 5. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {CLAUDE_ARTIFACTS_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die interaktive Code-Generierung mit Live-Preview.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Code Editor Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Live Code-Preview</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Multi-Language Support</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Export-Funktionen</div>', content)
    
    # 6. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{CLAUDE_ARTIFACTS_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 7. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">Claude Pro</h2>\n        <div class="package-price">Inkl. Claude Pro</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Live Code-Preview, Multi-Language Support, Iterative Editing und Export-Funktionen – inklusive in Claude Pro.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Live Code-Preview</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Multi-Language Support</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Iterative Editing</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Export-Funktionen</div>\n        </div>\n        <a href="#" class="btn btn-primary">Claude Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 8. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Live Code-Preview</strong> – Sieh sofort die Ergebnisse deines Codes direkt im Chat</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Multi-Language Support</strong> – Unterstützung für verschiedene Programmiersprachen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Iterative Editing</strong> – Iteratives Bearbeiten von Code mit direktem Feedback</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Export-Funktionen</strong> – Exportiere deinen generierten Code direkt</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Claude Pro</strong> – Inklusive in Claude Pro, nutze alle Features</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Claude Pro erforderlich</strong> – Benötigt Claude Pro Abonnement</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Komplexität</strong> – Komplexe Projekte können herausfordernd sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Feature-Limits</strong> – Einige Features nur in Claude Pro verfügbar</span></li>',
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
        f'<h2 class="section-title">{CLAUDE_ARTIFACTS_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{CLAUDE_ARTIFACTS_DATA["name"]}</th><th>GitHub Copilot</th><th>Cursor</th></tr>',
        content
    )
    
    # 10. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {CLAUDE_ARTIFACTS_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und nutze interaktive Code-Generierung mit Live-Preview, Multi-Language Support und iterativem Bearbeiten.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'claude-artifacts.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
