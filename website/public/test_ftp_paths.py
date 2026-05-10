#!/usr/bin/env python3
"""
🔍 Teste verschiedene FTP-Pfade
================================
Findet den korrekten Pfad zum Document Root
"""

import ftplib
from pathlib import Path

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

# Mögliche Pfade zum Document Root
POSSIBLE_PATHS = [
    "/home/automation-cango-app-empire/htdocs/automation-cango-app-empire.com",
    "htdocs/automation-cango-app-empire.com",
    "automation-cango-app-empire.com",
    "htdocs",
    "public_html",
    "/",
]

print("=" * 60)
print("🔍 Teste FTP-Pfade zum Document Root")
print("=" * 60)
print()

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    print("✅ FTP-Verbindung erfolgreich!")
    print(f"📁 Start-Verzeichnis: {ftp.pwd()}")
    print()
    
    # Zeige verfügbare Verzeichnisse
    print("📋 Verfügbare Verzeichnisse im Root:")
    try:
        ftp.retrlines('LIST', max(0, lambda x: print(f"   {x}") or 0))
    except:
        lines = []
        ftp.retrlines('LIST', lines.append)
        for line in lines[:10]:
            print(f"   {line}")
    print()
    
    # Teste verschiedene Pfade
    print("🔍 Teste verschiedene Pfade...")
    print()
    
    found_path = None
    
    for path in POSSIBLE_PATHS:
        try:
            ftp.cwd(path)
            current = ftp.pwd()
            print(f"✅ Pfad funktioniert: {path}")
            print(f"   → Aktuelles Verzeichnis: {current}")
            
            # Prüfe ob HTML-Dateien vorhanden sind (indiziert Document Root)
            try:
                files = ftp.nlst()
                html_files = [f for f in files if f.endswith('.html')]
                if html_files:
                    print(f"   ✅ HTML-Dateien gefunden: {len(html_files)}")
                    print(f"      Beispiele: {', '.join(html_files[:3])}")
                    found_path = current
                    break
            except:
                pass
            
            print()
        except Exception as e:
            print(f"❌ Pfad nicht erreichbar: {path}")
            print()
    
    if found_path:
        print("=" * 60)
        print(f"✅ KORREKTER PFAD GEFUNDEN: {found_path}")
        print("=" * 60)
    else:
        print("=" * 60)
        print("⚠️  Kein direkter Pfad gefunden")
        print("=" * 60)
        print()
        print("💡 Alternative: Nutze public_html und kopiere dann")
    
    ftp.quit()
    
except Exception as e:
    print(f"❌ FTP Fehler: {e}")
