#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfe Font-Einbindungen in index.html
"""

import ftplib
from io import BytesIO
import re

from cango_env import ftp_credentials

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()

TARGET_DIR = "/docker/nginx-proxy-manager-5tiw/www"

def check_fonts_in_html(html_content):
    """Prüfe ob Fonts korrekt eingebunden sind"""
    issues = []
    
    # Prüfe Google Fonts
    if 'fonts.googleapis.com' not in html_content:
        issues.append("❌ Google Fonts nicht gefunden")
    else:
        print("   ✅ Google Fonts gefunden")
    
    # Prüfe font-family Definitionen
    font_families = re.findall(r'font-family:\s*([^;]+)', html_content, re.IGNORECASE)
    if not font_families:
        issues.append("❌ Keine font-family Definitionen gefunden")
    else:
        print(f"   ✅ {len(font_families)} font-family Definitionen gefunden")
        # Zeige erste paar
        for ff in font_families[:3]:
            print(f"      - {ff.strip()}")
    
    # Prüfe @font-face
    if '@font-face' not in html_content:
        print("   ⚠️  Keine @font-face Definitionen")
    else:
        print("   ✅ @font-face Definitionen gefunden")
    
    # Prüfe preconnect für Fonts
    if 'fonts.googleapis.com' in html_content:
        if 'preconnect' not in html_content.lower():
            issues.append("⚠️  Keine preconnect für Google Fonts")
        else:
            print("   ✅ preconnect für Google Fonts gefunden")
    
    return issues

def main():
    print("=" * 70)
    print("🔍 PRÜFE FONT-EINBINDUNGEN")
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
    
    # Lade index.html
    print("📥 Lade index.html...")
    try:
        ftp.cwd(TARGET_DIR)
        file_data = BytesIO()
        ftp.retrbinary('RETR index.html', file_data.write)
        html_content = file_data.getvalue().decode('utf-8', errors='ignore')
        
        print(f"   ✅ Datei geladen ({len(html_content)} Zeichen)\n")
        
        # Prüfe Fonts
        print("🔍 Prüfe Font-Einbindungen...")
        issues = check_fonts_in_html(html_content)
        
        if issues:
            print("\n⚠️  Gefundene Probleme:")
            for issue in issues:
                print(f"   {issue}")
        else:
            print("\n✅ Alle Font-Checks bestanden")
        
        # Zeige Font-Links
        print("\n📋 Font-Links in der Datei:")
        font_links = re.findall(r'<link[^>]*fonts[^>]*>', html_content, re.IGNORECASE)
        for link in font_links[:5]:
            print(f"   {link[:100]}...")
        
    except Exception as e:
        print(f"❌ Fehler: {e}")
    
    ftp.quit()
    
    print("\n" + "=" * 70)
    print("✅ PRÜFUNG ABGESCHLOSSEN")
    print("=" * 70)

if __name__ == '__main__':
    main()
