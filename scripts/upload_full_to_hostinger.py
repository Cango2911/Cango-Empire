#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Vollständiger Upload zu Hostinger (HTML + Bilder + Blogs)
Überträgt website/ komplett via FTP auf den VPS.
"""

import ftplib
import os
from pathlib import Path

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"
REMOTE_BASE = "/docker/nginx-proxy-manager-5tiw/www"

REPO_PATH = Path("/Users/canberkkivilcim/PycharmProjects/Cango-Empire")
WEBSITE_DIR = REPO_PATH / "website"

def ensure_remote_dir(ftp: ftplib.FTP, remote_path: str):
    """Erstellt Remote-Verzeichnis falls nicht vorhanden."""
    parts = remote_path.strip("/").split("/")
    current = "/"
    for part in parts:
        current = f"{current}{part}/"
        try:
            ftp.cwd(current)
        except ftplib.error_perm:
            try:
                ftp.mkd(current)
                ftp.cwd(current)
            except Exception as e:
                print(f"  ⚠ mkd {current}: {e}")

def upload_file(ftp: ftplib.FTP, local: Path, remote_path: str) -> bool:
    try:
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {remote_path}", f)
        return True
    except Exception as e:
        print(f"  ✗ {local.name}: {e}")
        return False

def upload_dir(ftp: ftplib.FTP, local_dir: Path, remote_dir: str):
    """Rekursiv ein lokales Verzeichnis hochladen."""
    ensure_remote_dir(ftp, remote_dir)
    ftp.cwd(remote_dir)

    ok = 0
    fail = 0
    for item in sorted(local_dir.iterdir()):
        if item.name.startswith(".") or item.name.endswith(".bak"):
            continue
        if item.is_dir():
            upload_dir(ftp, item, f"{remote_dir}/{item.name}")
            ftp.cwd(remote_dir)  # zurück ins parent
        else:
            if upload_file(ftp, item, item.name):
                print(f"  ↑ {remote_dir}/{item.name}")
                ok += 1
            else:
                fail += 1
    return ok, fail

def main():
    print("\n" + "=" * 65)
    print("📤 CanGo Empire – Vollständiger Upload zu Hostinger VPS")
    print("=" * 65)
    print(f"   Quelle:  {WEBSITE_DIR}")
    print(f"   Ziel:    {FTP_HOST}{REMOTE_BASE}")
    print()

    if not WEBSITE_DIR.exists():
        print("❌ website/ Verzeichnis nicht gefunden!")
        return

    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        print("✅ FTP-Verbindung hergestellt\n")
    except Exception as e:
        print(f"❌ FTP-Verbindung fehlgeschlagen: {e}")
        return

    try:
        total_ok = 0
        total_fail = 0

        # Alle Dateien und Unterordner in website/ hochladen
        for item in sorted(WEBSITE_DIR.iterdir()):
            if item.name.startswith(".") or item.name.endswith(".bak"):
                continue
            if item.is_dir():
                print(f"\n📁 Ordner: {item.name}/")
                ok, fail = upload_dir(ftp, item, f"{REMOTE_BASE}/{item.name}")
                total_ok += ok
                total_fail += fail
                ftp.cwd(REMOTE_BASE)
            else:
                ftp.cwd(REMOTE_BASE)
                if upload_file(ftp, item, item.name):
                    print(f"  ↑ {item.name}")
                    total_ok += 1
                else:
                    total_fail += 1

    except Exception as e:
        print(f"\n❌ Fehler während Upload: {e}")
    finally:
        ftp.quit()

    print("\n" + "=" * 65)
    print(f"✅ {total_ok} Dateien hochgeladen, {total_fail} Fehler")
    print("=" * 65)
    print("\n🌐 Live unter: https://automation-cango-app-empire.com\n")

if __name__ == "__main__":
    main()
