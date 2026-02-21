#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LAYOUT FIX: Sections untereinander statt nebeneinander
"""

from pathlib import Path
import re
import ftplib

LOCAL_DIR = Path("/Users/canberkkivilcim/Cango Universal")

HTML_FILES = [
    "ueber-uns.html",
    "produkte.html", 
    "kontakt.html",
    "blogs.html",
    "marktplatz.html",
    "cango-empire-v4-monopoly.html"
]

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOTS = [
    "/htdocs/automation-cango-app-empire.com/",
    "/public_html/",
    "/domains/automation-cango-app-empire.com/public_html/",
    "/files/"
]

def fix_layout(filepath):
    """Fixt das Layout-Problem - Sections untereinander"""
    if not filepath.exists():
        return None, f"Datei nicht gefunden: {filepath}"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    fixes = []
    
    # === ENTFERNE ALTE LAYOUT-FIXES ===
    patterns_to_remove = [
        r'/\*\s*={10,}\s*\n\s*GLOBALER NAVIGATION.*?\n\s*={10,}\s*\*/\s*(?:.*?\n)*?footer\s*\{[^}]*\}',
        r'/\*\s*={10,}\s*\n\s*LAYOUT FIX.*?\n\s*={10,}\s*\*/\s*(?:.*?\n)*?\*/\s*\{[^}]*\}',
        r'/\*\s*={10,}\s*\n\s*FINAL LAYOUT FIX.*?\n\s*={10,}\s*\*/\s*(?:.*?\n)*?\}\s*\}',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    fixes.append("Alte Layout-Fixes entfernt")
    
    # === FIX: Layout für Sections untereinander ===
    layout_fix = '''
/* ============================================
   FINAL LAYOUT FIX - SECTIONS UNTEREINANDER
   ============================================ */

html, body {
  overflow-x: hidden !important;
}

body {
  display: block !important;
  min-height: 100vh !important;
}

/* Sektionen MÜSSEN untereinander sein */
section,
.hero,
.manifest,
.revolution,
.arsenal,
.allianz,
.founder,
.cta,
footer {
  display: block !important;
  width: 100% !important;
  clear: both !important;
  float: none !important;
  position: relative !important;
  box-sizing: border-box !important;
}

/* Container zentrieren aber nicht nebeneinander */
.container {
  display: block !important;
  width: 100% !important;
  max-width: 1200px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  box-sizing: border-box !important;
}

/* Grid-Layouts nur für INHALT, nicht für Sektionen */
.manifest__grid { 
  display: grid !important; 
  grid-template-columns: repeat(2, 1fr) !important; 
  gap: 1.5rem !important;
}

.arsenal__grid { 
  display: grid !important; 
  grid-template-columns: repeat(3, 1fr) !important; 
  gap: 1.5rem !important;
}

.industries__grid { 
  display: grid !important; 
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)) !important; 
  gap: 1.5rem !important;
}

.founder__content { 
  display: grid !important; 
  grid-template-columns: 280px 1fr !important; 
  gap: 2rem !important;
}

/* Navigation volle Breite */
.nav {
  width: 100vw !important;
  max-width: 100vw !important;
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 9999 !important;
}

.nav__inner {
  width: 100% !important;
  max-width: 1400px !important;
  margin: 0 auto !important;
  padding: 0 2rem !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
}

.nav__menu {
  display: flex !important;
  gap: 1.5rem !important;
}

/* Scrolling erlauben */
html {
  overflow-y: scroll !important;
  overflow-x: hidden !important;
}

body {
  overflow-y: auto !important;
  overflow-x: hidden !important;
}

/* Responsive: Alles untereinander auf Mobile */
@media (max-width: 1024px) {
  .manifest__grid,
  .arsenal__grid,
  .industries__grid,
  .founder__content {
    grid-template-columns: 1fr !important;
  }
}
'''
    
    # Entferne alten Fix falls vorhanden
    if 'FINAL LAYOUT FIX - SECTIONS UNTEREINANDER' in content:
        # Ersetze den alten Fix
        content = re.sub(
            r'/\*\s*={10,}\s*\n\s*FINAL LAYOUT FIX.*?\n\s*={10,}\s*\*/\s*(?:.*?\n)*?\}\s*\}',
            layout_fix,
            content,
            flags=re.DOTALL
        )
        fixes.append("Layout-Fix aktualisiert")
    else:
        # Füge neuen Fix hinzu
        content = content.replace('</style>', layout_fix + '\n  </style>')
        fixes.append("Layout-Fix hinzugefügt")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return fixes, None
    else:
        return [], "Keine Änderungen nötig"

def upload_file(filepath, filename):
    """Lädt eine Datei auf alle Document Roots hoch"""
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        
        uploaded = []
        for docroot in DOC_ROOTS:
            try:
                ftp.cwd(docroot)
                with open(filepath, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
                try:
                    ftp.sendcmd(f'SITE CHMOD 644 {filename}')
                except:
                    pass
                uploaded.append(docroot)
            except Exception as e:
                pass
        
        ftp.quit()
        return uploaded
    except Exception as e:
        return []

def main():
    print("=" * 70)
    print("🔧 LAYOUT FIX: SECTIONS UNTEREINANDER")
    print("=" * 70)
    print()
    
    results = []
    
    for filename in HTML_FILES:
        filepath = LOCAL_DIR / filename
        print(f"📄 Bearbeite: {filename}")
        
        fixes, error = fix_layout(filepath)
        
        if error and "nicht gefunden" in error:
            print(f"   ⚠️  {error}")
            continue
        elif error:
            print(f"   ℹ️  {error}")
            results.append((filename, [], []))
        else:
            print(f"   ✅ Fixes: {', '.join(fixes)}")
            # Upload
            uploaded = upload_file(filepath, filename)
            print(f"   ✅ Hochgeladen zu: {len(uploaded)} Verzeichnisse")
            results.append((filename, fixes, uploaded))
        print()
    
    print("=" * 70)
    print("📊 ZUSAMMENFASSUNG")
    print("=" * 70)
    for filename, fixes, uploaded in results:
        status = "✅" if fixes else "⏭️"
        print(f"{status} {filename}: {len(fixes)} Fixes, {len(uploaded)} Uploads")
    print()
    print("🚨 WICHTIG - JETZT TESTEN:")
    print("   1. Chrome Cache leeren: Cmd+Shift+Delete")
    print("   2. ALLE Inkognito-Fenster schließen")
    print("   3. NEUES Inkognito-Fenster: Cmd+Shift+N")
    print("   4. Testen:")
    print("      ✓ automation-cango-app-empire.com/ueber-uns.html")
    print("      ✓ automation-cango-app-empire.com/produkte.html")
    print()
    print("   Prüfen:")
    print("      → Sections sind UNTEREINANDER (nicht nebeneinander)")
    print("      → Navigation vollständig ausgebreitet")
    print("      → Scrolling funktioniert")
    print()

if __name__ == '__main__':
    main()
