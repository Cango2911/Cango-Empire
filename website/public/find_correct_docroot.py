#!/usr/bin/env python3
"""
🔍 Finde den korrekten Document Root
====================================
"""

import ftplib

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

print("=" * 60)
print("🔍 Finde korrekten Document Root")
print("=" * 60)
print()

try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    
    # Start-Verzeichnis
    start_dir = ftp.pwd()
    print(f"📁 Start-Verzeichnis: {start_dir}")
    print()
    
    # Teste verschiedene Verzeichnisse
    test_paths = [
        ("/", "Root-Verzeichnis"),
        ("public_html", "public_html (relativ)"),
        ("htdocs/automation-cango-app-empire.com", "htdocs/... (relativ)"),
    ]
    
    for path, description in test_paths:
        try:
            ftp.cwd(path)
            current = ftp.pwd()
            files = ftp.nlst()
            html_files = [f for f in files if f.endswith('.html')]
            
            print(f"📂 {description}: {current}")
            print(f"   HTML-Dateien: {len(html_files)}")
            if html_files:
                print(f"   Beispiele: {', '.join(html_files[:5])}")
            
            # Prüfe ob ueber-uns.html und produkte.html vorhanden sind
            has_ueber_uns = 'ueber-uns.html' in files
            has_produkte = 'produkte.html' in files
            
            if has_ueber_uns and has_produkte:
                print(f"   ✅ Enthält ueber-uns.html und produkte.html")
                print(f"   🎯 DIESER PFAD IST DER DOCUMENT ROOT!")
                print()
                break
            else:
                print(f"   ⚠️  Fehlt: ueber-uns.html={has_ueber_uns}, produkte.html={has_produkte}")
            print()
        except Exception as e:
            print(f"   ❌ Fehler: {e}")
            print()
    
    # Gehe zurück zum Start
    ftp.cwd(start_dir)
    
    # Prüfe ob htdocs/automation-cango-app-empire.com existiert
    print("🔍 Prüfe htdocs/automation-cango-app-empire.com...")
    try:
        ftp.cwd("htdocs/automation-cango-app-empire.com")
        current = ftp.pwd()
        files = ftp.nlst()
        html_files = [f for f in files if f.endswith('.html')]
        print(f"   📁 Pfad: {current}")
        print(f"   HTML-Dateien: {len(html_files)}")
        if html_files:
            print(f"   Beispiele: {', '.join(html_files[:5])}")
        
        has_ueber_uns = 'ueber-uns.html' in files
        has_produkte = 'produkte.html' in files
        if has_ueber_uns and has_produkte:
            print(f"   ✅ DIESER PFAD IST DER DOCUMENT ROOT!")
        else:
            print(f"   ⚠️  Dateien fehlen hier")
    except Exception as e:
        print(f"   ❌ Pfad nicht erreichbar: {e}")
    
    ftp.quit()
    
except Exception as e:
    print(f"❌ FTP Fehler: {e}")
