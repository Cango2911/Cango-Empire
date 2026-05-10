#!/usr/bin/env python3
"""
📤 Upload nur der gefixten Dateien
==================================
"""

import ftplib
from pathlib import Path

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
SCRIPT_DIR = Path(__file__).parent

print("=" * 60)
print("📤 Upload gefixte Dateien")
print("=" * 60)
print()

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print("✅ FTP verbunden")
    print()
    
    # Upload nur produkte.html und ueber-uns.html
    files_to_upload = ["produkte.html", "ueber-uns.html"]
    
    for filename in files_to_upload:
        file_path = SCRIPT_DIR / filename
        if file_path.exists():
            print(f"📤 Lade {filename} hoch...")
            with open(file_path, 'rb') as f:
                ftp.storbinary(f'STOR {filename}', f)
            
            # Setze Berechtigungen
            try:
                ftp.sendcmd(f'SITE CHMOD 644 {filename}')
                print(f"   ✅ {filename} hochgeladen + Berechtigungen gesetzt")
            except:
                print(f"   ✅ {filename} hochgeladen")
        else:
            print(f"   ⚠️  {filename} nicht gefunden")
    
    ftp.quit()
    
    print()
    print("=" * 60)
    print("✅ UPLOAD ABGESCHLOSSEN!")
    print("=" * 60)
    print()
    print("🧪 Teste jetzt:")
    print("   1. Hard Refresh: Cmd+Shift+R")
    print("   2. Teste beide Seiten")
    print()
    
except Exception as e:
    print(f"❌ Fehler: {e}")
    import traceback
    traceback.print_exc()
