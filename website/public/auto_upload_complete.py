#!/usr/bin/env python3
"""
🚀 AUTOMATISCHER KOMPLETT-UPLOAD
================================
Macht ALLES automatisch:
1. Upload per FTP
2. Kopiere zum Document Root (falls möglich)
3. Setze Berechtigungen (falls möglich)
4. Lösche unnötige Dateien
"""

import ftplib
import os
from pathlib import Path
import subprocess
import sys
import time

# ============================================================
# KONFIGURATION
# ============================================================

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

SERVER = "31.97.56.197"
SSH_USER = "root"
DOC_ROOT = "/home/automation-cango-app-empire/htdocs/automation-cango-app-empire.com"
FTP_PATH = "/domains/automation-cango-app-empire.com/public_html"
OWNER = "automation-cango-app-empire:automation-cango-app-empire"

# Wichtige Dateien (werden BEHALTEN)
IMPORTANT_FILES = [
    "cango-empire-v4-monopoly.html",
    "ueber-uns.html",
    "produkte.html",
    "kontakt.html",
    "blogs.html",
    "marktplatz.html",
    "index.html"
]

SCRIPT_DIR = Path(__file__).parent

# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def run_ssh_command(cmd, description=""):
    """Führe SSH-Befehl aus"""
    full_cmd = f'ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no {SSH_USER}@{SERVER} "{cmd}"'
    try:
        result = subprocess.run(
            full_cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode == 0:
            if description:
                print(f"   ✅ {description}")
            return True, result.stdout.strip()
        else:
            if description:
                print(f"   ⚠️  {description}: {result.stderr.strip()}")
            return False, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def upload_file_ftp(ftp, local_path, remote_path, description):
    """Upload eine Datei per FTP mit Retries"""
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            print(f"   ✅ {description}")
            return True
        except Exception as e:
            if attempt < max_retries:
                print(f"   ⚠️  Versuch {attempt} fehlgeschlagen, wiederhole in 2 Sekunden...")
                time.sleep(2)
            else:
                print(f"   ❌ {description}: {e}")
                return False
    return False

# ============================================================
# MAIN
# ============================================================

print("=" * 60)
print("🚀 AUTOMATISCHER KOMPLETT-UPLOAD")
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
# SCHRITT 1: FTP-UPLOAD
# ============================================================

print("=" * 60)
print("2️⃣  FTP-UPLOAD")
print("=" * 60)
print()

try:
    print("📤 Verbinde zu FTP...")
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    print("✅ FTP-Verbindung erfolgreich!")
    
    # Navigiere zum Verzeichnis
    try:
        ftp.cwd("public_html")
    except:
        ftp.mkd("public_html")
        ftp.cwd("public_html")
    
    # Erstelle Ordner
    for folder in ["assets", "images"]:
        try:
            ftp.mkd(folder)
        except:
            pass
    
    print()
    print("📤 Lade HTML-Dateien hoch...")
    for html_file in html_files:
        filename = html_file.name
        upload_file_ftp(ftp, html_file, filename, filename)
    
    print()
    print("📤 Lade Bilder hoch...")
    for folder in ["assets", "images"]:
        image_path = SCRIPT_DIR / folder / "founder-canberk-kivilcim.jpg"
        if image_path.exists():
            try:
                ftp.cwd(folder)
            except:
                ftp.mkd(folder)
                ftp.cwd(folder)
            upload_file_ftp(ftp, image_path, "founder-canberk-kivilcim.jpg", f"{folder}/founder-canberk-kivilcim.jpg")
            ftp.cwd("..")
    
    ftp.quit()
    print()
    print("✅ FTP-UPLOAD ERFOLGREICH!")
    
except Exception as e:
    print(f"❌ FTP Fehler: {e}")
    print()
    print("⚠️  FTP-Upload fehlgeschlagen. Dateien müssen manuell hochgeladen werden.")
    sys.exit(1)

# ============================================================
# SCHRITT 2: SSH-OPERATIONEN (Kopieren + Berechtigungen + Aufräumen)
# ============================================================

print()
print("=" * 60)
print("3️⃣  SSH-OPERATIONEN (Kopieren + Berechtigungen + Aufräumen)")
print("=" * 60)
print()

# Teste SSH
success, output = run_ssh_command("echo 'SSH Test'", "SSH-Verbindung testen")
if not success:
    print("⚠️  SSH funktioniert nicht!")
    print()
    print("💡 MANUELLE SCHRITTE IM CLOUDPANEL:")
    print("   1. Kopiere Dateien von /domains/.../public_html/ nach")
    print(f"      {DOC_ROOT}")
    print("   2. Setze Berechtigungen: HTML/Bilder 644, Ordner 755")
    print("   3. Lösche unnötige Dateien manuell")
    sys.exit(0)

print()

# Kopiere Dateien
print("📋 Kopiere Dateien zum Document Root...")
run_ssh_command(f"mkdir -p {DOC_ROOT}/images {DOC_ROOT}/assets", "Ordner erstellen")

for html_file in html_files:
    filename = html_file.name
    run_ssh_command(
        f"cp {FTP_PATH}/{filename} {DOC_ROOT}/{filename}",
        f"{filename} kopieren"
    )

run_ssh_command(
    f"cp {FTP_PATH}/images/founder-canberk-kivilcim.jpg {DOC_ROOT}/images/founder-canberk-kivilcim.jpg",
    "images/ Bild kopieren"
)
run_ssh_command(
    f"cp {FTP_PATH}/assets/founder-canberk-kivilcim.jpg {DOC_ROOT}/assets/founder-canberk-kivilcim.jpg",
    "assets/ Bild kopieren"
)
print()

# Setze Berechtigungen
print("🔧 Setze Berechtigungen...")
run_ssh_command(f"chmod 755 {DOC_ROOT}/images {DOC_ROOT}/assets && chown {OWNER} {DOC_ROOT}/images {DOC_ROOT}/assets", "Ordner-Berechtigungen")

for html_file in html_files:
    filename = html_file.name
    run_ssh_command(
        f"chmod 644 {DOC_ROOT}/{filename} && chown {OWNER} {DOC_ROOT}/{filename}",
        f"{filename} Berechtigungen"
    )

run_ssh_command(
    f"chmod 644 {DOC_ROOT}/images/founder-canberk-kivilcim.jpg {DOC_ROOT}/assets/founder-canberk-kivilcim.jpg && chown {OWNER} {DOC_ROOT}/images/founder-canberk-kivilcim.jpg {DOC_ROOT}/assets/founder-canberk-kivilcim.jpg",
    "Bild-Berechtigungen"
)
print()

# Lösche unnötige Dateien
print("🗑️  Lösche unnötige Dateien...")
success, file_list = run_ssh_command(f"ls {DOC_ROOT}/*.html 2>/dev/null", "HTML-Dateien auflisten")
if success:
    files = file_list.split('\n')
    for file_line in files:
        if file_line.strip():
            filename = os.path.basename(file_line.strip())
            if filename not in IMPORTANT_FILES and filename.endswith('.html'):
                run_ssh_command(f"rm -f {DOC_ROOT}/{filename}", f"Lösche {filename}")

# Lösche Backup-Dateien
run_ssh_command(f"rm -f {DOC_ROOT}/*.bak {DOC_ROOT}/*.backup {DOC_ROOT}/*.old 2>/dev/null", "Lösche Backup-Dateien")
print()

# Finale Prüfung
print("🔍 Finale Prüfung...")
run_ssh_command(f"ls -lh {DOC_ROOT}/*.html | head -10", "HTML-Dateien")
print()
run_ssh_command(f"ls -lh {DOC_ROOT}/images/founder-canberk-kivilcim.jpg {DOC_ROOT}/assets/founder-canberk-kivilcim.jpg", "Bilder")
print()

print("=" * 60)
print("✅ FERTIG! ALLES AUTOMATISCH ERLEDIGT!")
print("=" * 60)
print()
print("🧪 Teste jetzt:")
print("   1. Warte 1-2 Minuten")
print("   2. Hard Refresh: Cmd+Shift+R")
print("   3. Teste alle Seiten")
print()
