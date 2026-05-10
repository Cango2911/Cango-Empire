#!/usr/bin/env python3
"""
🔍 Prüfe Dateien auf dem Server
================================
"""

import ftplib
from pathlib import Path

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
SCRIPT_DIR = Path(__file__).parent

print("=" * 60)
print("🔍 Prüfe Dateien auf dem Server")
print("=" * 60)
print()

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print("✅ FTP verbunden")
    print()
    
    # Lade produkte.html herunter
    print("📥 Lade produkte.html vom Server...")
    with open(SCRIPT_DIR / "produkte_server.html", 'wb') as f:
        ftp.retrbinary('RETR produkte.html', f.write)
    print("   ✅ produkte.html heruntergeladen")
    
    # Lade ueber-uns.html herunter
    print("📥 Lade ueber-uns.html vom Server...")
    with open(SCRIPT_DIR / "ueber-uns_server.html", 'wb') as f:
        ftp.retrbinary('RETR ueber-uns.html', f.write)
    print("   ✅ ueber-uns.html heruntergeladen")
    
    ftp.quit()
    
    # Prüfe die Dateien
    print()
    print("🔍 Analysiere Dateien...")
    print()
    
    # Prüfe produkte.html
    prod_content = (SCRIPT_DIR / "produkte_server.html").read_text(encoding='utf-8')
    
    # Prüfe body overflow
    if 'overflow-y: auto' in prod_content or 'overflow-y:auto' in prod_content:
        print("   ✅ produkte.html hat overflow-y: auto")
    else:
        print("   ❌ produkte.html hat KEIN overflow-y: auto")
        # Zeige body-Style
        import re
        body_match = re.search(r'body\s*\{[^}]*\}', prod_content, re.DOTALL)
        if body_match:
            print(f"   Body-Style: {body_match.group(0)[:200]}...")
    
    # Prüfe ueber-uns.html
    ueber_content = (SCRIPT_DIR / "ueber-uns_server.html").read_text(encoding='utf-8')
    
    if 'overflow-y: auto' in ueber_content or 'overflow-y:auto' in ueber_content:
        print("   ✅ ueber-uns.html hat overflow-y: auto")
    else:
        print("   ❌ ueber-uns.html hat KEIN overflow-y: auto")
    
    print()
    print("=" * 60)
    print("✅ PRÜFUNG ABGESCHLOSSEN!")
    print("=" * 60)
    print()
    print("📁 Dateien gespeichert als:")
    print("   - produkte_server.html")
    print("   - ueber-uns_server.html")
    print()
    
except Exception as e:
    print(f"❌ Fehler: {e}")
    import traceback
    traceback.print_exc()
