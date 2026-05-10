#!/usr/bin/env python3
"""
🔧 Füge fehlenden Body-Content zu produkte.html hinzu
=====================================================
"""

from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
file_path = SCRIPT_DIR / "produkte.html"

# Lese die Datei
content = file_path.read_text(encoding='utf-8')

# Body-Content (Navigation + Hero + Tool-Cards)
body_content = """
</head>
<body>
<a aria-label="Zum Hauptinhalt springen" class="skip-link" href="#main-content">Zum Hauptinhalt springen</a>

<!-- ========================================
     NAVIGATION
     ======================================== -->
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

<!-- ========================================
     PRODUKTE PAGE
     ======================================== -->
<main class="produkte-page" id="main-content">
<!-- Hero Section -->
<section class="produkte-hero">
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
<section class="tools-intro">
<div class="container">
<p>Alle Tools sind vollständig in unsere n8n Workflows integriert und werden täglich in Produktion eingesetzt. Wir testen kontinuierlich neue Tools und erweitern unser Arsenal.</p>
</div>
</section>

<!-- Tools Grid -->
<section class="tools-section">
<div class="container">
<div class="tools-grid">
<!-- Tool Cards werden hier dynamisch geladen -->
<div class="tool-card" data-category="ai">
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

<div class="tool-card" data-category="ai">
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

<div class="tool-card" data-category="ai">
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

<!-- Weitere Tool-Cards können hier hinzugefügt werden -->
</div>
</div>
</section>
</main>

<!-- ========================================
     FOOTER
     ======================================== -->
<footer class="footer">
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
<div class="footer__col">
<h4 class="footer__subtitle">Rechtliches</h4>
<ul class="footer__links">
<li><a href="#impressum">Impressum</a></li>
<li><a href="#datenschutz">Datenschutz</a></li>
</ul>
</div>
</div>
<div class="footer__bottom">
<p>&copy; 2024 CanGo App Empire. Alle Rechte vorbehalten.</p>
</div>
</div>
</footer>
"""

# Ersetze </style> mit </style> + Body-Content
if '</style>' in content:
    content = content.replace('</style>', '</style>' + body_content)
    file_path.write_text(content, encoding='utf-8')
    print("✅ Body-Content hinzugefügt!")
else:
    print("❌ </style> nicht gefunden!")
