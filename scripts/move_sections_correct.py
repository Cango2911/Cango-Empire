#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verschiebe BREAKING NEWS und DAILY BLOGS Container nach rechts oben
"""

import ftplib
from io import BytesIO
import re

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

TARGET_DIR = "/docker/nginx-proxy-manager-5tiw/www"

def find_and_extract_container(content, class_name, start_pos):
    """Finde und extrahiere einen Container"""
    # Finde den Start des divs mit der Klasse
    pattern = rf'<div[^>]*class="[^"]*{class_name}[^"]*"[^>]*>'
    match = re.search(pattern, content[start_pos:], re.IGNORECASE)
    if not match:
        return None, None
    
    div_start = start_pos + match.start()
    
    # Finde das schließende </div> für diesen Container
    # Zähle die div-Tiefe
    depth = 0
    i = div_start
    container_start = None
    
    while i < len(content):
        if content[i:i+4] == '<div':
            if container_start is None:
                container_start = i
            depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0 and container_start is not None:
                return container_start, i + 6
        i += 1
    
    return None, None

def main():
    print("=" * 70)
    print("🔧 VERSCHIEBE NEWS-SEKTIONEN")
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
        
        # Lade index.html
        print("📥 Lade index.html...")
        file_data = BytesIO()
        ftp.retrbinary('RETR index.html', file_data.write)
        content = file_data.getvalue().decode('utf-8', errors='ignore')
        print(f"   ✅ Datei geladen ({len(content)} Zeichen)\n")
        
        # Finde beide Container
        print("🔍 Suche Container...")
        
        # Finde hero__news
        news_pos = content.find('hero__news')
        if news_pos > 0:
            news_start, news_end = find_and_extract_container(content, 'hero__news', max(0, news_pos - 100))
            if news_start and news_end:
                news_container = content[news_start:news_end]
                print(f"   ✅ BREAKING NEWS Container gefunden ({len(news_container)} Zeichen)")
            else:
                print("   ❌ BREAKING NEWS Container nicht vollständig gefunden")
                news_container = None
        else:
            print("   ❌ BREAKING NEWS nicht gefunden")
            news_container = None
        
        # Finde hero__blogs
        blogs_pos = content.find('hero__blogs')
        if blogs_pos > 0:
            blogs_start, blogs_end = find_and_extract_container(content, 'hero__blogs', max(0, blogs_pos - 100))
            if blogs_start and blogs_end:
                blogs_container = content[blogs_start:blogs_end]
                print(f"   ✅ DAILY BLOGS Container gefunden ({len(blogs_container)} Zeichen)")
            else:
                print("   ❌ DAILY BLOGS Container nicht vollständig gefunden")
                blogs_container = None
        else:
            print("   ❌ DAILY BLOGS nicht gefunden")
            blogs_container = None
        
        if news_container and blogs_container:
            # Entferne Container aus aktueller Position
            content = content.replace(news_container, "", 1)
            content = content.replace(blogs_container, "", 1)
            
            # Finde Einfügeposition (nach </header> oder </nav>)
            insert_patterns = [
                r'(</header>)',
                r'(</nav>)',
                r'(<main[^>]*>)',
                r'(<section[^>]*class="[^"]*hero[^"]*"[^>]*>)'
            ]
            
            insert_pos = None
            for pattern in insert_patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    insert_pos = match.end()
                    print(f"   ✅ Einfügeposition gefunden: {pattern}")
                    break
            
            if insert_pos:
                # Füge Container rechts oben ein
                wrapper = f'''
<!-- BREAKING NEWS & DAILY BLOGS - Rechts oben positioniert -->
<div style="position: fixed; top: 80px; right: 20px; width: 380px; z-index: 1000; display: flex; flex-direction: column; gap: 16px; max-height: calc(100vh - 120px); overflow-y: auto;">
{news_container}
{blogs_container}
</div>
'''
                content = content[:insert_pos] + wrapper + content[insert_pos:]
                
                # Aktualisiere CSS für bessere Positionierung
                # Entferne sticky positioning
                content = re.sub(
                    r'(\.hero__news\s*\{[^}]*?)position:\s*sticky[^;]*;',
                    r'\1position: relative !important;',
                    content,
                    flags=re.DOTALL | re.IGNORECASE
                )
                
                content = re.sub(
                    r'(\.hero__blogs\s*\{[^}]*?)position:\s*sticky[^;]*;',
                    r'\1position: relative !important;',
                    content,
                    flags=re.DOTALL | re.IGNORECASE
                )
                
                print("   ✅ Container verschoben\n")
                
                # Speichere
                print("📤 Speichere aktualisierte Datei...")
                updated_data = BytesIO(content.encode('utf-8'))
                ftp.storbinary('STOR index.html', updated_data)
                ftp.sendcmd('SITE CHMOD 644 index.html')
                print("   ✅ index.html aktualisiert\n")
                
                # Aktualisiere auch cango-empire-v4-monopoly.html
                print("📤 Aktualisiere cango-empire-v4-monopoly.html...")
                updated_data.seek(0)
                ftp.storbinary('STOR cango-empire-v4-monopoly.html', updated_data)
                ftp.sendcmd('SITE CHMOD 644 cango-empire-v4-monopoly.html')
                print("   ✅ cango-empire-v4-monopoly.html aktualisiert\n")
            else:
                print("   ❌ Keine Einfügeposition gefunden")
        else:
            print("   ❌ Nicht alle Container gefunden")
    
    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()
    
    ftp.quit()
    
    print("=" * 70)
    print("✅ FERTIG")
    print("=" * 70)
    print()
    print("💡 Für Domain-Bindung siehe: DOMAIN_BINDUNG_ANLEITUNG.md")

if __name__ == '__main__':
    main()
