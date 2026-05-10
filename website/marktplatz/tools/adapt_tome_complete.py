#!/usr/bin/env python3
"""
Vollständige Anpassung von tome.html
Alle Sections werden systematisch angepasst für Tome
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Tome Daten aus ki-tech.html
TOME_DATA = {
    'name': 'Tome',
    'badge': 'STORYTELLING',
    'description': 'AI-Powered Storytelling-Plattform. Interaktive Präsentationen mit automatischer Bild-Generierung.',
    'features': [
        {'title': 'AI-Content-Generierung', 'description': 'AI-Content-Generierung für interaktive Präsentationen. Erstelle Storytelling-Präsentationen automatisch.', 'icon': 'sparkles'},
        {'title': 'Auto-Bilder', 'description': 'Automatische Bild-Generierung für deine Präsentationen. Professionelle Bilder ohne manuelle Suche.', 'icon': 'image'},
        {'title': 'Interaktive Elemente', 'description': 'Interaktive Elemente für engagierende Präsentationen. Embed Videos, Links und mehr.', 'icon': 'layers'},
        {'title': 'Sharing & Analytics', 'description': 'Teile deine Präsentationen und verfolge Analytics. Sieh, wie deine Präsentationen performen.', 'icon': 'share'},
        {'title': 'Custom Branding', 'description': 'Custom Branding für deine Marke. Passe Farben, Fonts und Styles an deine Brand an.', 'icon': 'palette'},
        {'title': 'Freemium / Pro', 'description': 'Kostenlose Version verfügbar, Pro-Version mit erweiterten Features. Perfekt für Einsteiger und Profis.', 'icon': 'check-circle'}
    ],
    'price': 'Kostenlos / Pro',
    'logo': 'https://cdn.simpleicons.org/storytelling/FF6B6B',
    'keywords': 'Tome, Storytelling, AI Präsentationen, Interactive Presentations, Auto-Bilder, Content Generation'
}

def adapt_file(file_path):
    """Vollständige Anpassung der tome.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{TOME_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {TOME_DATA["name"]} AI-Powered Storytelling-Präsentationen mit automatischer Bild-Generierung erstellst.</p>',
        content
    )
    content = re.sub(r'(<p>Klicken um Video zu laden</p>|<p>Video wird später integriert</p>)', '<p>Video wird später integriert</p>', content)
    
    # 2. Features Section
    content = re.sub(
        r'(<h2 class="section-title">Was macht [^<]+ besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {TOME_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der AI-Powered Storytelling-Plattform.</p>',
        content
    )
    
    # Features - vereinfachte Anpassung
    content = re.sub(r'(<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][0]["description"]}</p>', content, count=1)
    content = re.sub(r'(<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][1]["description"]}</p>', content, count=1)
    content = re.sub(r'(<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][2]["description"]}</p>', content, count=1)
    content = re.sub(r'(<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][3]["description"]}</p>', content, count=1)
    content = re.sub(r'(<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][4]["description"]}</p>', content, count=1)
    content = re.sub(r'(<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>)', f'<h3 class="feature-title">{TOME_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{TOME_DATA["features"][5]["description"]}</p>', content, count=1)
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {TOME_DATA["name"]}?</h3>
          <p>
            {TOME_DATA["name"]} ist eine AI-Powered Storytelling-Plattform für interaktive Präsentationen. Mit automatischer Bild-Generierung und AI-Content-Generierung erstellst du engagierende Präsentationen – perfekt für Storytelling und Präsentationen.
          </p>
          <p>
            Im Gegensatz zu traditionellen Präsentationstools verwendet {TOME_DATA["name"]} KI für automatische Bild-Generierung und Content-Generierung. Das macht {TOME_DATA["name"]} zur ersten Wahl für alle, die schnell engagierende Präsentationen erstellen wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-Content-Generierung für interaktive Präsentationen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatische Bild-Generierung für deine Präsentationen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Interaktive Elemente für engagierende Präsentationen
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    content = re.sub(r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)', '<span>Screenshot: Tome Dashboard</span>', content)
    
    # 4. Use Cases
    content = re.sub(r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)', f'<h2 class="section-title">Wofür kann ich {TOME_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>', content)
    content = re.sub(r'(<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>)', '<h3 class="usecase-title">Storytelling Presentations</h3>\n            <p class="usecase-description">Erstelle Storytelling-Präsentationen mit AI-Content-Generierung und automatischer Bild-Generierung. Engagierende Präsentationen ohne manuelle Arbeit.</p>', content, count=1)
    content = re.sub(r'(<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>)', '<h3 class="usecase-title">Interactive Presentations</h3>\n            <p class="usecase-description">Erstelle interaktive Präsentationen mit Embed-Videos und Links. Teilen und verfolge Analytics für deine Präsentationen.</p>', content, count=1)
    content = re.sub(r'(<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>)', '<h3 class="usecase-title">Marketing Presentations</h3>\n            <p class="usecase-description">Erstelle Marketing-Präsentationen mit Custom Branding. Professionelle Präsentationen für deine Marke.</p>', content, count=1)
    
    # 5. Gallery
    content = re.sub(r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)', f'<h2 class="section-title">So sieht {TOME_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die AI-Powered Storytelling-Plattform.</p>', content)
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Storytelling Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">AI-Content-Generierung</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Auto-Bilder</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Interaktive Elemente</div>', content)
    
    # 6-10. Pricing, Package, Pros/Cons, Comparison, CTA
    content = re.sub(r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)', f'<h2 class="section-title">{TOME_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>', content)
    content = re.sub(r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>.*?<a href="#" class="btn btn-primary">Make Core holen</a>)', f'<h2 class="package-title">{TOME_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. AI-Content-Generierung, Auto-Bilder, Interaktive Elemente und Sharing & Analytics.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>AI-Content-Generierung</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Auto-Bilder</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Interaktive Elemente</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Sharing & Analytics</div>\n        </div>\n        <a href="#" class="btn btn-primary">{TOME_DATA["name"]} Pro holen</a>', content, flags=re.DOTALL)
    
    # Pros & Cons
    content = re.sub(r'(<span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span>)', f'<span><strong>AI-Content-Generierung</strong> – AI-Content-Generierung für interaktive Präsentationen</span>', content, count=1)
    content = re.sub(r'(<span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span>)', f'<span><strong>Auto-Bilder</strong> – Automatische Bild-Generierung für deine Präsentationen</span>', content, count=1)
    content = re.sub(r'(<span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span>)', f'<span><strong>Interaktive Elemente</strong> – Interaktive Elemente für engagierende Präsentationen</span>', content, count=1)
    content = re.sub(r'(<span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span>)', f'<span><strong>Sharing & Analytics</strong> – Teile deine Präsentationen und verfolge Analytics</span>', content, count=1)
    content = re.sub(r'(<span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span>)', f'<span><strong>Freemium / Pro</strong> – Kostenlose Version verfügbar, Pro-Version mit erweiterten Features</span>', content, count=1)
    
    content = re.sub(r'(<span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span>)', f'<span><strong>Feature-Limits</strong> – Einige Features nur in Pro-Version verfügbar</span>', content, count=1)
    content = re.sub(r'(<span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span>)', f'<span><strong>Design-Limits</strong> – Design-Optionen können bei freien Plänen einschränkend sein</span>', content, count=1)
    content = re.sub(r'(<span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span>)', f'<span><strong>Customization</strong> – Customization-Optionen können bei freien Plänen einschränkend sein</span>', content, count=1)
    content = re.sub(r'(<span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span>)', f'<span><strong>Dokumentation</strong> – Dokumentation könnte ausführlicher sein</span>', content, count=1)
    
    # Comparison & CTA
    content = re.sub(r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)', f'<h2 class="section-title">{TOME_DATA["name"]} vs. Konkurrenz</h2>', content)
    content = re.sub(r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)', f'<tr><th>Feature</th><th>{TOME_DATA["name"]}</th><th>Prezi</th><th>Gamma</th></tr>', content)
    content = re.sub(r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)', f'<h2 class="cta-title">Bereit für {TOME_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle AI-Powered Storytelling-Präsentationen mit automatischer Bild-Generierung und interaktiven Elementen.</p>', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'tome.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
