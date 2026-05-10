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
    
    # 1. Features Section
    features_section_pattern = r'(<h2 class="section-title">Was macht Make besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)'
    features_replacement = f'<h2 class="section-title">Was macht {ZEP_DATA["name"]} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der Memory API für AI-Agents.</p>'
    content = re.sub(features_section_pattern, features_replacement, content)
    
    # Features Grid anpassen
    feature_cards = []
    for i, feature in enumerate(ZEP_DATA['features'][:6]):
        icon_svg = get_feature_icon(feature['icon'])
        feature_card = f'''        <div class="feature-card">
          <div class="feature-icon">
            {icon_svg}
          </div>
          <h3 class="feature-title">{feature['title']}</h3>
          <p class="feature-description">{feature['description']}</p>
        </div>'''
        feature_cards.append(feature_card)
    
    features_grid_pattern = r'(<div class="features-grid">\s*)(<div class="feature-card">.*?</div>\s*){6}(\s*</div>)'
    features_grid_replacement = f'<div class="features-grid">\n' + '\n'.join(feature_cards) + '\n      </div>'
    content = re.sub(features_grid_pattern, features_grid_replacement, content, flags=re.DOTALL)
    
    # 2. Overview Section
    overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>)'
    overview_replacement = f'''<h3>Was ist {ZEP_DATA["name"]}?</h3>
          <p>
            {ZEP_DATA["name"]} ist eine Memory API für AI-Agents. Mit Langzeit-Memory ermöglicht {ZEP_DATA["name"]} kontextuelle Erinnerungen für Chatbots und Conversational AI – perfekt für intelligente Gesprächsführung.
          </p>
          <p>
            Im Gegensatz zu statischen Memory-Lösungen bietet {ZEP_DATA["name"]} intelligentes Context Management über mehrere Sessions hinweg. Das macht {ZEP_DATA["name"]} zur ersten Wahl für entwickler von Chatbots und Conversational AI-Anwendungen.
          </p>'''
    content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
    
    # 3. Use Cases Section
    usecases = [
        {'title': 'Chatbots', 'description': 'Intelligente Chatbots mit Langzeit-Memory. Verbessere die Gesprächsqualität mit kontextuellen Erinnerungen.'},
        {'title': 'Conversational AI', 'description': 'Conversational AI-Anwendungen mit Context Management. Nahtlose Gesprächsfortführung über mehrere Sessions.'},
        {'title': 'AI Agents', 'description': 'AI Agents mit Langzeit-Memory. Ermögliche deinen Agents, sich an vorherige Interaktionen zu erinnern.'}
    ]
    
    # 4. Pricing Section (wird später angepasst)
    
    # 5. Pros & Cons (wird später angepasst)
    
    # 6. Comparison (wird später angepasst)
    
    # 7. CTA (wird später angepasst)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {file_path} wurde angepasst")

def get_feature_icon(icon_type):
    """SVG Icons für Features"""
    icons = {
        'brain': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44L2 22v-1.5A2.5 2.5 0 0 1 4.5 18h1.5"/>
              <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44L22 22v-1.5A2.5 2.5 0 0 0 19.5 18H18"/>
            </svg>''',
        'layers': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>
            </svg>''',
        'users': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>''',
        'code': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>
            </svg>''',
        'message-circle': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
            </svg>''',
        'zap': '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
            </svg>'''
    }
    return icons.get(icon_type, icons['code'])

if __name__ == '__main__':
    file_path = 'zep-memory.html'
    try:
        adapt_file(file_path)
        print(f"✅ {file_path} wurde erfolgreich angepasst!")
    except Exception as e:
        print(f"❌ Fehler: {e}")
        sys.exit(1)
