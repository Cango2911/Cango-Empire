#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korrigiere index.html - sollte den Inhalt von cango-empire-v4-monopoly.html haben
"""

import ftplib
from io import BytesIO

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

TARGET_DIR = "/docker/nginx-proxy-manager-5tiw/www"

def main():
    print("=" * 70)
    print("🔧 KORRIGIERE INDEX.HTML")
    print("=" * 70)
    print()
    print("💡 index.html sollte den Inhalt von cango-empire-v4-monopoly.html haben")
    print()
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        print("✅ FTP-Verbindung hergestellt\n")
    except Exception as e:
        print(f"❌ FTP-Fehler: {e}")
        return
    
    # Lade cango-empire-v4-monopoly.html
    print("📥 Lade cango-empire-v4-monopoly.html...")
    try:
        ftp.cwd("/")
        file_data = BytesIO()
        ftp.retrbinary('RETR cango-empire-v4-monopoly.html', file_data.write)
        file_size = file_data.tell()
        file_data.seek(0)
        
        if file_size == 0:
            print("   ❌ Datei ist leer!")
            ftp.quit()
            return
        
        print(f"   ✅ Datei geladen ({file_size} Bytes)\n")
        
        # Speichere als index.html im Docker-Verzeichnis
        print("📤 Speichere als index.html...")
        ftp.cwd(TARGET_DIR)
        ftp.storbinary('STOR index.html', file_data)
        ftp.sendcmd('SITE CHMOD 644 index.html')
        
        print("   ✅ index.html aktualisiert\n")
        
        # Prüfe ob Datei korrekt ist
        print("🔍 Prüfe index.html...")
        items = []
        ftp.retrlines('LIST index.html', items.append)
        for item in items:
            if 'index.html' in item:
                print(f"   ✅ {item}")
        
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print("✅ INDEX.HTML KORRIGIERT")
    print("=" * 70)
    print()
    print("💡 Nächste Schritte:")
    print("   1. Warte 5-10 Sekunden")
    print("   2. Teste: http://31.97.56.197:8080/")
    print("   3. Falls nötig, Container neu starten:")
    print("      docker restart nginx-proxy-manager-5tiw-automation-cango-app-empire-web-1")

if __name__ == '__main__':
    main()
