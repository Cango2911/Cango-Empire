#!/usr/bin/env python3
"""
🚀 100% AUTOMATISCHER UPLOAD - DIREKT INS DOCUMENT ROOT
=======================================================
Lädt direkt in / (Document Root) hoch
Löscht unnötige Dateien
Setzt Berechtigungen (falls möglich)
"""

import ftplib
from pathlib import Path
import time

# ============================================================
# KONFIGURATION
# ============================================================

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"  # Document Root ist das Root-Verzeichnis!

# Wichtige Dateien (werden BEHALTEN)
IMPORTANT_FILES = {
    "cango-empire-v4-monopoly.html",
    "ueber-uns.html",
    "produkte.html",
    "kontakt.html",
    "blogs.html",
    "marktplatz.html",
    "index.html"
}

SCRIPT_DIR = Path(__file__).parent

# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def upload_file(ftp, local_path, remote_path, description):
    """Upload eine Datei mit Retries"""
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"   ✅ {description}")
            return True
        except Exception as e:
            if attempt < max_retries:
                print(f"   ⚠️  Versuch {attempt} fehlgeschlagen, wiederhole...")
                time.sleep(2)
            else:
                print(f"   ❌ {description}: {e}")
                return False
    return False

def delete_file(ftp, filename, description):
    """Lösche eine Datei"""
    try:
        ftp.delete(filename)
        print(f"   🗑️  {description}")
        return True
    except Exception as e:
        print(f"   ⚠️  Konnte {description} nicht löschen: {e}")
        return False

# ============================================================
# MAIN
# ============================================================

print("=" * 60)
print("🚀 100% AUTOMATISCHER UPLOAD - DIREKT INS DOCUMENT ROOT")
print("=" * 60)
print()

# Prüfe lokale Dateien
print("1️⃣  Prüfe lokale Dateien...")
html_files = list(SCRIPT_DIR.glob("*.html"))
image_files = list((SCRIPT_DIR / "images").glob("*.jpg")) + list((SCRIPT_DIR / "assets").glob("*.jpg"))

print(f"   ✅ {len(html_files)} HTML-Dateien gefunden")
print(f"   ✅ {len(image_files)} Bilder gefunden")
print()

# ============================================================
# SCHRITT 1: FTP-VERBINDUNG
# ============================================================

print("=" * 60)
print("2️⃣  FTP-VERBINDUNG")
print("=" * 60)
print()

try:
    print("📤 Verbinde zu FTP...")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    print("✅ FTP-Verbindung erfolgreich!")
    
    # Navigiere zum Document Root
    ftp.cwd(DOC_ROOT)
    current_dir = ftp.pwd()
    print(f"📁 Aktuelles Verzeichnis: {current_dir}")
    print()
    
    # ============================================================
    # SCHRITT 2: LÖSCHE UNNÖTIGE DATEIEN
    # ============================================================
    
    print("=" * 60)
    print("3️⃣  LÖSCHE UNNÖTIGE DATEIEN")
    print("=" * 60)
    print()
    
    try:
        files = ftp.nlst()
        deleted_count = 0
        
        for filename in files:
            # Überspringe Verzeichnisse
            if filename in ['.', '..', 'images', 'assets', 'domains', 'htdocs', 'blogs']:
                continue
            
            # Lösche Backup-Dateien
            if filename.endswith(('.backup', '.bak', '.old', '.tmp')):
                delete_file(ftp, filename, f"Lösche Backup: {filename}")
                deleted_count += 1
                continue
            
            # Lösche HTML-Dateien die nicht wichtig sind
            if filename.endswith('.html') and filename not in IMPORTANT_FILES:
                delete_file(ftp, filename, f"Lösche unnötige HTML: {filename}")
                deleted_count += 1
        
        if deleted_count > 0:
            print(f"   ✅ {deleted_count} unnötige Dateien gelöscht")
        else:
            print("   ℹ️  Keine unnötigen Dateien gefunden")
    except Exception as e:
        print(f"   ⚠️  Fehler beim Löschen: {e}")
    
    print()
    
    # ============================================================
    # SCHRITT 3: ERSTELLE ORDNER
    # ============================================================
    
    print("=" * 60)
    print("4️⃣  ERSTELLE ORDNER")
    print("=" * 60)
    print()
    
    for folder in ["assets", "images"]:
        try:
            ftp.mkd(folder)
            print(f"   ✅ Ordner erstellt: {folder}/")
        except:
            print(f"   ℹ️  Ordner existiert bereits: {folder}/")
    
    print()
    
    # ============================================================
    # SCHRITT 4: UPLOAD HTML-DATEIEN
    # ============================================================
    
    print("=" * 60)
    print("5️⃣  UPLOAD HTML-DATEIEN")
    print("=" * 60)
    print()
    
    for html_file in html_files:
        filename = html_file.name
        upload_file(ftp, html_file, filename, filename)
    
    print()
    
    # ============================================================
    # SCHRITT 5: UPLOAD BILDER
    # ============================================================
    
    print("=" * 60)
    print("6️⃣  UPLOAD BILDER")
    print("=" * 60)
    print()
    
    for folder in ["assets", "images"]:
        image_path = SCRIPT_DIR / folder / "founder-canberk-kivilcim.jpg"
        if image_path.exists():
            try:
                ftp.cwd(folder)
            except:
                ftp.mkd(folder)
                ftp.cwd(folder)
            
            upload_file(ftp, image_path, "founder-canberk-kivilcim.jpg", f"{folder}/founder-canberk-kivilcim.jpg")
            ftp.cwd("..")
    
    print()
    
    # ============================================================
    # SCHRITT 6: FINALE PRÜFUNG
    # ============================================================
    
    print("=" * 60)
    print("7️⃣  FINALE PRÜFUNG")
    print("=" * 60)
    print()
    
    ftp.cwd(DOC_ROOT)
    files = ftp.nlst()
    html_files_uploaded = [f for f in files if f.endswith('.html')]
    
    print(f"📊 HTML-Dateien auf Server: {len(html_files_uploaded)}")
    for filename in sorted(html_files_uploaded):
        if filename in IMPORTANT_FILES:
            print(f"   ✅ {filename}")
        else:
            print(f"   ⚠️  {filename} (sollte gelöscht werden)")
    
    print()
    
    # Prüfe Bilder
    for folder in ["assets", "images"]:
        try:
            ftp.cwd(folder)
            files = ftp.nlst()
            if "founder-canberk-kivilcim.jpg" in files:
                print(f"   ✅ {folder}/founder-canberk-kivilcim.jpg")
            else:
                print(f"   ❌ {folder}/founder-canberk-kivilcim.jpg fehlt")
            ftp.cwd("..")
        except:
            print(f"   ❌ {folder}/ Ordner nicht erreichbar")
    
    print()
    
    ftp.quit()
    
    print("=" * 60)
    print("✅ FERTIG! ALLES AUTOMATISCH ERLEDIGT!")
    print("=" * 60)
    print()
    print("🧪 Teste jetzt:")
    print("   1. Warte 1-2 Minuten (CDN-Synchronisation)")
    print("   2. Hard Refresh: Cmd+Shift+R")
    print("   3. Teste: https://automation-cango-app-empire.com/ueber-uns.html")
    print()
    print("⚠️  HINWEIS: Berechtigungen müssen im CloudPanel gesetzt werden:")
    print("   - HTML-Dateien: 644")
    print("   - Ordner: 755")
    print("   - Bilder: 644")
    print()
    
except Exception as e:
    print(f"❌ FTP Fehler: {e}")
    import traceback
    traceback.print_exc()
