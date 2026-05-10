#!/usr/bin/env python3
"""
🔍 PROBLEMANALYSE produkte.html
===============================
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent
file_path = SCRIPT_DIR / "produkte.html"

if not file_path.exists():
    print(f"❌ {file_path} nicht gefunden!")
    exit(1)

content = file_path.read_text(encoding='utf-8')

problems = []
warnings = []
info = []

# 1. Prüfe auf display: none in tool-card
if 'display: none' in content or 'display:none' in content:
    # Prüfe ob es in tool-card Kontext ist
    if 'tool-card' in content and ('display: none' in content or 'display:none' in content):
        problems.append("❌ display: none gefunden - könnte Tool-Cards verstecken")
    else:
        warnings.append("⚠️  display: none gefunden (möglicherweise in anderen Elementen)")

# 2. Prüfe auf overflow: hidden am body
if 'body {' in content:
    body_match = re.search(r'body\s*\{[^}]*\}', content, re.DOTALL)
    if body_match:
        body_css = body_match.group(0)
        if 'overflow' in body_css:
            if 'overflow: hidden' in body_css or 'overflow:hidden' in body_css:
                if 'overflow-y: auto' not in body_css:
                    problems.append("❌ body hat overflow: hidden ohne overflow-y: auto - blockiert Scrollen")
                else:
                    info.append("ℹ️  body hat overflow: hidden aber auch overflow-y: auto")
            elif 'overflow-y: auto' in body_css:
                info.append("✅ body hat overflow-y: auto - Scrollen sollte funktionieren")
        else:
            warnings.append("⚠️  body hat kein overflow Property definiert")

# 3. Prüfe auf kritische JavaScript-Fehler
if 'loadToolLogos' in content:
    info.append("ℹ️  Logo-Loading Script vorhanden")
    # Prüfe ob es korrekt implementiert ist
    if 'document.querySelectorAll(\'.tool-card\')' in content:
        info.append("   ✅ Tool-Card Selector vorhanden")
    else:
        warnings.append("   ⚠️  Tool-Card Selector möglicherweise falsch")

# 4. Prüfe auf tools-container styles
if 'tools-container' in content:
    if 'max-height: 80vh' in content:
        warnings.append("⚠️  tools-container hat max-height: 80vh - könnte Content abschneiden")
    if 'overflow-y: auto' in content:
        info.append("ℹ️  tools-container hat overflow-y: auto")

# 5. Zähle Tool-Cards
tool_card_count = content.count('class="tool-card"')
info.append(f"ℹ️  {tool_card_count} Tool-Cards gefunden")

# 6. Prüfe ob main oder section display: none hat
if 'display: none !important' in content:
    problems.append("❌ KRITISCH: display: none !important gefunden - versteckt Elemente")
elif 'display: none' in content:
    # Prüfe Kontext
    display_none_matches = re.findall(r'[^{]*\{[^}]*display\s*:\s*none[^}]*\}', content, re.DOTALL)
    if display_none_matches:
        for match in display_none_matches[:3]:  # Zeige erste 3
            if 'tool-card' in match or 'tools-grid' in match or 'main' in match:
                problems.append(f"❌ display: none in kritischem Element: {match[:100]}...")

# 7. Prüfe auf visibility: hidden
if 'visibility: hidden' in content:
    visibility_matches = re.findall(r'[^{]*\{[^}]*visibility\s*:\s*hidden[^}]*\}', content, re.DOTALL)
    if visibility_matches:
        for match in visibility_matches[:3]:
            if 'tool-card' in match or 'tools-grid' in match:
                problems.append(f"❌ visibility: hidden in kritischem Element")

# 8. Prüfe auf opacity: 0
if 'opacity: 0' in content or 'opacity:0' in content:
    opacity_matches = re.findall(r'[^{]*\{[^}]*opacity\s*:\s*0[^}]*\}', content, re.DOTALL)
    if opacity_matches:
        for match in opacity_matches[:3]:
            if 'tool-card' in match or 'tools-grid' in match:
                warnings.append(f"⚠️  opacity: 0 in Element - könnte unsichtbar sein")

# 9. Prüfe HTML-Struktur
if '<body' not in content:
    problems.append("❌ KRITISCH: Kein <body> Tag gefunden!")
elif content.count('<body') > 1:
    problems.append(f"❌ KRITISCH: Mehrere <body> Tags gefunden: {content.count('<body')}")

if '</body>' not in content:
    problems.append("❌ KRITISCH: Kein </body> Tag gefunden!")

# 10. Prüfe ob tools-grid sichtbar ist
if '.tools-grid' in content:
    tools_grid_match = re.search(r'\.tools-grid[^{]*\{[^}]*\}', content, re.DOTALL)
    if tools_grid_match:
        tools_grid_css = tools_grid_match.group(0)
        if 'display: none' in tools_grid_css or 'display:none' in tools_grid_css:
            problems.append("❌ KRITISCH: .tools-grid hat display: none!")
        elif 'display: grid' in tools_grid_css:
            info.append("✅ .tools-grid hat display: grid")
        else:
            warnings.append("⚠️  .tools-grid hat kein display Property")

print("=" * 60)
print("🔍 PROBLEMANALYSE produkte.html")
print("=" * 60)
print()

if problems:
    print("❌ KRITISCHE PROBLEME:")
    for p in problems:
        print(f"   {p}")
    print()

if warnings:
    print("⚠️  WARNUNGEN:")
    for w in warnings:
        print(f"   {w}")
    print()

if info:
    print("ℹ️  INFORMATIONEN:")
    for i in info:
        print(f"   {i}")
    print()

print(f"📊 Dateigröße: {len(content):,} Zeichen")
print(f"   Zeilen: {content.count(chr(10)):,}")
print(f"   <body> Tags: {content.count('<body')}")
print(f"   </body> Tags: {content.count('</body>')}")
print()

if not problems:
    print("✅ Keine kritischen Probleme gefunden!")
else:
    print("❌ KRITISCHE PROBLEME GEFUNDEN - Datei muss gefixt werden!")
