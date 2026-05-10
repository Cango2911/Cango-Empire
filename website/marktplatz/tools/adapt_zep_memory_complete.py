#!/usr/bin/env python3
"""
Vollständige Anpassung von zep-memory.html
Alle Sections werden systematisch angepasst für ZEP Memory
"""

import re
import sys

# ZEP Memory Daten aus ki-tech.html
ZEP_DATA = {
    'name': 'ZEP Memory',
    'badge': 'MEMORY API',
    'description': 'Langzeit-Memory für AI-Agents. Kontextuelle Erinnerungen für Chatbots und Conversational AI.',
    'features': [
        {
            'title': 'Long-term Memory',
            'description': 'Langzeit-Memory für AI-Agents. Kontextuelle Erinnerungen über mehrere Sessions hinweg.',
            'icon': 'brain'
        },
        {
            'title': 'Context Management',
            'description': 'Intelligentes Context Management für Chatbots und Conversational AI. Behalte den Überblick über Gesprächsverläufe.',
            'icon': 'layers'
        },
        {
            'title': 'Session Handling',
            'description': 'Effizientes Session Handling für nahtlose Gesprächsfortführung. Session-basierte Memory-Verwaltung.',
            'icon': 'users'
        },
        {
            'title': 'API verfügbar',
            'description': 'REST API für einfache Integration in deine AI-Anwendungen. API-first Design für Automation.',
            'icon': 'code'
        },
        {
            'title': 'Kontextuelle Erinnerungen',
            'description': 'Intelligente, kontextuelle Erinnerungen für Chatbots. Verbessere die Gesprächsqualität mit Langzeit-Memory.',
            'icon': 'message-circle'
        },
        {
            'title': 'Schnelle Performance',
            'description': 'Optimierte Performance für große Datenmengen. Skalierbare Memory-Infrastruktur.',
            'icon': 'zap'
        }
    ],
    'price': 'Kostenlos / Pro',
    'logo': 'https://cdn.simpleicons.org/zep/FF6B6B',
    'keywords': 'ZEP Memory, Memory API, AI Agents, Chatbots, Conversational AI, Long-term Memory, Context Management, Session Handling'
}

def adapt_file(file_path):
    """Vollständige Anpassung der zep-memory.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Header
    features_header_pattern = r'(<h2 class="section-title">Was macht Make besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)'
    features_header_replacement = f'<h2 class="section-title">Was macht {ZEP_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Memory API für AI-Agents.</p>'
    content = re.sub(features_header_pattern, features_header_replacement, content)
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Long-term Memory
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44L2 22v-1.5A2.5 2.5 0 0 1 4.5 18h1.5"/>\n              <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44L22 22v-1.5A2.5 2.5 0 0 0 19.5 18H18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Context Management
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Session Handling
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: API verfügbar
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Kontextuelle Erinnerungen
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Schnelle Performance
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{ZEP_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{ZEP_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {ZEP_DATA["name"]}?</h3>
          <p>
            {ZEP_DATA["name"]} ist eine Memory API für AI-Agents. Mit Langzeit-Memory ermöglicht {ZEP_DATA["name"]} kontextuelle Erinnerungen für Chatbots und Conversational AI – perfekt für intelligente Gesprächsführung.
          </p>
          <p>
            Im Gegensatz zu statischen Memory-Lösungen bietet {ZEP_DATA["name"]} intelligentes Context Management über mehrere Sessions hinweg. Das macht {ZEP_DATA["name"]} zur ersten Wahl für Entwickler von Chatbots und Conversational AI-Anwendungen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Langzeit-Memory für AI-Agents über mehrere Sessions
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Intelligentes Context Management für Chatbots
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              REST API für einfache Integration in AI-Anwendungen
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>)',
        '<span>Screenshot: ZEP Memory Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {ZEP_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Chatbots
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🤖</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Chatbots</h3>\n            <p class="usecase-description">Intelligente Chatbots mit Langzeit-Memory. Verbessere die Gesprächsqualität mit kontextuellen Erinnerungen.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Conversational AI
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">💬</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Conversational AI</h3>\n            <p class="usecase-description">Conversational AI-Anwendungen mit Context Management. Nahtlose Gesprächsfortführung über mehrere Sessions.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: AI Agents
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🧠</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">AI Agents</h3>\n            <p class="usecase-description">AI Agents mit Langzeit-Memory. Ermögliche deinen Agents, sich an vorherige Interaktionen zu erinnern.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {ZEP_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die Memory API und Context Management.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Memory Dashboard</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Context Management</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Session Handling</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">API Integration</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{ZEP_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # Pricing wird generisch gelassen, da "Kostenlos / Pro" nicht genug Details gibt
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{ZEP_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Langzeit-Memory, Context Management, Session Handling und API-Zugriff.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Langzeit-Memory</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Context Management</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Session Handling</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>REST API</div>\n        </div>\n        <a href="#" class="btn btn-primary">{ZEP_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    content = re.sub(
        r'(<h2 class="section-title">Vor- und Nachteile</h2>\s*<p class="section-subtitle">Eine ehrliche Einschätzung von Make\.</p>)',
        f'<h2 class="section-title">Vor- und Nachteile</h2>\n        <p class="section-subtitle">Eine ehrliche Einschätzung von {ZEP_DATA["name"]}.</p>',
        content
    )
    
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Langzeit-Memory</strong> – Kontextuelle Erinnerungen über mehrere Sessions</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Context Management</strong> – Intelligentes Context Management für Chatbots</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Session Handling</strong> – Effizientes Session Handling für nahtlose Gesprächsfortführung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>REST API</strong> – API-first Design für einfache Integration</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Skalierbare Infrastruktur</strong> – Optimierte Performance für große Datenmengen</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>API-first</strong> – Benötigt technische Kenntnisse für Integration</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Speicher-Limits</strong> – Memory-Limits können bei großen Projekten einschränkend sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Preis steigt schnell</strong> – Höhere Preise für größere Volumen</span></li>',
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
        f'<h2 class="section-title">{ZEP_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{ZEP_DATA["name"]}</th><th>Pinecone</th><th>LangChain Memory</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {ZEP_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und verbessere deine Chatbots mit Langzeit-Memory und Context Management.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'zep-memory.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
