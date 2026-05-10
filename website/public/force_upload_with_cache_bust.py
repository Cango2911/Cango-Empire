#!/usr/bin/env python3
"""
🚀 FORCE UPLOAD mit Cache-Busting
==================================
"""

import ftplib
from pathlib import Path
import time

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
SCRIPT_DIR = Path(__file__).parent

print("=" * 60)
print("🚀 FORCE UPLOAD mit Cache-Busting")
print("=" * 60)
print()

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print("✅ FTP verbunden")
    print()
    
    # Upload produkte.html
    print("📤 Lade produkte.html hoch...")
    with open(SCRIPT_DIR / "produkte.html", 'rb') as f:
        ftp.storbinary('STOR produkte.html', f)
    
    # Warte kurz
    time.sleep(1)
    
    # Lösche alte Version (falls vorhanden)
    try:
        ftp.delete('produkte.html.bak')
    except:
        pass
    
    # Setze Berechtigungen
    try:
        ftp.sendcmd('SITE CHMOD 644 produkte.html')
        print("   ✅ produkte.html hochgeladen + Berechtigungen")
    except:
        print("   ✅ produkte.html hochgeladen")
    
    print()
    
    # Upload ueber-uns.html
    print("📤 Lade ueber-uns.html hoch...")
    with open(SCRIPT_DIR / "ueber-uns.html", 'rb') as f:
        ftp.storbinary('STOR ueber-uns.html', f)
    
    # Setze Berechtigungen
    try:
        ftp.sendcmd('SITE CHMOD 644 ueber-uns.html')
        print("   ✅ ueber-uns.html hochgeladen + Berechtigungen")
    except:
        print("   ✅ ueber-uns.html hochgeladen")
    
    print()
    
    # Verifiziere Upload
    print("🔍 Verifiziere Upload...")
    try:
        size = ftp.size('produkte.html')
        local_size = (SCRIPT_DIR / "produkte.html").stat().st_size
        print(f"   produkte.html: Server={size:,} Bytes, Lokal={local_size:,} Bytes")
        if size == local_size:
            print("   ✅ Größe stimmt überein")
        else:
            print(f"   ⚠️  Größe unterscheidet sich um {abs(size - local_size)} Bytes")
    except:
        print("   ⚠️  Größe nicht prüfbar")
    
    ftp.quit()
    
    print()
    print("=" * 60)
    print("✅ UPLOAD ABGESCHLOSSEN!")
    print("=" * 60)
    print()
    print("🧪 WICHTIG: Cache leeren!")
    print("   1. Chrome: Cmd+Shift+R (Hard Refresh)")
    print("   2. Oder: Chrome DevTools → Network → 'Disable cache' aktivieren")
    print("   3. Oder: Chrome → Einstellungen → Datenschutz → Browserdaten löschen")
    print()
    print("📋 Teste jetzt:")
    print("   - https://automation-cango-app-empire.com/produkte.html")
    print("   - https://automation-cango-app-empire.com/ueber-uns.html")
    print()
    
except Exception as e:
    print(f"❌ Fehler: {e}")
    import traceback
    traceback.print_exc()
