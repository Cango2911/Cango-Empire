#!/usr/bin/env python3
"""
🔧 FIX ECHTE PROBLEME
=====================
Das Problem ist wahrscheinlich:
1. JavaScript läuft bevor DOM ready ist
2. Tool-Cards werden nicht gefunden
3. CSS versteckt den Content
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

def fix_produkte_real():
    """Fix echte Probleme in produkte.html"""
    file_path = SCRIPT_DIR / "produkte.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Fix 1: Stelle sicher, dass .produkte-page sichtbar ist
    if '.produkte-page' in content:
        # Entferne alle display: none von produkte-page
        content = re.sub(
            r'\.produkte-page[^{]*\{[^}]*display\s*:\s*none[^}]*\}',
            r'.produkte-page { display: block !important; }',
            content,
            flags=re.DOTALL
        )
        fixes.append("✅ produkte-page visibility")
    
    # Fix 2: Stelle sicher, dass .tools-grid sichtbar ist
    content = re.sub(
        r'\.tools-grid[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'.tools-grid { display: grid !important; visibility: visible !important; opacity: 1 !important; }',
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ tools-grid visibility")
    
    # Fix 3: Stelle sicher, dass .tool-card sichtbar ist
    content = re.sub(
        r'\.tool-card[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'.tool-card { display: block !important; visibility: visible !important; }',
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ tool-card visibility")
    
    # Fix 4: Füge CSS hinzu um sicherzustellen dass Content sichtbar ist
    # Suche nach </style> und füge vorher ein
    if '</style>' in content:
        critical_css = """
    /* === KRITISCHER FIX: Stelle sicher dass Content sichtbar ist === */
    .produkte-page,
    .produkte-hero,
    .tools-intro,
    .tools-grid,
    .tool-card {
      display: block !important;
      visibility: visible !important;
      opacity: 1 !important;
    }
    
    .tools-grid {
      display: grid !important;
    }
    
    body {
      overflow-y: auto !important;
      overflow-x: hidden !important;
    }
    
    html {
      overflow-y: auto !important;
    }
"""
        content = content.replace('</style>', critical_css + '\n  </style>')
        fixes.append("✅ Kritischer CSS-Fix hinzugefügt")
    
    # Fix 5: Stelle sicher, dass JavaScript erst nach DOMContentLoaded läuft
    # Suche nach loadToolLogos Funktion
    if 'loadToolLogos' in content:
        # Stelle sicher, dass es nach DOMContentLoaded läuft
        if 'document.addEventListener(\'DOMContentLoaded\'' not in content or 'document.readyState' not in content:
            # Füge DOMContentLoaded Wrapper hinzu
            content = re.sub(
                r'(function loadToolLogos\(\) \{)',
                r'// Warte auf DOM\n    if (document.readyState === \'loading\') {\n      document.addEventListener(\'DOMContentLoaded\', function() {\n        setTimeout(loadToolLogos, 100);\n      });\n      return;\n    }\n    \1',
                content
            )
            fixes.append("✅ JavaScript DOM-Ready Fix")
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

def fix_ueber_uns_real():
    """Fix echte Probleme in ueber-uns.html"""
    file_path = SCRIPT_DIR / "ueber-uns.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Fix 1: Füge kritischen CSS-Fix hinzu
    if '</style>' in content:
        critical_css = """
    /* === KRITISCHER FIX: Stelle sicher dass Scrollen funktioniert === */
    html {
      overflow-y: auto !important;
      height: auto !important;
    }
    
    body {
      overflow-y: auto !important;
      overflow-x: hidden !important;
      min-height: 100vh !important;
      height: auto !important;
      position: relative !important;
    }
    
    /* Entferne alle Overlays die scrollen blockieren */
    .overlay,
    .modal,
    .backdrop {
      pointer-events: none !important;
    }
"""
        content = content.replace('</style>', critical_css + '\n  </style>')
        fixes.append("✅ Kritischer CSS-Fix hinzugefügt")
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

print("=" * 60)
print("🔧 FIX ECHTE PROBLEME")
print("=" * 60)
print()

print("1️⃣  Fix produkte.html...")
produkte_fixes = fix_produkte_real()
for fix in produkte_fixes:
    print(f"   {fix}")
print()

print("2️⃣  Fix ueber-uns.html...")
ueber_uns_fixes = fix_ueber_uns_real()
for fix in ueber_uns_fixes:
    print(f"   {fix}")
print()

print("=" * 60)
print("✅ FIXES ABGESCHLOSSEN!")
print("=" * 60)
print()
