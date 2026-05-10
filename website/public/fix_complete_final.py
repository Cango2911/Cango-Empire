#!/usr/bin/env python3
"""
🔧 KOMPLETT-FIX: Füge vollständigen Body-Content hinzu
=====================================================
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

def fix_produkte_complete():
    """Füge vollständigen Body-Content zu produkte.html hinzu"""
    file_path = SCRIPT_DIR / "produkte.html"
    content = file_path.read_text(encoding='utf-8')
    
    # Prüfe ob Body bereits vorhanden ist
    if '<body' in content and '</body>' in content:
        # Body existiert, aber vielleicht fehlt Content
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1).strip()
            if len(body_content) < 100:  # Body ist fast leer
                print("   ⚠️  Body existiert aber ist fast leer")
                # Ersetze leeren Body mit vollständigem Content
                full_body = get_full_body_content()
                content = re.sub(
                    r'<body[^>]*>.*?</body>',
                    full_body,
                    content,
                    flags=re.DOTALL
                )
                file_path.write_text(content, encoding='utf-8')
                return ["✅ Body-Content vollständig ersetzt"]
            else:
                return ["ℹ️  Body-Content bereits vorhanden"]
    
    # Body existiert nicht - füge hinzu
    if '</style>' in content:
        full_body = get_full_body_content()
        content = content.replace('</style>', '</style>\n' + full_body)
        file_path.write_text(content, encoding='utf-8')
        return ["✅ Body-Content hinzugefügt"]
    
    return ["❌ Konnte Body-Content nicht hinzufügen"]

def get_full_body_content():
    """Gibt vollständigen Body-Content zurück"""
    return """</head>
<body>
<a aria-label="Zum Hauptinhalt springen" class="skip-link" href="#main-content">Zum Hauptinhalt springen</a>

<!-- NAVIGATION -->
<nav aria-label="Hauptnavigation" class="nav" role="navigation">
<div class="container nav__inner">
<a class="nav__brand" href="cango-empire-v4-monopoly.html#home">
<span class="nav__brand-icon">C</span>
<span>CanGo App Empire</span>
</a>
<button aria-label="Menü öffnen" class="nav__toggle" onclick="document.querySelector('.nav__menu').classList.toggle('active')" type="button">
<span></span>
<span></span>
<span></span>
</button>
<div class="nav__menu">
<a class="nav__link" href="cango-empire-v4-monopoly.html#branchen">Branchen</a>
<a class="nav__link" href="produkte.html"><!-- ACTIVE -->Produkte</a>
<a class="nav__link" href="selfmade-empire.html">Workflow Kampagnen</a>
<a class="nav__link" href="ueber-uns.html">Über Uns</a>
<a class="nav__link" href="cango-empire-v4-monopoly.html#faq">FAQ</a>
<a class="nav__cta" href="kontakt.html">Jetzt anfragen</a>
</div>
</div>
</nav>

<!-- PRODUKTE PAGE -->
<main class="produkte-page" id="main-content" style="display: block !important; visibility: visible !important; opacity: 1 !important;">

<!-- Hero Section -->
<section class="produkte-hero" style="display: block !important;">
<div class="container">
<div class="produkte-header">
<div class="produkte-header__icon">⚡</div>
<div class="produkte-hero__eyebrow">KI-TOOLS & AUTOMATION</div>
<h1 class="produkte-hero__title">Die besten KI-Tools für deine Workflows</h1>
<p class="produkte-hero__subtitle">Getestet, integriert und optimiert für maximale Performance in unseren n8n Automation-Workflows</p>
</div>
</div>
</section>

<!-- Tools Intro -->
<section class="tools-intro" style="display: block !important;">
<div class="container">
<p>Alle Tools sind vollständig in unsere n8n Workflows integriert und werden täglich in Produktion eingesetzt. Wir testen kontinuierlich neue Tools und erweitern unser Arsenal.</p>
</div>
</section>

<!-- Tools Grid -->
<section class="tools-section" style="display: block !important;">
<div class="container">
<div class="tools-grid" style="display: grid !important; visibility: visible !important; opacity: 1 !important;">
<div class="tool-card" data-category="ai" style="display: block !important; visibility: visible !important;">
<div class="tool-card__header">
<div class="tool-card__icon"></div>
<div class="tool-card__title-group">
<span class="tool-card__badge">KI</span>
<h3 class="tool-card__name">ChatGPT / OpenAI</h3>
</div>
</div>
<p class="tool-card__description">Mächtiger Sprachmodell für Textgenerierung, Code und Konversationen</p>
<ul class="tool-card__features">
<li>GPT-4 Turbo</li>
<li>Code Interpreter</li>
<li>DALL-E Integration</li>
</ul>
<div class="tool-card__footer">
<span class="tool-card__price">Ab $20/Monat</span>
<a href="https://openai.com" class="tool-card__cta" target="_blank" rel="noopener">Jetzt testen</a>
</div>
</div>

<div class="tool-card" data-category="ai" style="display: block !important; visibility: visible !important;">
<div class="tool-card__header">
<div class="tool-card__icon"></div>
<div class="tool-card__title-group">
<span class="tool-card__badge">KI</span>
<h3 class="tool-card__name">Claude 3.5 Sonnet</h3>
</div>
</div>
<p class="tool-card__description">Fortgeschrittenes KI-Modell von Anthropic mit exzellenter Code-Qualität</p>
<ul class="tool-card__features">
<li>200K Context Window</li>
<li>Code Generation</li>
<li>Document Analysis</li>
</ul>
<div class="tool-card__footer">
<span class="tool-card__price">Ab $15/Monat</span>
<a href="https://anthropic.com" class="tool-card__cta" target="_blank" rel="noopener">Jetzt testen</a>
</div>
</div>

<div class="tool-card" data-category="ai" style="display: block !important; visibility: visible !important;">
<div class="tool-card__header">
<div class="tool-card__icon"></div>
<div class="tool-card__title-group">
<span class="tool-card__badge">KI</span>
<h3 class="tool-card__name">Perplexity Pro</h3>
</div>
</div>
<p class="tool-card__description">KI-Suchmaschine mit Quellenangaben und aktuellen Informationen</p>
<ul class="tool-card__features">
<li>Real-time Search</li>
<li>Source Citations</li>
<li>Pro Search Mode</li>
</ul>
<div class="tool-card__footer">
<span class="tool-card__price">Ab $20/Monat</span>
<a href="https://perplexity.ai" class="tool-card__cta" target="_blank" rel="noopener">Jetzt testen</a>
</div>
</div>
</div>
</div>
</section>
</main>

<!-- FOOTER -->
<footer class="footer" style="display: block !important;">
<div class="container">
<div class="footer__grid">
<div class="footer__col">
<h3 class="footer__title">CanGo App Empire</h3>
<p class="footer__text">Die industrielle Revolution im Marketing</p>
</div>
<div class="footer__col">
<h4 class="footer__subtitle">Navigation</h4>
<ul class="footer__links">
<li><a href="cango-empire-v4-monopoly.html">Startseite</a></li>
<li><a href="produkte.html">Produkte</a></li>
<li><a href="ueber-uns.html">Über Uns</a></li>
<li><a href="kontakt.html">Kontakt</a></li>
</ul>
</div>
</div>
<div class="footer__bottom">
<p>&copy; 2024 CanGo App Empire. Alle Rechte vorbehalten.</p>
</div>
</div>
</footer>
"""

def fix_ueber_uns_scroll():
    """Fix Scroll-Problem auf ueber-uns.html"""
    file_path = SCRIPT_DIR / "ueber-uns.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Stelle sicher, dass body min-height und overflow-y hat
    body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        if 'overflow-y: auto' not in body_content or 'min-height' not in body_content:
            new_body = f"body {{\n{body_content}\n  overflow-y: auto !important;\n  overflow-x: hidden !important;\n  min-height: 100vh !important;\n  height: auto !important;\n  position: relative !important;\n}}"
            content = content.replace(body_match.group(0), new_body)
            fixes.append("✅ Body scroll-Fix")
    
    # Stelle sicher, dass html overflow-y hat
    html_match = re.search(r'html\s*\{([^}]*)\}', content, re.DOTALL)
    if html_match:
        html_content = html_match.group(1)
        if 'overflow-y: auto' not in html_content:
            new_html = f"html {{\n{html_content}\n  overflow-y: auto !important;\n  height: auto !important;\n}}"
            content = content.replace(html_match.group(0), new_html)
            fixes.append("✅ HTML scroll-Fix")
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

print("=" * 60)
print("🔧 KOMPLETT-FIX")
print("=" * 60)
print()

print("1️⃣  Fix produkte.html...")
produkte_fixes = fix_produkte_complete()
for fix in produkte_fixes:
    print(f"   {fix}")
print()

print("2️⃣  Fix ueber-uns.html (Scroll)...")
ueber_uns_fixes = fix_ueber_uns_scroll()
for fix in ueber_uns_fixes:
    print(f"   {fix}")
print()

print("=" * 60)
print("✅ FIXES ABGESCHLOSSEN!")
print("=" * 60)
print()
