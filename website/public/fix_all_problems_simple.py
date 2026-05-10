#!/usr/bin/env python3
"""
🔧 FIX ALLE PROBLEME (Einfacher Ansatz)
=======================================
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

# Prüfe welche Datei gefixt werden soll - die große Version
produkte_file = SCRIPT_DIR / "produkte_complete.html"
if not produkte_file.exists():
    produkte_file = SCRIPT_DIR / "produkte.html"

print("=" * 60)
print("🔧 FIX ALLE PROBLEME")
print("=" * 60)
print()
print(f"📁 Datei: {produkte_file.name}")
print(f"   Größe: {produkte_file.stat().st_size:,} Bytes")
print()

content = produkte_file.read_text(encoding='utf-8')
original_size = len(content)
fixes = []

# Fix 1: Entferne display: none !important
count_before = content.count('display: none !important') + content.count('display:none !important')
content = content.replace('display: none !important', 'display: block !important')
content = content.replace('display:none !important', 'display: block !important')
if count_before > 0:
    fixes.append(f"✅ {count_before}x display: none !important → display: block !important")

# Fix 2: body overflow: hidden → overflow-y: auto
body_match = re.search(r'body\s*\{[^}]*\}', content, re.DOTALL)
if body_match:
    body_css = body_match.group(0)
    if 'overflow' in body_css and 'hidden' in body_css and 'overflow-y: auto' not in body_css:
        new_body = body_css.replace('overflow: hidden', 'overflow-y: auto')
        new_body = new_body.replace('overflow-x: hidden', 'overflow-x: hidden')
        if 'overflow-y: auto' not in new_body:
            new_body = new_body.replace('{', '{ overflow-y: auto !important; ')
        content = content.replace(body_css, new_body)
        fixes.append("✅ body overflow: hidden → overflow-y: auto !important")

# Fix 3: tools-container max-height: 80vh entfernen
if 'tools-container' in content and 'max-height: 80vh' in content:
    content = content.replace('max-height: 80vh', 'max-height: none')
    fixes.append("✅ tools-container max-height: 80vh → max-height: none")

# Fix 4: .tools-grid display: none → display: grid
if '.tools-grid' in content:
    # Suche nach .tools-grid CSS
    tools_grid_pattern = r'\.tools-grid[^{]*\{[^}]*display\s*:\s*none[^}]*\}'
    matches = re.findall(tools_grid_pattern, content, re.DOTALL | re.IGNORECASE)
    if matches:
        for match in matches:
            new_match = match.replace('display: none', 'display: grid !important')
            new_match = new_match.replace('display:none', 'display: grid !important')
            content = content.replace(match, new_match)
        fixes.append(f"✅ {len(matches)}x .tools-grid display: none → display: grid !important")

# Fix 5: .tool-card display: none → display: block
if '.tool-card' in content:
    tool_card_pattern = r'\.tool-card[^{]*\{[^}]*display\s*:\s*none[^}]*\}'
    matches = re.findall(tool_card_pattern, content, re.DOTALL | re.IGNORECASE)
    if matches:
        for match in matches:
            new_match = match.replace('display: none', 'display: block !important')
            new_match = new_match.replace('display:none', 'display: block !important')
            content = content.replace(match, new_match)
        fixes.append(f"✅ {len(matches)}x .tool-card display: none → display: block !important")

# Fix 6: Füge kritischen CSS-Fix am Ende hinzu (vor </style>)
if '</style>' in content:
    critical_fix = """
    /* === KRITISCHER FIX: Stelle sicher dass Content sichtbar ist === */
    body, html {
        overflow-y: auto !important;
        overflow-x: hidden !important;
        min-height: 100vh !important;
        height: auto !important;
    }
    
    .tools-grid,
    .tools-container,
    .tool-card {
        display: grid !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    .tool-card {
        display: block !important;
    }
    
"""
    content = content.replace('</style>', critical_fix + '\n  </style>')
    fixes.append("✅ Kritischer CSS-Fix hinzugefügt")

# Speichere gefixte Datei
output_file = SCRIPT_DIR / "produkte_fixed.html"
output_file.write_text(content, encoding='utf-8')

print("Angewendete Fixes:")
for fix in fixes:
    print(f"   {fix}")
print()

print(f"📊 Dateigröße: {original_size:,} → {len(content):,} Zeichen")
print(f"   Datei gespeichert als: {output_file.name}")
print()

# Finale Prüfung
remaining = []
if 'display: none !important' in content.lower():
    remaining.append("❌ display: none !important noch vorhanden")
if content.lower().count('display: none') > 10:  # Erlaubt einige für spezielle Fälle
    remaining.append(f"⚠️  Noch {content.lower().count('display: none')} display: none gefunden")

if remaining:
    print("⚠️  VERBLEIBENDE PROBLEME:")
    for issue in remaining:
        print(f"   {issue}")
else:
    print("✅ Alle kritischen Probleme behoben!")
    print()
    print("📤 Bereit zum Upload!")
