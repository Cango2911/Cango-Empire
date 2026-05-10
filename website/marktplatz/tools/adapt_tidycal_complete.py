#!/usr/bin/env python3
"""
Vollständige Anpassung von tidycal.html
Alle Sections werden systematisch angepasst für TidyCal
"""

import re
import sys

# TidyCal Daten aus ki-tech.html
TIDYCAL_DATA = {
    'name': 'TidyCal',
    'badge': 'SCHEDULING',
    'description': 'Meeting-Scheduling mit AI. Automatisiertes Kalender-Management und Terminbuchung.',
    'features': [
        {
            'title': 'Meeting-Scheduling',
            'description': 'Automatisiertes Meeting-Scheduling für optimale Terminbuchung. AI-gestütztes Kalender-Management.',
            'icon': 'calendar'
        },
        {
            'title': 'Calendar-Sync',
            'description': 'Nahtlose Synchronisation mit Google Calendar, Outlook und anderen Kalendern. Automatische Updates.',
            'icon': 'refresh-cw'
        },
        {
            'title': 'AI-Optimierung',
            'description': 'AI-gestützte Termin-Optimierung für bessere Verfügbarkeit. Intelligente Slot-Vorschläge.',
            'icon': 'sparkles'
        },
        {
            'title': 'Booking Links',
            'description': 'Personalisierte Booking-Links für deine Kunden. Einfache Terminbuchung ohne Back-and-Forth.',
            'icon': 'link'
        },
        {
            'title': 'Reminders',
            'description': 'Automatische Erinnerungen für Meetings und Termine. Verpasse nie wieder einen Termin.',
            'icon': 'bell'
        },
        {
            'title': 'Lifetime Deal',
            'description': 'Lifetime Deal verfügbar. Einmalig zahlen, lebenslang nutzen – keine monatlichen Gebühren.',
            'icon': 'check-circle'
        }
    ],
    'price': 'LIFETIME DEAL',
    'logo': 'https://cdn.simpleicons.org/calendar/FF6B6B',
    'keywords': 'TidyCal, Meeting Scheduling, Calendar Management, AI Scheduling, Terminbuchung, Lifetime Deal'
}

def adapt_file(file_path):
    """Vollständige Anpassung der tidycal.html Datei"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Features Section - Subtitle
    content = re.sub(
        r'(<h2 class="section-title">Was macht TidyCal besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
        f'<h2 class="section-title">Was macht {TIDYCAL_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Meeting-Scheduling-Plattform mit AI.</p>',
        content
    )
    
    # Features Grid - alle 6 Feature Cards
    # Feature 1: Meeting-Scheduling
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4\.93 4\.93l2\.83 2\.83M16\.24 16\.24l2\.83 2\.83M2 12h4M18 12h4M4\.93 19\.07l2\.83-2\.83M16\.24 7\.76l2\.83-2\.83"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Visueller Editor</h3>\s*<p class="feature-description">Drag-and-Drop Interface für komplexe Workflows\. Keine Programmierkenntnisse nötig\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][0]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][0]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 2: Calendar-Sync
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">1000\+ Apps</h3>\s*<p class="feature-description">Verbinde Google, Slack, Shopify, Notion und hunderte weitere Apps\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][1]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][1]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 3: AI-Optimierung
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M14\.7 6\.3a1 1 0 0 0 0 1\.4l1\.6 1\.6a1 1 0 0 0 1\.4 0l3\.77-3\.77a6 6 0 0 1-7\.94 7\.94l-6\.91 6\.91a2\.12 2\.12 0 0 1-3-3l6\.91-6\.91a6 6 0 0 1 7\.94-7\.94l-3\.76 3\.76z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">HTTP/API Module</h3>\s*<p class="feature-description">Verbinde jede API – auch ohne native Integration\. Volle Flexibilität\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][2]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][2]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 4: Booking Links
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Router & Filter</h3>\s*<p class="feature-description">Verzweige Workflows mit Bedingungen\. Komplexe Logik leicht umgesetzt\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][3]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][3]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 5: Reminders
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Scheduling</h3>\s*<p class="feature-description">Zeitgesteuerte Ausführung: Minütlich, stündlich, täglich oder nach Plan\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][4]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][4]["description"]}</p>\n        </div>',
        content
    )
    
    # Feature 6: Lifetime Deal
    content = re.sub(
        r'(<div class="feature-card">\s*<div class="feature-icon">\s*<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\s*<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\s*</svg>\s*</div>\s*<h3 class="feature-title">Error Handling</h3>\s*<p class="feature-description">Robuste Fehlerbehandlung mit automatischen Retries und Benachrichtigungen\.</p>\s*</div>)',
        f'<div class="feature-card">\n          <div class="feature-icon">\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>\n            </svg>\n          </div>\n          <h3 class="feature-title">{TIDYCAL_DATA["features"][5]["title"]}</h3>\n          <p class="feature-description">{TIDYCAL_DATA["features"][5]["description"]}</p>\n        </div>',
        content
    )
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist TidyCal\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
    overview_replacement = f'''<h3>Was ist {TIDYCAL_DATA["name"]}?</h3>
          <p>
            {TIDYCAL_DATA["name"]} ist eine Meeting-Scheduling-Plattform mit AI. Mit automatisiertem Kalender-Management und Terminbuchung hilft {TIDYCAL_DATA["name"]} dir, deine Termine effizienter zu verwalten – perfekt für Freelancer und Unternehmen.
          </p>
          <p>
            Im Gegensatz zu traditionellen Kalender-Apps bietet {TIDYCAL_DATA["name"]} AI-gestützte Termin-Optimierung für bessere Verfügbarkeit. Das macht {TIDYCAL_DATA["name"]} zur ersten Wahl für alle, die ihre Terminbuchung automatisieren wollen.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Automatisiertes Meeting-Scheduling für optimale Terminbuchung
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Nahtlose Synchronisation mit Google Calendar, Outlook und anderen Kalendern
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              AI-gestützte Termin-Optimierung für bessere Verfügbarkeit
            </li>
          </ul>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # Overview Image Caption
    content = re.sub(
        r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)',
        '<span>Screenshot: TidyCal Dashboard</span>',
        content
    )
    
    # 3. Use Cases Section
    content = re.sub(
        r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
        f'<h2 class="section-title">Wofür kann ich {TIDYCAL_DATA["name"]} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
        content
    )
    
    # Use Case 1: Client Scheduling
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📧</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Lead-Automatisierung</h3>\s*<p class="usecase-description">Neue Leads automatisch in CRM übertragen, E-Mails senden und in Slack benachrichtigen\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">👥</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Client Scheduling</h3>\n            <p class="usecase-description">Automatisiere die Terminbuchung mit deinen Kunden. AI-gestütztes Meeting-Scheduling für optimale Verfügbarkeit.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 2: Team Management
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">🛒</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">E-Commerce Workflows</h3>\s*<p class="usecase-description">Bestellungen synchronisieren, Lagerbestände aktualisieren, Tracking-Infos versenden\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">👔</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Team Management</h3>\n            <p class="usecase-description">Verwalte Team-Termine effizient. Kalender-Sync für nahtlose Zusammenarbeit.</p>\n          </div>\n        </div>',
        content
    )
    
    # Use Case 3: Appointment Booking
    content = re.sub(
        r'(<div class="usecase-card">\s*<div class="usecase-image"><span class="usecase-icon">📊</span></div>\s*<div class="usecase-content">\s*<h3 class="usecase-title">Reporting & Dashboards</h3>\s*<p class="usecase-description">Daten aus verschiedenen Quellen sammeln, aufbereiten und in Google Sheets/Airtable speichern\.</p>\s*</div>\s*</div>)',
        '<div class="usecase-card">\n          <div class="usecase-image"><span class="usecase-icon">📅</span></div>\n          <div class="usecase-content">\n            <h3 class="usecase-title">Appointment Booking</h3>\n            <p class="usecase-description">Einfache Terminbuchung ohne Back-and-Forth. Personalisierte Booking-Links für deine Kunden.</p>\n          </div>\n        </div>',
        content
    )
    
    # 4. Gallery Section
    content = re.sub(
        r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
        f'<h2 class="section-title">So sieht {TIDYCAL_DATA["name"]} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die Meeting-Scheduling-Plattform mit AI.</p>',
        content
    )
    
    # Gallery Captions
    content = re.sub(r'<div class="gallery-caption">Scenario Builder mit Modulen</div>', '<div class="gallery-caption">Scheduling Interface</div>', content)
    content = re.sub(r'<div class="gallery-caption">Router für Verzweigungen</div>', '<div class="gallery-caption">Calendar-Sync</div>', content)
    content = re.sub(r'<div class="gallery-caption">Data Mapping Interface</div>', '<div class="gallery-caption">AI-Optimierung</div>', content)
    content = re.sub(r'<div class="gallery-caption">Execution History</div>', '<div class="gallery-caption">Booking Links</div>', content)
    
    # 5. Pricing Section
    content = re.sub(
        r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
        f'<h2 class="section-title">{TIDYCAL_DATA["name"]} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
        content
    )
    
    # 6. Popular Package
    content = re.sub(
        r'(<h2 class="package-title">Make Core</h2>\s*<div class="package-price">€9/Monat</div>\s*<p class="package-description">Das beste Preis-Leistungs-Verhältnis.*?</p>\s*<div class="package-features">.*?</div>\s*<a href="#" class="btn btn-primary">Make Core holen</a>)',
        f'<h2 class="package-title">{TIDYCAL_DATA["name"]} Lifetime</h2>\n        <div class="package-price">LIFETIME DEAL</div>\n        <p class="package-description">Das beste Preis-Leistungs-Verhältnis für die meisten Anwender. Meeting-Scheduling, Calendar-Sync, AI-Optimierung und Booking-Links – einmalig zahlen, lebenslang nutzen.</p>\n        <div class="package-features">\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Meeting-Scheduling</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Calendar-Sync</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>AI-Optimierung</div>\n          <div class="package-feature"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>Booking-Links</div>\n        </div>\n        <a href="#" class="btn btn-primary">{TIDYCAL_DATA["name"]} Lifetime holen</a>',
        content,
        flags=re.DOTALL
    )
    
    # 7. Pros & Cons
    # Pros
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Flexibler als Zapier</strong> – Router, Schleifen und komplexe Logik möglich</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>AI-powered Scheduling</strong> – AI-gestützte Termin-Optimierung für bessere Verfügbarkeit</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Günstiger</strong> – Mehr Operationen für weniger Geld</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Calendar-Sync</strong> – Nahtlose Synchronisation mit Google Calendar, Outlook und anderen Kalendern</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Visueller Editor</strong> – Workflows auf einen Blick verstehen</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Booking-Links</strong> – Personalisierte Booking-Links für deine Kunden</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>HTTP/API Module</strong> – Verbinde jede API ohne native Integration</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span><strong>Reminders</strong> – Automatische Erinnerungen für Meetings und Termine</span></li>',
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
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Lernkurve</strong> – AI-Optimierung erfordert etwas Einarbeitung</span></li>',
        content
    )
    content = re.sub(
        r'(<li><svg.*?</svg><span><strong>Weniger native Apps</strong> – Nicht so viele direkte Integrationen wie Zapier</span></li>)',
        f'<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg><span><strong>Kalender-Limits</strong> – Limits bei der Anzahl der synchronisierten Kalender</span></li>',
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
        f'<h2 class="section-title">{TIDYCAL_DATA["name"]} vs. Konkurrenz</h2>',
        content
    )
    content = re.sub(
        r'(<tr><th>Feature</th><th>Make</th><th>Zapier</th><th>n8n</th></tr>)',
        f'<tr><th>Feature</th><th>{TIDYCAL_DATA["name"]}</th><th>Calendly</th><th>Acuity Scheduling</th></tr>',
        content
    )
    
    # 9. CTA Section
    content = re.sub(
        r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
        f'<h2 class="cta-title">Bereit für {TIDYCAL_DATA["name"]}?</h2>\n      <p class="cta-description">Starte jetzt und automatisiere deine Terminbuchung mit AI-powered Meeting-Scheduling und Kalender-Management.</p>',
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde vollständig angepasst")

if __name__ == '__main__':
    file_path = 'tidycal.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
