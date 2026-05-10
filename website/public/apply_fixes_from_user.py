#!/usr/bin/env python3
"""
🔧 Wende Fixes an (basierend auf User-Script)
=============================================
"""

from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent

# Finde die Datei mit Problemen (die große Version)
produkte_file = None
for f in SCRIPT_DIR.glob("produkte*.html"):
    size = f.stat().st_size
    if size > 30000:  # Größer als 30KB
        content = f.read_text(encoding='utf-8')
        if len(content) > 100000:  # Über 100K Zeichen
            produkte_file = f
            break

if not produkte_file:
    print("❌ Keine große produkte.html Datei gefunden!")
    print("   Suche nach Dateien > 100K Zeichen...")
    exit(1)

print("=" * 60)
print("🔧 WENDE FIXES AN")
print("=" * 60)
print()
print(f"📁 Datei: {produkte_file.name}")
print(f"   Größe: {len(produkte_file.read_text(encoding='utf-8')):,} Zeichen")
print()

content = produkte_file.read_text(encoding='utf-8')
original_size = len(content)
fixes = []

# Fix 1: Entferne display: none !important von .tool-card__icon
icon_matches = len(re.findall(r'\.tool-card__icon\s*\{[^}]*display\s*:\s*none\s*!important[^}]*\}', content, re.DOTALL))
if icon_matches > 0:
    content = re.sub(
        r'\.tool-card__icon\s*\{[^}]*display\s*:\s*none\s*!important[^}]*\}',
        r'.tool-card__icon { display: flex !important; align-items: center; justify-content: center; }',
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

# Fix 3: Stelle sicher, dass body overflow-y: auto hat
body_match = re.search(r'body\s*\{([^}]*)\}', content, re.DOTALL)
if body_match:
    body_content = body_match.group(1)
    if 'overflow' in body_content:
        if 'overflow-y: auto' not in body_content and 'overflow-y:auto' not in body_content:
            # Ersetze overflow: hidden mit overflow-y: auto
            new_body = body_match.group(0).replace('overflow: hidden', 'overflow-y: auto !important')
            new_body = new_body.replace('overflow-x: hidden', 'overflow-x: hidden')
            if 'overflow-y: auto' not in new_body:
                new_body = new_body.replace('{', '{ overflow-y: auto !important; ')
            content = content.replace(body_match.group(0), new_body)
            fixes.append("✅ body overflow: hidden → overflow-y: auto !important")
    else:
        # Füge overflow-y hinzu
        new_body = body_match.group(0).replace('{', '{ overflow-y: auto !important; overflow-x: hidden; ')
        content = content.replace(body_match.group(0), new_body)
        fixes.append("✅ body overflow-y: auto !important hinzugefügt")

# Fix 4: Entferne max-height vom tools-container
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
    }
    
    .tool-card__icon {
        display: flex !important;
        visibility: visible !important;
    }
"""

if '<style>' in content:
    content = content.replace('<style>', '<style>' + critical_fix, 1)
    fixes.append("✅ Kritischer CSS-Fix eingefügt")

# Fix 6: Deaktiviere das problematische Logo-Loading-Script temporär
if 'function loadToolLogos' in content:
    # Ersetze die Funktion
    content = re.sub(
        r'function loadToolLogos\(\)\s*\{[^}]*\}',
        r'function loadToolLogos() { console.log("Logo loading disabled for debugging"); }',
        content,
        flags=re.DOTALL
    )
    # Kommentiere auch den Aufruf aus
    content = re.sub(
        r'loadToolLogos\(\)',
        r'// loadToolLogos() // TEMPORÄR DEAKTIVIERT',
        content
    )
    fixes.append("⚠️  Logo-Loading Script temporär deaktiviert (zum Testen)")

# Speichere korrigierte Version
output_file = SCRIPT_DIR / "produkte_fixed.html"
output_file.write_text(content, encoding='utf-8')

print("Angewendete Fixes:")
for fix in fixes:
    print(f"   {fix}")
print()

print(f"📊 Dateigröße: {original_size:,} → {len(content):,} Zeichen")
print(f"   Datei gespeichert als: {output_file.name}")
print()

# Prüfe ob <body> vorhanden ist
if '<body' in content:
    print("✅ <body> Tag vorhanden!")
    print()
    print("📤 Bereit zum Upload!")
    print()
    print("📋 Nächste Schritte:")
    print("   1. Kopiere produkte_fixed.html → produkte.html")
    print("   2. Führe bulletproof_upload.py aus")
    print("   3. Cache leeren (Cmd+Shift+R)")
    print("   4. Testen!")
else:
    print("❌ KEIN <body> Tag gefunden!")
    print("   Die Datei enthält nur CSS/JavaScript, kein HTML-Body!")
    print()
    print("💡 Lösung: Nutze die saubere Version (17K) die bereits funktioniert")
