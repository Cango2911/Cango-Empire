#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vergleiche index.html und cango-empire-v4-monopoly.html
"""

import ftplib
from io import BytesIO
import hashlib

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

TARGET_DIR = "/docker/nginx-proxy-manager-5tiw/www"

def get_file_hash(ftp, filename):
    """Lade Datei und berechne Hash"""
    try:
        file_data = BytesIO()
        ftp.retrbinary(f'RETR {filename}', file_data.write)
        content = file_data.getvalue()
        return hashlib.md5(content).hexdigest(), len(content)
    except:
        return None, 0

def main():
    print("=" * 70)
    print("🔍 VERGLEICHE HTML-DATEIEN")
    print("=" * 70)
    print()
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        print("✅ FTP-Verbindung hergestellt\n")
    except Exception as e:
        print(f"❌ FTP-Fehler: {e}")
        return
    
    try:
        ftp.cwd(TARGET_DIR)
        
        # Vergleiche Dateien
        print("📋 Vergleiche Dateien...")
        hash1, size1 = get_file_hash(ftp, "index.html")
        hash2, size2 = get_file_hash(ftp, "cango-empire-v4-monopoly.html")
        
        print(f"   index.html: {size1} Bytes, Hash: {hash1}")
        print(f"   cango-empire-v4-monopoly.html: {size2} Bytes, Hash: {hash2}")
        
        if hash1 == hash2:
            print("\n   ✅ Dateien sind IDENTISCH")
        else:
            print("\n   ⚠️  Dateien sind UNTERSCHIEDLICH")
            print("   💡 Kopiere cango-empire-v4-monopoly.html als index.html...")
            
            # Kopiere Datei
            file_data = BytesIO()
            ftp.retrbinary('RETR cango-empire-v4-monopoly.html', file_data.write)
            file_data.seek(0)
            ftp.storbinary('STOR index.html', file_data)
            ftp.sendcmd('SITE CHMOD 644 index.html')
            
            print("   ✅ index.html aktualisiert")
            
            # Prüfe erneut
            hash1_new, size1_new = get_file_hash(ftp, "index.html")
            if hash1_new == hash2:
                print("   ✅ Dateien sind jetzt identisch")
            else:
                print("   ⚠️  Dateien sind immer noch unterschiedlich")
        
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print("✅ VERGLEICH ABGESCHLOSSEN")
    print("=" * 70)
    print()
    print("💡 Falls die Schrift immer noch falsch ist:")
    print("   1. Leere den Browser-Cache (Strg+Shift+Delete)")
    print("   2. Teste im Inkognito-Modus")
    print("   3. Prüfe ob Google Fonts geladen werden (Browser DevTools)")

if __name__ == '__main__':
    main()
