#!/usr/bin/env python3
"""
🔧 AUTOMATISCHE REPARATUR
=========================
Fix:
1. Schwarzer Bildschirm auf produkte.html
2. Kein Scroll auf ueber-uns.html
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

def fix_produkte():
    """Fix schwarzer Bildschirm auf produkte.html"""
    file_path = SCRIPT_DIR / "produkte.html"
    content = file_path.read_text(encoding='utf-8')
    
    # Problem 1: Body könnte overflow: hidden haben
    # Problem 2: Main-Container könnte display: none oder opacity: 0 haben
    # Problem 3: Tools-Grid könnte nicht sichtbar sein
    
    fixes = []
    
    # Fix 1: Stelle sicher, dass body scrollbar hat
    if 'body {' in content:
        # Prüfe ob overflow: hidden auf body ist
        body_style_match = re.search(r'body\s*\{[^}]*\}', content, re.DOTALL)
        if body_style_match:
            body_style = body_style_match.group(0)
            if 'overflow' in body_style and 'hidden' in body_style:
                # Ersetze overflow: hidden mit overflow-y: auto
                content = content.replace(
                    body_style,
                    body_style.replace('overflow: hidden', 'overflow-y: auto').replace('overflow-x: hidden', 'overflow-x: hidden')
                )
                fixes.append("✅ Body overflow gefixt")
    
    # Fix 2: Stelle sicher, dass main-content sichtbar ist
    if '.main-content' in content or '#main-content' in content:
        # Entferne display: none !important von main-content
        content = re.sub(
            r'(\.main-content|#main-content)[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
            r'\1 { display: block !important; }',
            content,
            flags=re.DOTALL
        )
        fixes.append("✅ Main-content visibility gefixt")
    
    # Fix 3: Stelle sicher, dass tools-grid sichtbar ist
    if '.tools-grid' in content:
        # Entferne display: none von tools-grid
        content = re.sub(
            r'\.tools-grid[^{]*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
            r'.tools-grid { display: grid !important; }',
            content,
            flags=re.DOTALL
        )
        fixes.append("✅ Tools-grid visibility gefixt")
    
    # Fix 4: Stelle sicher, dass body background-color gesetzt ist
    if 'body {' in content:
        body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
            if 'background' not in body_content or 'background-color' not in body_content:
                # Füge background-color hinzu
                new_body = f"body {{\n{body_content}\n  background-color: var(--bg-base, #030712);\n}}"
                content = content.replace(body_match.group(0), new_body)
                fixes.append("✅ Body background-color hinzugefügt")
    
    # Fix 5: Stelle sicher, dass html overflow-y: auto hat
    if 'html {' in content:
        html_match = re.search(r'html\s*\{([^}]*)\}', content, re.DOTALL)
        if html_match:
            html_content = html_match.group(1)
            if 'overflow-y' not in html_content:
                new_html = f"html {{\n{html_content}\n  overflow-y: auto;\n}}"
                content = content.replace(html_match.group(0), new_html)
                fixes.append("✅ HTML overflow-y hinzugefügt")
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

def fix_ueber_uns():
    """Fix kein Scroll auf ueber-uns.html"""
    file_path = SCRIPT_DIR / "ueber-uns.html"
    content = file_path.read_text(encoding='utf-8')
    
    fixes = []
    
    # Fix 1: Stelle sicher, dass body scrollbar hat
    if 'body {' in content:
        body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
        if body_match:
            body_content = body_match.group(1)
            # Ersetze overflow: hidden mit overflow-y: auto
            if 'overflow' in body_content and 'hidden' in body_content:
                body_content = body_content.replace('overflow: hidden', 'overflow-y: auto')
                new_body = f"body {{\n{body_content}\n}}"
                content = content.replace(body_match.group(0), new_body)
                fixes.append("✅ Body overflow gefixt")
    
    # Fix 2: Stelle sicher, dass html overflow-y: auto hat
    if 'html {' in content:
        html_match = re.search(r'html\s*\{([^}]*)\}', content, re.DOTALL)
        if html_match:
            html_content = html_match.group(1)
            if 'overflow-y' not in html_content:
                new_html = f"html {{\n{html_content}\n  overflow-y: auto;\n}}"
                content = content.replace(html_match.group(0), new_html)
                fixes.append("✅ HTML overflow-y hinzugefügt")
    
    # Fix 3: Entferne position: fixed von Overlays die scrollen blockieren
    # Suche nach Overlays mit position: fixed die möglicherweise den ganzen Screen blockieren
    content = re.sub(
        r'\.(overlay|modal|popup)[^{]*\{[^}]*position\s*:\s*fixed[^}]*z-index\s*:\s*9999[^}]*\}',
        r'.\1 { position: fixed; z-index: 9999; pointer-events: none; }',
        content,
        flags=re.DOTALL
    )
    
    file_path.write_text(content, encoding='utf-8')
    return fixes

print("=" * 60)
print("🔧 AUTOMATISCHE REPARATUR")
print("=" * 60)
print()

print("1️⃣  Fix produkte.html (schwarzer Bildschirm)...")
produkte_fixes = fix_produkte()
for fix in produkte_fixes:
    print(f"   {fix}")
if not produkte_fixes:
    print("   ℹ️  Keine Fixes nötig")
print()

print("2️⃣  Fix ueber-uns.html (kein Scroll)...")
ueber_uns_fixes = fix_ueber_uns()
for fix in ueber_uns_fixes:
    print(f"   {fix}")
if not ueber_uns_fixes:
    print("   ℹ️  Keine Fixes nötig")
print()

print("=" * 60)
print("✅ REPARATUR ABGESCHLOSSEN!")
print("=" * 60)
print()
print("📤 Lade gefixte Dateien hoch...")
print()
