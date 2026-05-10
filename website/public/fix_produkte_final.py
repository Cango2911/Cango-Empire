#!/usr/bin/env python3
"""
🔧 FINALE KORREKTUR produkte.html
==================================
Entfernt alle display: none !important
Fixe kritische Probleme
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

# Finde die große produkte.html Datei (die mit Problemen)
produkte_file = SCRIPT_DIR / "produkte_complete.html"
if not produkte_file.exists():
    # Prüfe ob es eine andere große Version gibt
    for f in SCRIPT_DIR.glob("produkte*.html"):
        size = f.stat().st_size
        if size > 30000:  # Größer als 30KB
            produkte_file = f
            break

if not produkte_file.exists():
    print("❌ Keine große produkte.html Datei gefunden!")
    print("   Suche nach produkte_complete.html oder ähnlichen Dateien...")
    exit(1)

print("=" * 60)
print("🔧 FINALE KORREKTUR produkte.html")
print("=" * 60)
print()
print(f"📁 Datei: {produkte_file.name}")
print(f"   Größe: {produkte_file.stat().st_size:,} Bytes")
print()

content = produkte_file.read_text(encoding='utf-8')
original_size = len(content)
fixes = []

# Fix 1: Entferne display: none !important von .tool-card__icon
# Aber behalte die Struktur bei, nur das Verstecken entfernen
icon_matches = len(re.findall(r'\.tool-card__icon\s*\{[^}]*display\s*:\s*none\s*!important[^}]*\}', content, re.DOTALL))
if icon_matches > 0:
    content = re.sub(
        r'\.tool-card__icon\s*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'.tool-card__icon { display: flex !important; align-items: center; justify-content: center; visibility: visible !important; }',
        content,
        flags=re.DOTALL
    )
    fixes.append(f"✅ {icon_matches}x .tool-card__icon display: none !important → display: flex")

# Fix 2: Entferne alle anderen display: none !important
count_before = content.count('display: none !important') + content.count('display:none !important')
if count_before > 0:
    content = content.replace('display: none !important', 'display: block !important')
    content = content.replace('display:none !important', 'display: block !important')
    fixes.append(f"✅ {count_before}x display: none !important → display: block !important")

# Fix 3: Stelle sicher, dass body overflow-y: auto hat (nicht hidden)
body_match = re.search(r'body\s*\{[^}]*\}', content, re.DOTALL)
if body_match:
    body_css = body_match.group(0)
    if 'overflow' in body_css:
        if 'overflow-y: auto' not in body_css and 'overflow-y:auto' not in body_css:
            # Ersetze overflow: hidden mit overflow-y: auto
            new_body = body_css.replace('overflow: hidden', 'overflow-y: auto !important')
            new_body = new_body.replace('overflow-x: hidden', 'overflow-x: hidden')
            if 'overflow-y: auto' not in new_body:
                new_body = new_body.replace('{', '{ overflow-y: auto !important; ')
            content = content.replace(body_css, new_body)
            fixes.append("✅ body overflow: hidden → overflow-y: auto !important")
    else:
        # Füge overflow-y hinzu
        new_body = body_css.replace('{', '{ overflow-y: auto !important; overflow-x: hidden; ')
        content = content.replace(body_css, new_body)
        fixes.append("✅ body overflow-y: auto !important hinzugefügt")

# Fix 4: Entferne max-height vom tools-container oder erhöhe es drastisch
if 'tools-container' in content and 'max-height: 80vh' in content:
    content = re.sub(
        r'(\.tools-container[^{]*\{[^}]*)max-height\s*:\s*80vh',
        r'\1max-height: none',
        content,
        flags=re.DOTALL
    )
    fixes.append("✅ tools-container max-height: 80vh → max-height: none")

# Fix 5: Füge kritischen CSS-Fix am Anfang des <style> Tags ein
critical_fix = """
    /* === KRITISCHER FIX: Stelle sicher dass alles sichtbar ist === */
    body, html {
        overflow-y: auto !important;
        overflow-x: hidden !important;
        min-height: 100vh !important;
        height: auto !important;
    }
    
    .produkte-page,
    .produkte-hero,
    .tools-section,
    .tools-container,
    .tools-grid,
    .tool-card {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    .tools-grid {
        display: grid !important;
    }
    
    .tool-card {
        display: flex !important;
        flex-direction: column !important;
    }
    
    .tool-card__icon {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
"""

# Füge den Fix nach dem ersten <style> Tag ein
if '<style>' in content:
    content = content.replace('<style>', '<style>' + critical_fix, 1)
    fixes.append("✅ Kritischer CSS-Fix eingefügt")

# Fix 6: Stelle sicher dass html overflow-y hat
html_match = re.search(r'html\s*\{[^}]*\}', content, re.DOTALL)
if html_match:
    html_css = html_match.group(0)
    if 'overflow-y: auto' not in html_css:
        new_html = html_css.replace('{', '{ overflow-y: auto !important; ')
        content = content.replace(html_css, new_html)
        fixes.append("✅ html overflow-y: auto !important hinzugefügt")

# Fix 7: Deaktiviere das problematische Logo-Loading-Script temporär (optional)
# Kommentiere es aus statt zu löschen
if 'function loadToolLogos' in content:
    # Kommentiere die Funktion aus
    content = re.sub(
        r'(function loadToolLogos\(\)\s*\{)',
        r'// TEMPORÄR DEAKTIVIERT FÜR DEBUGGING\n    // \1',
        content,
        flags=re.DOTALL
    )
    # Kommentiere auch den Aufruf aus
    content = re.sub(
        r'(loadToolLogos\(\))',
        r'// \1 // TEMPORÄR DEAKTIVIERT',
        content
    )
    fixes.append("⚠️  Logo-Loading Script temporär deaktiviert (zum Testen)")

# Speichere korrigierte Version
output_file = SCRIPT_DIR / "produkte_fixed_final.html"
output_file.write_text(content, encoding='utf-8')

print("Angewendete Fixes:")
for fix in fixes:
    print(f"   {fix}")
print()

print(f"📊 Dateigröße: {original_size:,} → {len(content):,} Zeichen")
print(f"   Datei gespeichert als: {output_file.name}")
print()

# Finale Validierung
print("🔍 Finale Validierung...")
validation_errors = []

if '<body' not in content:
    validation_errors.append("❌ Kein <body> Tag gefunden!")
elif content.count('<body') > 1:
    validation_errors.append(f"⚠️  Mehrere <body> Tags: {content.count('<body')}")

if '</body>' not in content:
    validation_errors.append("❌ Kein </body> Tag gefunden!")

if 'display: none !important' in content.lower():
    validation_errors.append("❌ display: none !important noch vorhanden!")

if 'overflow-y: auto' not in content:
    validation_errors.append("⚠️  overflow-y: auto nicht gefunden!")

if validation_errors:
    print("⚠️  VALIDIERUNGSFEHLER:")
    for error in validation_errors:
        print(f"   {error}")
else:
    print("✅ Validierung erfolgreich!")
    print()
    print("📤 Bereit zum Upload!")
    print()
    print("📋 Nächste Schritte:")
    print("   1. Kopiere produkte_fixed_final.html → produkte.html")
    print("   2. Führe bulletproof_upload.py aus")
    print("   3. Cache leeren (Cmd+Shift+R)")
    print("   4. Testen!")
