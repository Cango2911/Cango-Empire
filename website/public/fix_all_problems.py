#!/usr/bin/env python3
"""
🔧 FIX ALLE PROBLEME
====================
Behebt alle gefundenen Probleme in produkte.html
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

# Prüfe welche Datei gefixt werden soll
produkte_file = SCRIPT_DIR / "produkte_server.html"
if not produkte_file.exists():
    produkte_file = SCRIPT_DIR / "produkte.html"

print("=" * 60)
print("🔧 FIX ALLE PROBLEME")
print("=" * 60)
print()
print(f"📁 Datei: {produkte_file.name}")
print()

content = produkte_file.read_text(encoding='utf-8')
original_size = len(content)
fixes = []

# Fix 1: Entferne display: none !important
if 'display: none !important' in content or 'display:none !important' in content:
    content = re.sub(
        r'display\s*:\s*none\s*!important',
        'display: block !important',
        content,
        flags=re.IGNORECASE
    )
    fixes.append("✅ display: none !important → display: block !important")

# Fix 2: Entferne display: none (außer in @media print)
# Ersetze display: none mit display: block (außer in print media queries)
content = re.sub(
    r'(?<!@media[^{]*print[^{]*\{[^}]*)(?<!@media[^{]*print[^{]*\{[^}]*\{[^}]*)(?<!@media[^{]*print[^{]*\{[^}]*\{[^}]*\{[^}]*)(?<!@media[^{]*print[^{]*\{[^}]*\{[^}]*\{[^}]*\{[^}]*)(?<!@media[^{]*print[^{]*\{[^}]*\{[^}]*\{[^}]*\{[^}]*\{[^}]*)display\s*:\s*none(?!\s*!important)',
    'display: block',
    content,
    flags=re.IGNORECASE
)
if 'display: none' not in content.lower() or content.lower().count('display: none') < 2:
    fixes.append("✅ display: none entfernt (außer in print media)")

# Fix 3: body overflow: hidden → overflow-y: auto
body_match = re.search(r'body\s*\{[^}]*\}', content, re.DOTALL)
if body_match:
    body_css = body_match.group(0)
    if 'overflow' in body_css and 'hidden' in body_css:
        if 'overflow-y: auto' not in body_css:
            new_body = body_css.replace('overflow: hidden', 'overflow-y: auto').replace('overflow-x: hidden', 'overflow-x: hidden')
            content = content.replace(body_css, new_body)
            fixes.append("✅ body overflow: hidden → overflow-y: auto")
        else:
            fixes.append("ℹ️  body hat bereits overflow-y: auto")

# Fix 4: tools-container max-height: 80vh entfernen/anpassen
if 'tools-container' in content and 'max-height: 80vh' in content:
    content = re.sub(
        r'\.tools-container[^{]*\{[^}]*max-height\s*:\s*80vh[^}]*\}',
        lambda m: m.group(0).replace('max-height: 80vh', 'max-height: none'),
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ tools-container max-height: 80vh → max-height: none")

# Fix 5: Stelle sicher dass tools-grid sichtbar ist
if '.tools-grid' in content:
    tools_grid_match = re.search(r'\.tools-grid[^{]*\{[^}]*\}', content, re.DOTALL)
    if tools_grid_match:
        tools_grid_css = tools_grid_match.group(0)
        if 'display: none' in tools_grid_css or 'display:none' in tools_grid_css:
            new_tools_grid = tools_grid_css.replace('display: none', 'display: grid').replace('display:none', 'display: grid')
            content = content.replace(tools_grid_css, new_tools_grid)
            fixes.append("✅ .tools-grid display: none → display: grid")
        elif 'display: grid' not in tools_grid_css:
            # Füge display: grid hinzu falls nicht vorhanden
            new_tools_grid = tools_grid_css.replace('{', '{ display: grid; ')
            content = content.replace(tools_grid_css, new_tools_grid)
            fixes.append("✅ .tools-grid display: grid hinzugefügt")

# Fix 6: Stelle sicher dass tool-card sichtbar ist
if '.tool-card' in content:
    tool_card_match = re.search(r'\.tool-card[^{]*\{[^}]*\}', content, re.DOTALL)
    if tool_card_match:
        tool_card_css = tool_card_match.group(0)
        if 'display: none' in tool_card_css or 'display:none' in tool_card_css:
            new_tool_card = tool_card_css.replace('display: none', 'display: block').replace('display:none', 'display: block')
            content = content.replace(tool_card_css, new_tool_card)
            fixes.append("✅ .tool-card display: none → display: block")

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

# Prüfe ob noch Probleme vorhanden
remaining_issues = []
if 'display: none !important' in content.lower():
    remaining_issues.append("❌ display: none !important noch vorhanden")
if content.count('display: none') > 5:  # Erlaubt einige für print media
    remaining_issues.append(f"⚠️  Noch {content.count('display: none')} display: none gefunden")

if remaining_issues:
    print("⚠️  VERBLEIBENDE PROBLEME:")
    for issue in remaining_issues:
        print(f"   {issue}")
else:
    print("✅ Alle kritischen Probleme behoben!")
