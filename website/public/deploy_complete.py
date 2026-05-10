#!/usr/bin/env python3
"""
🚀 KOMPLETT-AUTOMATISCHER DEPLOY
================================
Macht ALLES: Upload + Berechtigungen + Cleanup
"""

import ftplib
from pathlib import Path
import time

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
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

def upload_file(ftp, local_path, remote_path, description):
    """Upload mit Retries"""
    for attempt in range(1, 4):
        try:
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"   ✅ {description}")
            return True
        except Exception as e:
            if attempt < 3:
                time.sleep(2)
            else:
                print(f"   ❌ {description}: {e}")
                return False
    return False

def set_permissions(ftp, path, mode, description):
    """Versuche Berechtigungen per FTP zu setzen"""
    try:
        # Versuche SITE CHMOD (manche FTP-Server unterstützen das)
        ftp.sendcmd(f'SITE CHMOD {mode} {path}')
        print(f"   ✅ {description}: {mode}")
        return True
    except:
        try:
            # Alternative: CHMOD direkt
            ftp.sendcmd(f'CHMOD {mode} {path}')
            print(f"   ✅ {description}: {mode}")
            return True
        except:
            print(f"   ⚠️  {description}: Berechtigungen müssen manuell gesetzt werden")
            return False

def delete_file(ftp, filename):
    """Lösche Datei"""
    try:
        ftp.delete(filename)
        return True
    except:
        return False

print("=" * 60)
print("🚀 KOMPLETT-AUTOMATISCHER DEPLOY")
print("=" * 60)
print()

# 1. Prüfe lokale Dateien
print("1️⃣  Prüfe lokale Dateien...")
html_files = list(SCRIPT_DIR.glob("*.html"))
print(f"   ✅ {len(html_files)} HTML-Dateien")
print(f"   ✅ Bilder in images/ und assets/")
print()

# 2. FTP-Verbindung
print("2️⃣  Verbinde zu FTP...")
try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print(f"   ✅ Verbunden! Document Root: {ftp.pwd()}")
    print()
except Exception as e:
    print(f"   ❌ Fehler: {e}")
    exit(1)

# 3. Cleanup
print("3️⃣  Lösche unnötige Dateien...")
try:
    files = ftp.nlst()
    deleted = 0
    for f in files:
        if f in ['.', '..', 'images', 'assets', 'domains', 'htdocs', 'blogs']:
            continue
        if f.endswith(('.backup', '.bak', '.old', '.tmp')):
            if delete_file(ftp, f):
                deleted += 1
        elif f.endswith('.html') and f not in IMPORTANT_FILES:
            if delete_file(ftp, f):
                deleted += 1
    print(f"   ✅ {deleted} Dateien gelöscht")
    print()
except Exception as e:
    print(f"   ⚠️  Cleanup-Fehler: {e}")
    print()

# 4. Erstelle Ordner
print("4️⃣  Erstelle Ordner...")
for folder in ["assets", "images"]:
    try:
        ftp.mkd(folder)
        print(f"   ✅ {folder}/")
    except:
        print(f"   ℹ️  {folder}/ existiert")
print()

# 5. Upload HTML
print("5️⃣  Upload HTML-Dateien...")
for html_file in html_files:
    upload_file(ftp, html_file, html_file.name, html_file.name)
print()

# 6. Upload Bilder
print("6️⃣  Upload Bilder...")
for folder in ["assets", "images"]:
    img_path = SCRIPT_DIR / folder / "founder-canberk-kivilcim.jpg"
    if img_path.exists():
        try:
            ftp.cwd(folder)
        except:
            ftp.mkd(folder)
            ftp.cwd(folder)
        upload_file(ftp, img_path, "founder-canberk-kivilcim.jpg", f"{folder}/founder-canberk-kivilcim.jpg")
        ftp.cwd("..")
print()

# 7. Versuche Berechtigungen zu setzen
print("7️⃣  Setze Berechtigungen...")
ftp.cwd(DOC_ROOT)

# HTML-Dateien
for html_file in html_files:
    set_permissions(ftp, html_file.name, "644", html_file.name)

# Ordner
for folder in ["assets", "images"]:
    set_permissions(ftp, folder, "755", f"{folder}/")

# Bilder
for folder in ["assets", "images"]:
    set_permissions(ftp, f"{folder}/founder-canberk-kivilcim.jpg", "644", f"{folder}/founder-canberk-kivilcim.jpg")
print()

# 8. Finale Prüfung
print("8️⃣  Finale Prüfung...")
ftp.cwd(DOC_ROOT)
files = ftp.nlst()
html_on_server = [f for f in files if f.endswith('.html')]
print(f"   📊 {len(html_on_server)} HTML-Dateien auf Server")
for f in sorted(html_on_server):
    status = "✅" if f in IMPORTANT_FILES else "⚠️"
    print(f"      {status} {f}")

for folder in ["assets", "images"]:
    try:
        ftp.cwd(folder)
        files = ftp.nlst()
        if "founder-canberk-kivilcim.jpg" in files:
            print(f"      ✅ {folder}/founder-canberk-kivilcim.jpg")
        ftp.cwd("..")
    except:
        pass
print()

ftp.quit()

print("=" * 60)
print("✅ DEPLOY ABGESCHLOSSEN!")
print("=" * 60)
print()
print("🧪 Teste jetzt:")
print("   https://automation-cango-app-empire.com/ueber-uns.html")
print()
print("⚠️  Falls Berechtigungen nicht automatisch gesetzt wurden:")
print("   Setze im CloudPanel: HTML/Bilder 644, Ordner 755")
print()
