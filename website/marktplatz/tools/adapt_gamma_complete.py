#!/usr/bin/env python3
"""
Vollständige Anpassung von gamma.html
Alle Sections werden systematisch angepasst für Gamma
Video-Bereich bleibt erkennbar als Platzhalter
"""

import re
import sys

# Gamma Daten aus ki-tech.html
GAMMA_DATA = {
    'name': 'Gamma',
    'badge': 'PRESENTATION',
    'description': 'AI-generierte Präsentationen und Dokumente. Von der Idee zum fertigen Design in Sekunden.',
    'features': [
        {
            'title': 'AI-Präsentationen',
            'description': 'AI-generierte Präsentationen von der Idee zum fertigen Design. Erstelle professionelle Präsentationen in Sekunden.',
            'icon': 'presentation'
        },
        {
            'title': 'Auto-Design',
            'description': 'Automatisches Design für deine Präsentationen. Professionelle Layouts ohne manuelle Arbeit.',
            'icon': 'palette'
        },
        {
            'title': 'Export als PDF/PPT',
            'description': 'Exportiere deine Präsentationen als PDF oder PowerPoint. Perfekt für Präsentationen und Dokumente.',
            'icon': 'download'
        },
        {
            'title': 'Team-Kollaboration',
            'description': 'Team-Kollaboration für gemeinsame Arbeit. Arbeite mit deinem Team an Präsentationen.',
            'icon': 'users'
        },
        {
            'title': 'Custom Branding',
            'description': 'Custom Branding für deine Marke. Passe Farben, Fonts und Styles an deine Brand an.',
            'icon': 'palette'
        },
        {
            'title': 'Freemium / Pro',
            'description': 'Kostenlose Version verfügbar, Pro-Version mit erweiterten Features. Perfekt für Einsteiger und Profis.',
            'icon': 'check-circle'
        }
    ],
    'price': 'Kostenlos / Pro',
    'logo': 'https://cdn.simpleicons.org/presentation/FF6B6B',
    'keywords': 'Gamma, AI Präsentationen, Presentation AI, Auto-Design, Presentation Tool, AI Slides'
}

def adapt_file(file_path):
    """Vollständige Anpassung der gamma.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Video Section - Titel und Subtitle anpassen, aber Platzhalter behalten
    content = re.sub(
        r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
        f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{GAMMA_DATA["name"]} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {GAMMA_DATA["name"]} AI-generierte Präsentationen und Dokumente in Sekunden erstellst.</p>',
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
        r'(<h2 class="section-title">Was macht Gamma besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {GAMMA_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der AI-generierten Präsentationen und Dokumente.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards (vereinfachte Regex-Patterns)
    # Feature 1: AI-Präsentationen
    content = re.sub(
        r'(<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][0]["description"]}</p>',
        content,
        count=1
    )
    
    # Feature 2: Auto-Design
    content = re.sub(
        r'(<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][1]["description"]}</p>',
        content,
        count=1
    )
    
    # Feature 3: Export als PDF/PPT
    content = re.sub(
        r'(<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][2]["description"]}</p>',
        content,
        count=1
    )
    
    # Feature 4: Team-Kollaboration
    content = re.sub(
        r'(<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][3]["description"]}</p>',
        content,
        count=1
    )
    
    # Feature 5: Custom Branding
    content = re.sub(
        r'(<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][4]["description"]}</p>',
        content,
        count=1
    )
    
    # Feature 6: Freemium / Pro
    content = re.sub(
        r'(<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>)',
        f'<h3 class="feature-title">{GAMMA_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{GAMMA_DATA["features"][5]["description"]}</p>',
        content,
        count=1
    )
    
    # 3. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {GAMMA_DATA["name"]}?</h3>
          <p>
            {GAMMA_DATA["name"]} ist eine AI-generierte Präsentations-Plattform für Präsentationen und Dokumente. Mit automatischem Design und AI-generierten Inhalten erstellst du professionelle Präsentationen in Sekunden – perfekt für Geschäftspräsentationen und Dokumente.
          </p>
          <p>
            Im Gegensatz zu traditionellen Präsentationstools verwendet {GAMMA_DATA["name"]} KI, um automatisch Designs und Inhalte zu generieren. Das macht {GAMMA_DATA["name"]} zur ersten Wahl für alle, die schnell professionelle Präsentationen erstellen wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-generierte Präsentationen von der Idee zum fertigen Design
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatisches Design für deine Präsentationen
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Export als PDF oder PowerPoint
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: Gamma Dashboard</span>',
        content
    )
    
    # 4. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {GAMMA_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Business Presentations
    content = re.sub(
        r'(<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>)',
        '<h3 class="usecase-title">Business Presentations</h3>\n            <p class="usecase-description">Erstelle professionelle Geschäftspräsentationen in Sekunden. AI-generierte Inhalte und automatisches Design für maximale Effizienz.</p>',
        content,
        count=1
    )
    
    # Use Case 2: Pitch Decks
    content = re.sub(
        r'(<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>)',
        '<h3 class="usecase-title">Pitch Decks</h3>\n            <p class="usecase-description">Erstelle Pitch Decks für Investoren mit AI-generierten Inhalten. Professionelle Präsentationen ohne manuelle Arbeit.</p>',
        content,
        count=1
    )
    
    # Use Case 3: Marketing Materials
    content = re.sub(
        r'(<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>)',
        '<h3 class="usecase-title">Marketing Materials</h3>\n            <p class="usecase-description">Erstelle Marketing-Materialien und Dokumente mit automatischem Design. Export als PDF oder PowerPoint für Präsentationen.</p>',
        content,
        count=1
    )
    
    # 5. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {GAMMA_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die AI-generierte Präsentations-Plattform.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Presentation Editor</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">AI-Präsentationen</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">Auto-Design</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Export Options</div>', content)
    
    # 6. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{GAMMA_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 7. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{GAMMA_DATA["name"]} Pro</h2>\n        <div class="package-price">Pro Plan</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. AI-Präsentationen, Auto-Design, Export als PDF/PPT und Team-Kollaboration.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>AI-Präsentationen</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Auto-Design</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Export als PDF/PPT</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Team-Kollaboration</div>\n        </div>\n        <a href="#" class="btn btn-primary">{GAMMA_DATA["name"]} Pro holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 8. Pros & Cons
    # Pros
    content = re.sub(
        r'(<span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span>)',
        f'<span><strong>AI-Präsentationen</strong> – AI-generierte Präsentationen von der Idee zum fertigen Design</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span>)',
        f'<span><strong>Auto-Design</strong> – Automatisches Design für deine Präsentationen</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span>)',
        f'<span><strong>Export als PDF/PPT</strong> – Exportiere deine Präsentationen als PDF oder PowerPoint</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span>)',
        f'<span><strong>Team-Kollaboration</strong> – Team-Kollaboration für gemeinsame Arbeit</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Data Stores</strong> – Daten zwischen Ausführungen speichern</span>)',
        f'<span><strong>Freemium / Pro</strong> – Kostenlose Version verfügbar, Pro-Version mit erweiterten Features</span>',
        content,
        count=1
    )
    
    # Cons
    content = re.sub(
        r'(<span><strong>Steilere Lernkurve</strong> – Komplexer als Zapier für Einsteiger</span>)',
        f'<span><strong>Design-Limits</strong> – Einige Design-Optionen nur in Pro-Version verfügbar</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span>)',
        f'<span><strong>Feature-Limits</strong> – Einige Features nur in Pro-Version verfügbar</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Interface manchmal überladen</strong> – Kann bei großen Workflows unübersichtlich werden</span>)',
        f'<span><strong>Customization</strong> – Customization-Optionen können bei freien Plänen einschränkend sein</span>',
        content,
        count=1
    )
    content = re.sub(
        r'(<span><strong>Support langsam</strong> – Antwortzeiten könnten besser sein</span>)',
        f'<span><strong>Dokumentation</strong> – Dokumentation könnte ausführlicher sein</span>',
        content,
        count=1
    )
    
    # 9. Comparison
    content = re.sub(
        r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)',
        f'<h2 class="section-title">{GAMMA_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{GAMMA_DATA["name"]}</th><th>PowerPoint</th><th>Prezi</th></tr>',
        content
    )
    
    # 10. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {GAMMA_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und erstelle AI-generierte Präsentationen und Dokumente mit automatischem Design in Sekunden.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'gamma.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
