#!/usr/bin/env python3
"""
Vollständige Anpassung von yapper.html
Alle Sections werden systematisch angepasst für Yapper
"""

import re
import sys

# Yapper Daten aus ki-tech.html
YAPPER_DATA = {
    'name': 'Yapper',
    'badge': 'SOCIAL AUTOMATION',
    'description': 'Social Media Automation für X/Twitter. Auto-Posting, Thread-Generierung und Engagement-Management.',
    'features': [
        {
            'title': 'Auto-Posting',
            'description': 'Automatisches Posting auf X/Twitter. Zeitgesteuerte Posts für optimale Reichweite.',
            'icon': 'send'
        },
        {
            'title': 'Thread-Generierung',
            'description': 'Automatische Thread-Generierung für längere Inhalte. Erstelle Threads mit mehreren Tweets.',
            'icon': 'list'
        },
        {
            'title': 'Engagement Tracking',
            'description': 'Umfassendes Engagement-Tracking für deine Tweets. Analysiere Likes, Retweets und Replies.',
            'icon': 'trending-up'
        },
        {
            'title': 'API Integration',
            'description': 'REST API für einfache Integration in deine Workflows. API-first Design für Automation.',
            'icon': 'code'
        },
        {
            'title': 'Scheduling',
            'description': 'Zeitgesteuerte Posts für optimale Reichweite. Plane deine Tweets im Voraus.',
            'icon': 'clock'
        },
        {
            'title': 'Content Management',
            'description': 'Zentrale Verwaltung deiner Social Media Inhalte. Organisiere und plane deine Posts.',
            'icon': 'file-text'
        }
    ],
    'price': 'LIFETIME DEAL',
    'logo': 'https://cdn.simpleicons.org/twitter/1DA1F2',
    'keywords': 'Yapper, Social Media Automation, Twitter Automation, Auto-Posting, Thread-Generierung, Engagement Management'
}

def adapt_file(file_path):
    """Vollständige Anpassung der yapper.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht Make besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {YAPPER_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Social Media Automation für X/Twitter.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Auto-Posting
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Thread-Generierung
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: Engagement Tracking
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: API Integration
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Scheduling
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Content Management
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{YAPPER_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{YAPPER_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {YAPPER_DATA["name"]}?</h3>
          <p>
            {YAPPER_DATA["name"]} ist eine Social Media Automation-Plattform für X/Twitter. Mit automatischem Posting, Thread-Generierung und Engagement-Management hilft {YAPPER_DATA["name"]} dir, deine Social Media Präsenz zu automatisieren – perfekt für Content-Creator und Social Media Manager.
          </p>
          <p>
            Im Gegensatz zu manuellen Posting-Methoden bietet {YAPPER_DATA["name"]} automatisierte Workflows für deine Tweets. Das macht {YAPPER_DATA["name"]} zur ersten Wahl für alle, die ihre Social Media Präsenz optimieren wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatisches Posting auf X/Twitter
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Thread-Generierung für längere Inhalte
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Engagement-Tracking und Analytics
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Yapper Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {YAPPER_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Social Media Marketing
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📱</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Social Media Marketing</h3>\n            <p class="usecase-description">Automatisiere deine Twitter-Präsenz. Plane Posts im Voraus und maximiere deine Reichweite.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Content Automation
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">🔄</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Content Automation</h3>\n            <p class="usecase-description">Automatische Thread-Generierung für längere Inhalte. Erstelle Threads mit mehreren Tweets automatisch.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Engagement Management
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📈</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Engagement Management</h3>\n            <p class="usecase-description">Verfolge deine Twitter-Metriken. Analysiere Likes, Retweets und Replies für bessere Ergebnisse.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {YAPPER_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die Social Media Automation-Plattform.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Auto-Posting Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Thread-Generierung</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Engagement Tracking</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Scheduling</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{YAPPER_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{YAPPER_DATA["name"]} Lifetime</h2>\n        <div class="package-price">LIFETIME DEAL</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Auto-Posting, Thread-Generierung, Engagement Tracking und API-Zugriff – einmalig zahlen, lebenslang nutzen.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Auto-Posting</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Thread-Generierung</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Engagement Tracking</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>API Integration</div>\n        </div>\n        <a href="#" class="btn btn-primary">{YAPPER_DATA["name"]} Lifetime holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Auto-Posting</strong> – Automatisches Posting auf X/Twitter für optimale Reichweite</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Thread-Generierung</strong> – Automatische Thread-Generierung für längere Inhalte</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Engagement Tracking</strong> – Umfassendes Engagement-Tracking für deine Tweets</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>API Integration</strong> – REST API für einfache Integration in deine Workflows</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Lifetime Deal</strong> – Einmalig zahlen, lebenslang nutzen</span></li>',
        content
    )
    
    # Cons
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Nur X/Twitter</strong> – Fokussiert sich nur auf X/Twitter, keine anderen Plattformen</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>API-Limits</strong> – Twitter API-Limits können bei großen Volumen einschränkend sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Feature-Updates</strong> – Feature-Updates können bei Lifetime-Deals langsamer sein</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Twitter-Policy</strong> – Abhängig von Twitter API-Policies, die sich ändern können</span></li>',
        content
    )
    
    # 8. Comparison
    content = re.sub(
        r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)',
        f'<h2 class="section-title">{YAPPER_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{YAPPER_DATA["name"]}</th><th>Buffer</th><th>Hootsuite</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {YAPPER_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und automatisiere deine Twitter-Präsenz mit Auto-Posting, Thread-Generierung und Engagement-Management.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'yapper.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
