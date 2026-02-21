#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Synchronisiere wichtige Elemente von:
- Cango Universal
- OnlineAgentur CanGo
zu Cango-Empire und allen Speicherorten
"""

import os
import shutil
import subprocess
from pathlib import Path
import ftplib
from io import BytesIO

# Verzeichnisse
REPO_PATH = Path("/Users/canberkkivilcim/PycharmProjects/Cango-Empire")
CANGO_UNIVERSAL = Path("/Users/canberkkivilcim/Cango Universal")
ONLINE_AGENTUR = Path("/Users/canberkkivilcim/OnlineAgentur CanGo")

# FTP-Konfiguration
FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"
DOCKER_WWW_PATH = "/docker/nginx-proxy-manager-5tiw/www"

def sync_to_hostinger_docker(file_path):
    """Synchronisiere zu Hostinger Docker"""
    if file_path.suffix != '.html':
        return True
    
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(DOCKER_WWW_PATH)
        
        with open(file_path, 'rb') as f:
            ftp.storbinary(f'STOR {file_path.name}', f)
        ftp.sendcmd(f'SITE CHMOD 644 {file_path.name}')
        ftp.quit()
        return True
    except Exception as e:
        print(f"   ⚠️  Hostinger: {e}")
        return False

def sync_to_github(file_path, relative_path):
    """Synchronisiere zu GitHub"""
    try:
        os.chdir(REPO_PATH)
        subprocess.run(['git', 'add', str(relative_path)], check=True, capture_output=True)
        
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout.strip():
            subprocess.run(
                ['git', 'commit', '-m', f'Sync: {file_path.name}'],
                check=True,
                capture_output=True
            )
            subprocess.run(['git', 'push', 'origin', 'main'], check=True, capture_output=True)
        return True
    except Exception as e:
        print(f"   ⚠️  GitHub: {e}")
        return False

def copy_important_files():
    """Kopiere wichtige Dateien"""
    copied = []
    
    # 1. HTML-Dateien aus Cango Universal
    print("📋 Kopiere HTML-Dateien aus Cango Universal...")
    html_files = [
        "index.html",
        "cango-empire-v4-monopoly.html",
        "produkte.html",
        "ueber-uns.html",
        "kontakt.html",
        "blogs.html",
        "marktplatz.html"
    ]
    
    for html_file in html_files:
        source = CANGO_UNIVERSAL / html_file
        if source.exists():
            dest = REPO_PATH / "website" / html_file
            dest.parent.mkdir(exist_ok=True)
            shutil.copy2(source, dest)
            copied.append(("website", html_file))
            print(f"   ✅ {html_file}")
    
    # 2. Wichtige Python Scripts
    print("\n📋 Kopiere wichtige Python Scripts...")
    important_scripts = [
        "upload_to_docker_www.py",
        "move_sections_correct.py",
        "fix_index_html.py",
        "check_and_upload_docker_www.py",
        "compare_html_files.py",
        "check_fonts.py",
        "fix_layout_sections_vertical.py",
        "sync_all_locations.py"
    ]
    
    for script in important_scripts:
        # Prüfe beide Verzeichnisse
        for source_dir in [CANGO_UNIVERSAL, ONLINE_AGENTUR]:
            source = source_dir / script
            if source.exists():
                dest = REPO_PATH / "scripts" / script
                dest.parent.mkdir(exist_ok=True)
                shutil.copy2(source, dest)
                copied.append(("scripts", script))
                print(f"   ✅ {script}")
                break
    
    # 3. Dokumentationen
    print("\n📋 Kopiere Dokumentationen...")
    docs = [
        "DOMAIN_BINDUNG_ANLEITUNG.md",
        "SYNC_SYSTEM.md",
        "README.md"
    ]
    
    for doc in docs:
        for source_dir in [CANGO_UNIVERSAL, ONLINE_AGENTUR, REPO_PATH]:
            source = source_dir / doc
            if source.exists() and source != REPO_PATH / doc:
                dest = REPO_PATH / "docs" / doc
                dest.parent.mkdir(exist_ok=True)
                shutil.copy2(source, dest)
                copied.append(("docs", doc))
                print(f"   ✅ {doc}")
                break
    
    # 4. Docker-Konfiguration
    print("\n📋 Kopiere Docker-Konfiguration...")
    docker_files = ["docker-compose.yml", "daemon.json"]
    
    for docker_file in docker_files:
        for source_dir in [CANGO_UNIVERSAL, ONLINE_AGENTUR]:
            source = source_dir / docker_file
            if source.exists():
                dest = REPO_PATH / "docker" / docker_file
                dest.parent.mkdir(exist_ok=True)
                shutil.copy2(source, dest)
                copied.append(("docker", docker_file))
                print(f"   ✅ {docker_file}")
                break
    
    return copied

def sync_all_locations(copied_files):
    """Synchronisiere alle kopierten Dateien zu allen Orten"""
    print("\n🔄 Synchronisiere zu allen Speicherorten...")
    
    for category, filename in copied_files:
        file_path = REPO_PATH / category / filename
        relative_path = Path(category) / filename
        
        if not file_path.exists():
            continue
        
        print(f"\n📤 {filename}:")
        
        # Hostinger Docker (nur HTML)
        if filename.endswith('.html'):
            sync_to_hostinger_docker(file_path)
        
        # GitHub
        sync_to_github(file_path, relative_path)

def main():
    print("=" * 70)
    print("🔄 SYNCHRONISIERE WICHTIGE ELEMENTE")
    print("=" * 70)
    print()
    print("Quellen:")
    print(f"  - Cango Universal: {CANGO_UNIVERSAL}")
    print(f"  - OnlineAgentur CanGo: {ONLINE_AGENTUR}")
    print(f"  - Ziel: {REPO_PATH}")
    print()
    
    # Kopiere Dateien
    copied_files = copy_important_files()
    
    if not copied_files:
        print("\n⚠️  Keine Dateien zum Kopieren gefunden")
        return
    
    print(f"\n✅ {len(copied_files)} Dateien kopiert")
    
    # Synchronisiere zu allen Orten
    sync_all_locations(copied_files)
    
    print("\n" + "=" * 70)
    print("✅ SYNCHRONISATION ABGESCHLOSSEN")
    print("=" * 70)
    print()
    print("💡 Alle Dateien wurden synchronisiert zu:")
    print("   ✅ PyCharm Repository")
    print("   ✅ GitHub (Cango2911)")
    print("   ✅ Hostinger Docker (HTML-Dateien)")

if __name__ == '__main__':
    main()
