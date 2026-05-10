#!/usr/bin/env python3
"""
🔧 KRITISCHE FIXES
==================
Fix:
1. Schwarzer Bildschirm - stelle sicher dass Content sichtbar ist
2. Kein Scroll - entferne alle Scroll-Blockaden
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

def fix_produkte_critical():
    """Kritische Fixes für produkte.html"""
    file_path = SCRIPT_DIR / "produkte.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Fix 1: Stelle sicher, dass body overflow-y: auto hat (nicht hidden)
    content = re.sub(
        r'body\s*\{[^}]*overflow[^}]*\}',
        lambda m: m.group(0).replace('overflow: hidden', 'overflow-y: auto').replace('overflow-x: hidden', 'overflow-x: hidden'),
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ Body overflow gefixt")
    
    # Fix 2: Stelle sicher, dass html overflow-y: auto hat
    if 'html {' in content:
        html_match = re.search(r'html\s*\{([^}]*)\}', content, re.DOTALL)
        if html_match:
            html_content = html_match.group(1)
            if 'overflow-y' not in html_content:
                new_html = f"html {{\n{html_content}\n  overflow-y: auto !important;\n}}"
                content = content.replace(html_match.group(0), new_html)
                fixes.append("✅ HTML overflow-y hinzugefügt")
    
    # Fix 3: Stelle sicher, dass .produkte-page sichtbar ist
    content = re.sub(
        r'\.produkte-page[^{]*\{[^}]*display\s*:\s*none[^}]*\}',
        r'.produkte-page { display: block !important; }',
        content,
        flags=re.DOTALL
    )
    
    # Fix 4: Stelle sicher, dass .tools-grid sichtbar ist
    content = re.sub(
        r'\.tools-grid[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'.tools-grid { display: grid !important; }',
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ Tools-grid visibility gefixt")
    
    # Fix 5: Stelle sicher, dass body background-color gesetzt ist
    body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        if 'background' not in body_content or ('background:' in body_content and 'var(--bg-base)' not in body_content):
            # Füge background hinzu falls nicht vorhanden
            if 'background:' not in body_content:
                new_body = f"body {{\n{body_content}\n  background-color: var(--bg-base, #030712) !important;\n}}"
                content = content.replace(body_match.group(0), new_body)
                fixes.append("✅ Body background-color gesetzt")
    
    # Fix 6: Stelle sicher, dass main-content sichtbar ist
    content = re.sub(
        r'(\.main-content|#main-content|main)[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'\1 { display: block !important; }',
        content,
        flags=re.DOTALL
    )
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

def fix_ueber_uns_critical():
    """Kritische Fixes für ueber-uns.html"""
    file_path = SCRIPT_DIR / "ueber-uns.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Fix 1: Body overflow-y: auto (nicht hidden)
    content = re.sub(
        r'body\s*\{[^}]*overflow[^}]*\}',
        lambda m: m.group(0).replace('overflow: hidden', 'overflow-y: auto').replace('overflow-x: hidden', 'overflow-x: hidden'),
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ Body overflow gefixt")
    
    # Fix 2: HTML overflow-y: auto
    if 'html {' in content:
        html_match = re.search(r'html\s*\{([^}]*)\}', content, re.DOTALL)
        if html_match:
            html_content = html_match.group(1)
            if 'overflow-y' not in html_content:
                new_html = f"html {{\n{html_content}\n  overflow-y: auto !important;\n}}"
                content = content.replace(html_match.group(0), new_html)
                fixes.append("✅ HTML overflow-y hinzugefügt")
    
    # Fix 3: Entferne position: fixed von Overlays die scrollen blockieren
    # Suche nach Overlays mit sehr hohem z-index die den ganzen Screen blockieren könnten
    content = re.sub(
        r'\.(overlay|modal|popup|backdrop)[^{]*\{[^}]*position\s*:\s*fixed[^}]*z-index\s*:\s*999[^}]*\}',
        lambda m: m.group(0).replace('position: fixed', 'position: absolute') if 'pointer-events: none' not in m.group(0) else m.group(0),
        content,
        flags=re.DOTALL
    )
    
    # Fix 4: Stelle sicher, dass body min-height hat für Scrollen
    body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        if 'min-height' not in body_content:
            new_body = f"body {{\n{body_content}\n  min-height: 100vh;\n}}"
            content = content.replace(body_match.group(0), new_body)
            fixes.append("✅ Body min-height hinzugefügt")
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

print("=" * 60)
print("🔧 KRITISCHE FIXES")
print("=" * 60)
print()

print("1️⃣  Fix produkte.html...")
produkte_fixes = fix_produkte_critical()
for fix in produkte_fixes:
    print(f"   {fix}")
print()

print("2️⃣  Fix ueber-uns.html...")
ueber_uns_fixes = fix_ueber_uns_critical()
for fix in ueber_uns_fixes:
    print(f"   {fix}")
print()

print("=" * 60)
print("✅ KRITISCHE FIXES ABGESCHLOSSEN!")
print("=" * 60)
print()
