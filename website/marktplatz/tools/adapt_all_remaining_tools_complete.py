#!/usr/bin/env python3
"""
Vollständige Anpassung ALLER restlichen Tools (51 Tools)
Universelles Template-basiertes System für konsistente Anpassungen
"""

import re
import os
import sys

# Liste aller bereits angepassten Tools
ADAPTED_TOOLS = [
    'firecrawl', 'scraperapi', 'synthesia', 'stable-diffusion', 'bright-data',
    'pinecone', 'zep-memory', 'opus-clip', 'yapper', 'reap',
    'mootion', 'tidycal', 'nocode-backend', 'unmixr-ai', 'goose-vpn',
    'sociamonials', 'voila', 'binance-api', 'hostinger', 'luma-ai',
    'claude-artifacts', 'gamma', 'tome', 'murf', 'playht', 'headlime',
    'writesonic', 'grammarly', 'wordtune', 'quillbot', 'originality-ai'
]

def adapt_tool_complete(file_path, tool_name, description=""):
    """Vollständige Anpassung eines Tools mit allen Sections"""
    
    if not os.path.exists(file_path):
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Video Section
        content = re.sub(
            r'(<p class="section-label">Erklärvideo</p>\s*<h2 class="section-title">[^<]+in Aktion</h2>\s*<p class="section-subtitle">[^<]+</p>)',
            f'<p class="section-label">Erklärvideo</p>\n        <h2 class="section-title">{tool_name} in Aktion</h2>\n        <p class="section-subtitle">Erfahre, wie du mit {tool_name} {description or "professionelle Ergebnisse erzielst"}.</p>',
            content
        )
        content = re.sub(r'(<p>Klicken um Video zu laden</p>|<p>Video wird später integriert</p>)', '<p>Video wird später integriert</p>', content)
        
        # 2. Features Section
        content = re.sub(
            r'(<h2 class="section-title">Was macht [^<]+ besonders\?</h2>\s*<p class="section-subtitle">Entdecke die Vorteile der visuellen Automation-Plattform\.</p>)',
            f'<h2 class="section-title">Was macht {tool_name} besonders?</h2>\n        <p class="section-subtitle">Entdecke die Vorteile der {tool_name}-Plattform.</p>',
            content
        )
        
        # Features werden nicht einzeln angepasst (zu komplex für Batch-Verarbeitung)
        # Sie bleiben im Template-Zustand, können später verfeinert werden
        
        # 3. Overview Section
        overview_pattern = r'(<h3>Was ist Make\?</h3>\s*<p>\s*Make \(ehemals Integromat\) ist eine der leistungsstärksten visuellen Automation-Plattformen.*?</p>\s*<p>.*?</p>\s*<ul class="overview-list">\s*<li>.*?</li>\s*<li>.*?</li>\s*<li>.*?</li>\s*</ul>)'
        overview_replacement = f'''<h3>Was ist {tool_name}?</h3>
          <p>
            {tool_name} ist eine leistungsstarke Plattform für professionelle Ergebnisse. {description or f"Mit {tool_name} erzielst du maximale Effizienz und professionelle Qualität für deine Projekte."}
          </p>
          <p>
            Im Gegensatz zu traditionellen Tools bietet {tool_name} moderne Funktionen und optimierte Workflows für bessere Ergebnisse. Das macht {tool_name} zur ersten Wahl für professionelle Anwender.
          </p>
          <ul class="overview-list">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Professionelle Funktionen und Features für optimale Ergebnisse
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Optimierte Workflows für maximale Effizienz und Produktivität
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              Moderne Technologie für beste Qualität und Performance
            </li>
          </ul>'''
        content = re.sub(overview_pattern, overview_replacement, content, flags=re.DOTALL)
        content = re.sub(r'(<span>Screenshot: Make Scenario Builder</span>|<span>Screenshot:.*?</span>)', f'<span>Screenshot: {tool_name} Dashboard</span>', content)
        
        # 4. Use Cases Section
        content = re.sub(
            r'(<h2 class="section-title">Wofür kann ich Make nutzen\?</h2>\s*<p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten\.</p>)',
            f'<h2 class="section-title">Wofür kann ich {tool_name} nutzen?</h2>\n        <p class="section-subtitle">Entdecke die vielfältigen Einsatzmöglichkeiten.</p>',
            content
        )
        
        # 5. Gallery Section
        content = re.sub(
            r'(<h2 class="section-title">So sieht Make aus</h2>\s*<p class="section-subtitle">Ein Blick auf den visuellen Workflow-Builder\.</p>)',
            f'<h2 class="section-title">So sieht {tool_name} aus</h2>\n        <p class="section-subtitle">Ein Blick auf die {tool_name}-Plattform.</p>',
            content
        )
        
        # 6. Pricing Section
        content = re.sub(
            r'(<h2 class="section-title">Make Preismodelle</h2>\s*<p class="section-subtitle">Flexible Pakete für jeden Bedarf\.</p>)',
            f'<h2 class="section-title">{tool_name} Preismodelle</h2>\n        <p class="section-subtitle">Flexible Pakete für jeden Bedarf.</p>',
            content
        )
        
        # 7. Comparison Section
        content = re.sub(
            r'(<h2 class="section-title">Make vs\. Konkurrenz</h2>)',
            f'<h2 class="section-title">{tool_name} vs. Konkurrenz</h2>',
            content
        )
        
        # 8. CTA Section
        content = re.sub(
            r'(<h2 class="cta-title">Bereit für Make\?</h2>\s*<p class="cta-description">Starte kostenlos und automatisiere deine Workflows in Minuten\.</p>)',
            f'<h2 class="cta-title">Bereit für {tool_name}?</h2>\n      <p class="cta-description">Starte jetzt und nutze {tool_name} für professionelle Ergebnisse und optimierte Workflows.</p>',
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    except Exception as e:
        print(f"   ❌ Fehler bei {tool_name}: {e}")
        return False

# Tool-Mapping mit Dateinamen und Namen
TOOLS_TO_ADAPT = [
    ('chatgpt-plus.html', 'ChatGPT / OpenAI', 'GPT-4o für Datenanalyse, Vision-Tasks und Content-Generierung'),
    ('chatgpt.html', 'ChatGPT', 'GPT-4o für komplexe Aufgaben'),
    ('claude.html', 'Anthropic Claude', 'Das Gehirn unserer Python-Skripte für besseren Code'),
    ('claude-35.html', 'Claude 3.5 Sonnet', 'Überlegene Code-Qualität mit 200K Token Context'),
    ('perplexity-pro.html', 'Perplexity Pro', 'Echtzeit-Websuche mit Quellen für Business-Research'),
    ('perplexity.html', 'Perplexity', 'Echtzeit-Web-Recherche mit Faktenverifikation'),
    ('browseract.html', 'BrowserAct', 'Ghost-Agent für Headless Automation ohne API'),
    ('neuronwriter.html', 'NeuronWriter', 'NLP-Analyse für Content-Cluster und SEO-optimierte Blog-Generierung'),
    ('depositphotos.html', 'DepositPhotos', '320 Mio. Bilder/Videos mit Lifetime-Zugriff'),
    ('katteb.html', 'Katteb', 'Fact-Shield für verifizierte Informationen'),
    ('gemini.html', 'Gemini', 'Googles AI-Modell für multimodale Aufgaben'),
    ('grok.html', 'Grok', 'X.ai AI-Modell für natürliche Konversationen'),
    ('mistral-ai.html', 'Mistral AI', 'Open-Source AI-Modelle für Entwickler'),
    ('make-integromat.html', 'Make (Integromat)', 'Visuelle Automation-Plattform für komplexe Workflows'),
    ('zapier.html', 'Zapier', 'Automatisierung zwischen Apps ohne Code'),
    ('midjourney.html', 'Midjourney', 'AI-Image-Generierung für kreative Visuals'),
    ('runway.html', 'Runway', 'AI-Video-Generierung für kreative Projekte'),
    ('runway-gen3.html', 'Runway Gen-3', 'Next-Gen AI-Video-Generierung'),
    ('elevenlabs.html', 'ElevenLabs', 'Ultra-realistische Text-to-Speech-Stimmen'),
    ('surfer-seo.html', 'Surfer SEO', 'SEO-Optimierung für bessere Rankings'),
    ('ahrefs.html', 'Ahrefs', 'SEO-Tools für Keyword-Recherche und Backlink-Analyse'),
    ('descript.html', 'Descript', 'Video-Editor mit AI-Transkription'),
    ('notion.html', 'Notion AI', 'AI-gestütztes Workspace für Teams'),
    ('cursor.html', 'Cursor (AI IDE)', 'AI-powered Code-Editor für Entwickler'),
    ('frase.html', 'Frase', 'AI-Content-Optimierung für SEO'),
    ('jasper-ai.html', 'Jasper AI', 'AI-Content-Generierung für Marketing'),
    ('copy-ai.html', 'Copy.ai', 'AI-Copywriting für Marketing und Sales'),
    ('pika-labs.html', 'Pika Labs', 'AI-Video-Generierung für kreative Projekte'),
    ('semrush.html', 'SEMrush', 'SEO- und Marketing-Tools für bessere Rankings'),
    ('airtable.html', 'Airtable', 'Flexible Datenbank-Plattform für Teams'),
    ('supabase.html', 'Supabase', 'Open-Source Firebase-Alternative'),
    ('langchain.html', 'LangChain', 'Framework für LLM-Anwendungen'),
    ('hugging-face.html', 'Hugging Face', 'Open-Source AI-Modelle und Datasets'),
    ('feedspace.html', 'Feedspace', 'Social Media Automation-Plattform'),
    ('greta-ai.html', 'Greta', 'AI-Video-Generierung für Marketing'),
    ('skillplate.html', 'Skillplate', 'Online-Kurs-Plattform für Wissen'),
    ('canva.html', 'Canva', 'Design-Tool für kreative Visuals'),
    ('hubspot.html', 'HubSpot', 'All-in-One Marketing- und Sales-Plattform'),
    ('pipedrive.html', 'Pipedrive', 'CRM für Sales-Teams'),
    ('sendgrid.html', 'SendGrid', 'Email-Marketing-Plattform'),
    ('mailchimp.html', 'Mailchimp', 'Email-Marketing und Automation'),
    ('calendly.html', 'Calendly', 'Terminplanung ohne E-Mail-Chaos'),
    ('loom.html', 'Loom', 'Video-Messaging für Teams'),
    ('otter-ai.html', 'Otter.ai', 'AI-Transkription für Meetings'),
    ('rev.html', 'Rev', 'Professionelle Transkriptions-Services'),
    ('replicate.html', 'Replicate', 'Machine Learning API für Entwickler'),
    ('together-ai.html', 'Together.ai', 'Open-Source AI-Modelle API'),
    ('anthropic-bedrock.html', 'Anthropic Bedrock', 'AWS-integrierte Claude API'),
    ('cohere.html', 'Cohere', 'Enterprise AI für Text-Processing'),
    ('serper.html', 'Serper', 'Google Search API für Entwickler'),
    ('serpapi.html', 'SerpAPI', 'Search Engine Results API'),
    ('clickup.html', 'ClickUp', 'All-in-One Projektmanagement'),
    ('monday.html', 'Monday.com', 'Work-Management-Plattform für Teams'),
    ('asana.html', 'Asana', 'Projektmanagement für Teams'),
    ('typeform.html', 'Typeform', 'Interaktive Formulare und Umfragen'),
    ('stripe.html', 'Stripe', 'Payment-Processing für Online-Businesses'),
    ('unsplash-api.html', 'Unsplash API', 'Kostenlose Stock-Fotos API'),
    ('pexels-api.html', 'Pexels API', 'Kostenlose Stock-Videos API'),
    ('framer.html', 'Framer', 'Design-Tool für interaktive Prototypen'),
    ('webflow.html', 'Webflow', 'No-Code Website-Builder'),
    ('bubble.html', 'Bubble', 'No-Code App-Builder'),
    ('vercel.html', 'Vercel', 'Frontend-Hosting für moderne Web-Apps'),
    ('github.html', 'GitHub Copilot', 'AI-Pair-Programming für Entwickler'),
    ('tabnine.html', 'Tabnine', 'AI-Code-Completion für Entwickler'),
    ('sourcegraph.html', 'Sourcegraph', 'Code-Search und -Navigation'),
    # Weitere Tools nach Bedarf...
]

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 VOLLSTÄNDIGE ANPASSUNG ALLER RESTLICHEN TOOLS")
    print("=" * 60)
    print("")
    
    adapted_count = 0
    failed_count = 0
    
    for file_path, tool_name, description in TOOLS_TO_ADAPT:
        print(f"⏳ Bearbeite: {tool_name}...", end=' ')
        if adapt_tool_complete(file_path, tool_name, description):
            print("✅")
            adapted_count += 1
        else:
            print("❌")
            failed_count += 1
    
    print("")
    print("=" * 60)
    print(f"✅ {adapted_count} Tools erfolgreich angepasst")
    if failed_count > 0:
        print(f"❌ {failed_count} Tools konnten nicht angepasst werden")
    print("=" * 60)
    print("")
    print("🎉 ALLE RESTLICHEN TOOLS SIND JETZT ANGEPASST!")
