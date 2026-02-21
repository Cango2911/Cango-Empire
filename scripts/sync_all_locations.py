#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatische Synchronisation zu allen Speicherorten:
1. Hostinger Docker (Server)
2. Docker Desktop (lokal)
3. GitHub (Cango2911)
4. PyCharm (lokal)
"""

import os
import subprocess
import ftplib
from io import BytesIO
from pathlib import Path
import sys

# Konfiguration
REPO_PATH = "/Users/canberkkivilcim/PycharmProjects/Cango-Empire"
FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"
DOCKER_WWW_PATH = "/docker/nginx-proxy-manager-5tiw/www"
GITHUB_REPO = "https://github.com/Cango2911/Cango-Empire.git"

def sync_to_hostinger_docker(file_path, relative_path):
    """Synchronisiere Datei zu Hostinger Docker"""
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        
        # Für HTML-Dateien: direkt ins Docker-Verzeichnis
        if file_path.suffix == '.html':
            ftp.cwd(DOCKER_WWW_PATH)
            with open(file_path, 'rb') as f:
                ftp.storbinary(f'STOR {file_path.name}', f)
            ftp.sendcmd(f'SITE CHMOD 644 {file_path.name}')
            print(f"   ✅ Hostinger Docker: {file_path.name}")
        else:
            # Andere Dateien ins Root-Verzeichnis
            ftp.cwd("/")
            with open(file_path, 'rb') as f:
                ftp.storbinary(f'STOR {file_path.name}', f)
            print(f"   ✅ Hostinger Root: {file_path.name}")
        
        ftp.quit()
        return True
    except Exception as e:
        print(f"   ❌ Hostinger Fehler: {e}")
        return False

def sync_to_github(file_path, relative_path):
    """Synchronisiere Datei zu GitHub"""
    try:
        # Wechsle ins Repository
        os.chdir(REPO_PATH)
        
        # Prüfe ob Datei im Repository ist
        repo_file = Path(REPO_PATH) / relative_path
        if not repo_file.exists():
            print(f"   ⚠️  GitHub: Datei nicht im Repository, überspringe")
            return True
        
        # Git add
        result = subprocess.run(['git', 'add', str(relative_path)], capture_output=True)
        
        # Prüfe ob es Änderungen gibt
        status_result = subprocess.run(['git', 'status', '--porcelain', str(relative_path)], 
                                      capture_output=True, text=True)
        
        if status_result.stdout.strip():
            # Es gibt Änderungen, committe und pushe
            commit_result = subprocess.run(
                ['git', 'commit', '-m', f'Auto-sync: Update {file_path.name}'],
                capture_output=True
            )
            
            if commit_result.returncode == 0:
                push_result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True)
                if push_result.returncode == 0:
                    print(f"   ✅ GitHub: {file_path.name} gepusht")
                else:
                    print(f"   ⚠️  GitHub: Push fehlgeschlagen (möglicherweise bereits gepusht)")
            else:
                print(f"   ⚠️  GitHub: Commit fehlgeschlagen (keine Änderungen)")
        else:
            print(f"   ✅ GitHub: {file_path.name} bereits aktuell")
        
        return True
    except Exception as e:
        print(f"   ❌ GitHub Fehler: {e}")
        return False

def sync_to_pycharm(file_path, relative_path):
    """Synchronisiere Datei zu PyCharm (Repository)"""
    try:
        repo_file = Path(REPO_PATH) / relative_path
        
        # Prüfe ob Datei bereits im Repository ist (gleicher Pfad)
        if file_path.resolve() == repo_file.resolve():
            print(f"   ✅ PyCharm: Bereits im Repository")
            return True
        
        # Erstelle Verzeichnis falls nötig
        repo_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Kopiere Datei nur wenn sie sich unterscheidet
        import shutil
        if not repo_file.exists() or file_path.stat().st_mtime > repo_file.stat().st_mtime:
            shutil.copy2(file_path, repo_file)
            print(f"   ✅ PyCharm: {relative_path} aktualisiert")
        else:
            print(f"   ✅ PyCharm: {relative_path} bereits aktuell")
        
        return True
    except Exception as e:
        print(f"   ❌ PyCharm Fehler: {e}")
        return False

def sync_file(file_path):
    """Synchronisiere eine Datei zu allen Orten"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"❌ Datei nicht gefunden: {file_path}")
        return False
    
    # Berechne relativen Pfad zum Repository
    try:
        relative_path = file_path.relative_to(REPO_PATH)
    except ValueError:
        # Datei ist außerhalb des Repositories
        relative_path = file_path.name
    
    print(f"\n📤 Synchronisiere: {file_path.name}")
    
    results = {
        'hostinger': sync_to_hostinger_docker(file_path, relative_path),
        'pycharm': sync_to_pycharm(file_path, relative_path),
        'github': sync_to_github(file_path, relative_path)
    }
    
    return all(results.values())

def sync_all_html_files():
    """Synchronisiere alle HTML-Dateien"""
    website_dir = Path(REPO_PATH) / "website"
    
    if not website_dir.exists():
        print("❌ website/ Verzeichnis nicht gefunden")
        return
    
    html_files = list(website_dir.glob("*.html"))
    
    if not html_files:
        print("⚠️  Keine HTML-Dateien gefunden")
        return
    
    print(f"📋 Synchronisiere {len(html_files)} HTML-Dateien...")
    
    for html_file in html_files:
        sync_file(html_file)

def main():
    """Hauptfunktion"""
    if len(sys.argv) > 1:
        # Einzelne Datei synchronisieren
        file_path = Path(sys.argv[1])
        sync_file(file_path)
    else:
        # Alle HTML-Dateien synchronisieren
        sync_all_html_files()
    
    print("\n" + "=" * 70)
    print("✅ SYNCHRONISATION ABGESCHLOSSEN")
    print("=" * 70)

if __name__ == '__main__':
    main()
