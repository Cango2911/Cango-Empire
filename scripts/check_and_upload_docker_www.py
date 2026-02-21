#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfe und lade HTML-Dateien in das Docker www-Verzeichnis hoch
"""

import ftplib
import os

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

# Docker www-Verzeichnis
DOCKER_WWW_PATH = "/docker/nginx-proxy-manager-5tiw/www"

# Mögliche Quell-Verzeichnisse auf dem Server
SOURCE_PATHS = [
    "/",
    "/htdocs/automation-cango-app-empire.com",
    "/domains/automation-cango-app-empire.com/public_html",
    "/public_html",
    "/files",
    "/www"
]

HTML_FILES = [
    "index.html",
    "cango-empire-v4-monopoly.html",
    "produkte.html",
    "ueber-uns.html",
    "kontakt.html",
    "blogs.html",
    "marktplatz.html"
]

def find_files_on_server(ftp):
    """Finde HTML-Dateien auf dem Server"""
    found_files = {}
    
    for source_path in SOURCE_PATHS:
        try:
            ftp.cwd(source_path)
            items = []
            ftp.retrlines('LIST', items.append)
            
            for item in items:
                parts = item.split()
                if len(parts) < 9:
                    continue
                
                filename = ' '.join(parts[8:])
                if filename.endswith('.html') and filename in HTML_FILES:
                    if filename not in found_files:
                        found_files[filename] = source_path
                        print(f"   ✅ Gefunden: {source_path}/{filename}")
        except:
            pass
    
    return found_files

def copy_file_via_ftp(ftp, source_path, source_file, dest_path, dest_file):
    """Kopiert eine Datei über FTP"""
    try:
        # Wechsle ins Quell-Verzeichnis
        ftp.cwd(source_path)
        
        # Lade Datei in temporärem Speicher
        temp_data = []
        def callback(data):
            temp_data.append(data)
        
        ftp.retrbinary(f'RETR {source_file}', callback)
        
        # Wechsle ins Ziel-Verzeichnis
        ftp.cwd(dest_path)
        
        # Speichere Datei
        from io import BytesIO
        file_data = BytesIO(b''.join(temp_data))
        ftp.storbinary(f'STOR {dest_file}', file_data)
        
        # Setze Berechtigung
        ftp.sendcmd(f'SITE CHMOD 644 {dest_file}')
        
        print(f"   ✅ Kopiert: {source_file} → {dest_file}")
        return True
    except Exception as e:
        print(f"   ❌ Fehler beim Kopieren von {source_file}: {e}")
        return False

def main():
    print("=" * 70)
    print("🔍 SUCHE HTML-DATEIEN AUF DEM SERVER")
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
    
    # Finde Dateien auf dem Server
    print("🔍 Suche nach HTML-Dateien...")
    found_files = find_files_on_server(ftp)
    
    if not found_files:
        print("\n❌ Keine HTML-Dateien auf dem Server gefunden!")
        print("   💡 Du musst die Dateien zuerst auf den Server hochladen.")
        ftp.quit()
        return
    
    print(f"\n📋 Gefundene Dateien: {len(found_files)}/{len(HTML_FILES)}")
    print()
    
    # Prüfe ob Ziel-Verzeichnis existiert
    try:
        ftp.cwd(DOCKER_WWW_PATH)
        print(f"✅ Ziel-Verzeichnis existiert: {DOCKER_WWW_PATH}\n")
    except:
        print(f"⚠️  Ziel-Verzeichnis existiert nicht, erstelle es...")
        try:
            parts = DOCKER_WWW_PATH.strip('/').split('/')
            current_path = '/'
            for part in parts:
                current_path = os.path.join(current_path, part).replace('\\', '/')
                try:
                    ftp.cwd(current_path)
                except:
                    ftp.mkd(current_path)
                    ftp.cwd(current_path)
            print(f"✅ Verzeichnis erstellt: {DOCKER_WWW_PATH}\n")
        except Exception as e:
            print(f"❌ Fehler beim Erstellen: {e}")
            ftp.quit()
            return
    
    # Kopiere Dateien
    print("📤 Kopiere Dateien ins Docker www-Verzeichnis...")
    print()
    
    copied = 0
    for filename, source_path in found_files.items():
        print(f"📋 Kopiere {filename}...")
        if copy_file_via_ftp(ftp, source_path, filename, DOCKER_WWW_PATH, filename):
            copied += 1
    
    # Setze Verzeichnis-Berechtigung
    try:
        ftp.cwd(DOCKER_WWW_PATH)
        ftp.sendcmd('SITE CHMOD 755 .')
    except:
        pass
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print(f"✅ {copied}/{len(found_files)} DATEIEN KOPIERT")
    print("=" * 70)
    print()
    print("💡 Nächste Schritte:")
    print("   1. Warte 5-10 Sekunden")
    print("   2. Teste: http://31.97.56.197:8080/")
    print("   3. Prüfe Dateien im Container:")
    print("      docker exec nginx-proxy-manager-5tiw-automation-cango-app-empire-web-1 ls -lah /usr/share/nginx/html/")

if __name__ == '__main__':
    main()
