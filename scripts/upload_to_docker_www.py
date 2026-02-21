#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lade HTML-Dateien in das Docker www-Verzeichnis hoch
Mount-Pfad: /docker/nginx-proxy-manager-5tiw/www
"""

import ftplib
import os
import time

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

# Docker www-Verzeichnis
DOCKER_WWW_PATH = "/docker/nginx-proxy-manager-5tiw/www"

# HTML-Dateien zum Hochladen
HTML_FILES = [
    "index.html",
    "cango-empire-v4-monopoly.html",
    "produkte.html",
    "ueber-uns.html",
    "kontakt.html",
    "blogs.html",
    "marktplatz.html"
]

def upload_file(ftp, local_path, remote_path):
    """Lädt eine Datei hoch"""
    try:
        with open(local_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)
        print(f"   ✅ {os.path.basename(local_path)} hochgeladen")
        return True
    except Exception as e:
        print(f"   ❌ Fehler beim Hochladen von {os.path.basename(local_path)}: {e}")
        return False

def set_permissions(ftp, path):
    """Setzt Berechtigungen für eine Datei"""
    try:
        ftp.sendcmd(f'SITE CHMOD 644 {path}')
        return True
    except:
        return False

def main():
    print("=" * 70)
    print("📤 LADE HTML-DATEIEN IN DOCKER WWW-VERZEICHNIS")
    print("=" * 70)
    print()
    print(f"📁 Ziel-Verzeichnis: {DOCKER_WWW_PATH}")
    print()
    
    # Finde lokale HTML-Dateien
    local_files = []
    workspace_path = "/Users/canberkkivilcim/OnlineAgentur CanGo"
    
    for html_file in HTML_FILES:
        local_path = os.path.join(workspace_path, html_file)
        if os.path.exists(local_path):
            local_files.append((html_file, local_path))
            print(f"   ✅ Gefunden: {html_file}")
        else:
            print(f"   ⚠️  Nicht gefunden: {html_file}")
    
    if not local_files:
        print("\n❌ Keine HTML-Dateien gefunden!")
        return
    
    print(f"\n📤 Lade {len(local_files)} Dateien hoch...")
    print()
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        print("✅ FTP-Verbindung hergestellt\n")
    except Exception as e:
        print(f"❌ FTP-Fehler: {e}")
        return
    
    # Wechsle ins Docker www-Verzeichnis
    try:
        # Versuche ins Verzeichnis zu wechseln
        ftp.cwd(DOCKER_WWW_PATH)
        print(f"✅ Im Verzeichnis: {DOCKER_WWW_PATH}\n")
    except:
        # Versuche Verzeichnis zu erstellen
        print(f"⚠️  Verzeichnis existiert nicht, versuche zu erstellen...")
        try:
            # Erstelle Verzeichnis-Struktur
            parts = DOCKER_WWW_PATH.strip('/').split('/')
            current_path = '/'
            for part in parts:
                current_path = os.path.join(current_path, part).replace('\\', '/')
                try:
                    ftp.cwd(current_path)
                except:
                    try:
                        ftp.mkd(current_path)
                        ftp.cwd(current_path)
                        print(f"   ✅ Verzeichnis erstellt: {current_path}")
                    except Exception as e:
                        print(f"   ❌ Fehler beim Erstellen von {current_path}: {e}")
                        ftp.quit()
                        return
            print(f"✅ Verzeichnis-Struktur erstellt\n")
        except Exception as e:
            print(f"❌ Fehler: {e}")
            ftp.quit()
            return
    
    # Lade Dateien hoch
    uploaded = 0
    for html_file, local_path in local_files:
        print(f"📤 Lade {html_file}...")
        if upload_file(ftp, local_path, html_file):
            set_permissions(ftp, html_file)
            uploaded += 1
        time.sleep(0.5)  # Kurze Pause zwischen Uploads
    
    # Setze Verzeichnis-Berechtigung
    try:
        ftp.cwd(DOCKER_WWW_PATH)
        ftp.sendcmd('SITE CHMOD 755 .')
        print(f"\n✅ Verzeichnis-Berechtigung gesetzt: 0755")
    except:
        pass
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print(f"✅ {uploaded}/{len(local_files)} DATEIEN HOCHGELADEN")
    print("=" * 70)
    print()
    print("💡 Nächste Schritte:")
    print("   1. Warte 5-10 Sekunden")
    print("   2. Teste: http://31.97.56.197:8080/")
    print("   3. Falls immer noch 403:")
    print("      - Prüfe Container-Logs: docker logs nginx-proxy-manager-5tiw-automation-cango-app-empire-web-1")
    print("      - Prüfe Dateien im Container: docker exec nginx-proxy-manager-5tiw-automation-cango-app-empire-web-1 ls -lah /usr/share/nginx/html/")

if __name__ == '__main__':
    main()
