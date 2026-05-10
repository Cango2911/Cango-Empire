#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lade alle HTML-Dateien aus website/ zu Hostinger Docker hoch
"""

import ftplib
from pathlib import Path

from cango_env import ftp_credentials

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()
DOCKER_WWW_PATH = "/docker/nginx-proxy-manager-5tiw/www"

REPO_PATH = Path("/Users/canberkkivilcim/PycharmProjects/Cango-Empire")
WEBSITE_DIR = REPO_PATH / "website"

def main():
    print("=" * 70)
    print("📤 LADE HTML-DATEIEN ZU HOSTINGER DOCKER")
    print("=" * 70)
    print()
    
    # Finde alle HTML-Dateien
    html_files = list(WEBSITE_DIR.glob("*.html"))
    
    if not html_files:
        print("❌ Keine HTML-Dateien in website/ gefunden")
        return
    
    print(f"📋 Gefunden: {len(html_files)} HTML-Dateien\n")
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        print("✅ FTP-Verbindung hergestellt\n")
    except Exception as e:
        print(f"❌ FTP-Fehler: {e}")
        return
    
    try:
        ftp.cwd(DOCKER_WWW_PATH)
        print(f"✅ Im Verzeichnis: {DOCKER_WWW_PATH}\n")
    except:
        print(f"⚠️  Verzeichnis existiert nicht, erstelle es...")
        try:
            parts = DOCKER_WWW_PATH.strip('/').split('/')
            current_path = '/'
            for part in parts:
                current_path = f"{current_path}{part}/"
                try:
                    ftp.cwd(current_path)
                except:
                    ftp.mkd(current_path)
                    ftp.cwd(current_path)
            print(f"✅ Verzeichnis erstellt\n")
        except Exception as e:
            print(f"❌ Fehler: {e}")
            ftp.quit()
            return
    
    # Lade Dateien hoch
    uploaded = 0
    for html_file in html_files:
        try:
            print(f"📤 Lade {html_file.name}...")
            with open(html_file, 'rb') as f:
                ftp.storbinary(f'STOR {html_file.name}', f)
            ftp.sendcmd(f'SITE CHMOD 644 {html_file.name}')
            print(f"   ✅ {html_file.name} hochgeladen")
            uploaded += 1
        except Exception as e:
            print(f"   ❌ Fehler: {e}")
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print(f"✅ {uploaded}/{len(html_files)} DATEIEN HOCHGELADEN")
    print("=" * 70)

if __name__ == '__main__':
    main()
