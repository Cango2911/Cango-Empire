#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Depositphotos-Bilder den Blogs zuordnen und deployen.
Kopiert kuratierte Depositphotos-Bilder in blog-sections/ und uploaded via FTP.
Nur für Blogs mit verfügbaren Depositphotos-Bildern (Immobilien, Solar, Karriere, Coaching).
"""
import ftplib, shutil, time
from pathlib import Path

DOWNLOADS = Path("/Users/canberkkivilcim/Downloads")
ROOT      = Path(__file__).parent.parent
IMG_DIR   = ROOT / "website" / "images" / "blog-sections"
BLOGS_DIR = ROOT / "website" / "blogs"
IMG_DIR.mkdir(parents=True, exist_ok=True)

from cango_env import ftp_credentials

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()
REMOTE   = "/docker/nginx-proxy-manager-5tiw/www"

# ── Bilderzuordnung: slug → {hero, s1, s2, s3} ────────────────────────────────
# Alle Bilder visuell geprüft und thematisch exakt zugeordnet
MAPPING = {
    # ── IMMOBILIEN ────────────────────────────────────────────────────────────
    "immobilien": {
        "hero": "Depositphotos_11497591_XL.jpg",     # Modernes Haus mit Pool / Abend
        "s1":   "Depositphotos_166488312_XL.jpg",    # Familie mit Makler beim Hausbesuch
        "s2":   "Depositphotos_194489554_XL.jpg",    # Modernes Wohnzimmer / Innenraum
        "s3":   "Depositphotos_167932260_XL.jpg",    # Umzugskartons vor Backsteinhaus
    },

    # ── ENERGIE & SOLAR (Übersicht) ───────────────────────────────────────────
    "energie-solar": {
        "hero": "Depositphotos_21969917_XL.jpg",     # Solarpanele auf Dach / blauer Himmel
        "s1":   "Depositphotos_206148856_XL.jpg",    # Techniker installiert Solarpanele
        "s2":   "Depositphotos_249312888_XL.jpg",    # Großes Solarfeld / Industrieanlage
        "s3":   "Depositphotos_219685948_XL.jpg",    # Familie diskutiert Solarpanele
    },

    # ── KARRIERE & HR ────────────────────────────────────────────────────────
    "karriere-hr": {
        "hero": "Depositphotos_195980124_XL.jpg",    # Business-Team beim Meeting
        "s1":   "Depositphotos_521295052_XL.jpg",    # Diverse Gruppe beim Seminar
        "s2":   "Depositphotos_469514772_XL.jpg",    # Fragen beim professionellen Seminar
        "s3":   "Depositphotos_81645574_XL.jpg",     # Businessman und Frau geben Handschlag
    },

    # ── COACHING & MINDSET ────────────────────────────────────────────────────
    "coaching-mindset": {
        "hero": "Depositphotos_384110436_XL.jpg",    # Mann präsentiert Coaching-Vortrag
        "s1":   "Depositphotos_818216776_XL.jpg",    # Mann zeichnet Erfolgsplan / Motivation
        "s2":   "Depositphotos_712848692_XL.jpg",    # Coaching & Mentoring Text-Grafik
        "s3":   "Depositphotos_5111838_XL.jpg",      # Coaching Mentorship Touchscreen
    },

    # ── EIGENTUMSWOHNUNG KAUFEN ───────────────────────────────────────────────
    "artikel-eigentumswohnung-kaufen-2026": {
        "hero": "Depositphotos_338985112_XL.jpg",    # Junges Paar zeigt Schlüssel / neues Haus
        "s1":   "Depositphotos_78614118_XL.jpg",     # Paar gibt Handschlag mit Immobilienmakler
        "s2":   "Depositphotos_51673827_XL.jpg",     # Paar auf Sofa mit Immobilienmakler
        "s3":   "Depositphotos_182028964_XL.jpg",    # Makler übergibt Schlüssel an Käufer
    },

    # ── SOLARANLAGE RATGEBER ──────────────────────────────────────────────────
    "artikel-solaranlage-ratgeber-2026": {
        "hero": "Depositphotos_574363878_XL.jpg",    # Moderne Solarpanele auf Wohnhaus
        "s1":   "Depositphotos_28191355_XL.jpg",     # Backsteinhaus mit Solarpanelen auf Dach
        "s2":   "Depositphotos_478852100_XL.jpg",    # Techniker installiert Solarsystem auf Dach
        "s3":   "Depositphotos_315216994_XL.jpg",    # Solarfeld bei Sonnenuntergang
    },

    # ── ARTIKEL-PRODUKTIVITAET (Seminar/Coaching-Kontext) ────────────────────
    "artikel-produktivitaet-adhs-systeme": {
        "hero": "Depositphotos_369744646_XL.jpg",    # Person tippt auf Coaching-Digitalscreen
        "s1":   "Depositphotos_273411318_XL.jpg",    # Coaching-Wortwolke / Begriffe
        "s2":   "Depositphotos_693208702_XL.jpg",    # Coaching-Taste auf Tastatur
        "s3":   "Depositphotos_50020023_XL.jpg",     # Frau zeigt Coaching-Tablet mit Icons
    },
}

def ftp_ensure_dir(ftp, path):
    parts = path.strip("/").split("/")
    cur = "/"
    for p in parts:
        cur = f"{cur}{p}/"
        try:
            ftp.cwd(cur)
        except ftplib.error_perm:
            try:
                ftp.mkd(cur)
                ftp.cwd(cur)
            except:
                pass

def ftp_upload(ftp, local, remote_name):
    try:
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {remote_name}", f)
        return True
    except Exception as e:
        print(f"  ✗ FTP {local.name}: {e}")
        return False

def main():
    print("\n🖼  CanGo Empire – Depositphotos → Blog-Bilder Deploy\n")

    # FTP verbinden
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        print("✅ FTP OK\n")
    except Exception as e:
        print(f"❌ FTP: {e}")
        return

    remote_imgs = f"{REMOTE}/images/blog-sections"
    ftp_ensure_dir(ftp, remote_imgs)

    total_ok = 0
    total_fail = 0

    for slug, imgs in MAPPING.items():
        print(f"📄 {slug}")
        uploaded_files = []

        for key, filename in imgs.items():
            src = DOWNLOADS / filename
            if not src.exists():
                print(f"  ✗ {key}: {filename} nicht gefunden!")
                total_fail += 1
                continue

            # Zielname je nach key
            if key == "hero":
                dest_name = f"{slug}-hero.jpg"
            else:
                n = key[1]  # s1→1, s2→2, s3→3
                dest_name = f"{slug}-section-{n}.jpg"

            dest = IMG_DIR / dest_name
            shutil.copy2(src, dest)
            print(f"  ✓ {key}: {filename[:45]}")

            # FTP Upload
            ftp_ensure_dir(ftp, remote_imgs)
            ftp.cwd(remote_imgs)
            if ftp_upload(ftp, dest, dest_name):
                uploaded_files.append(dest_name)
                total_ok += 1
            else:
                total_fail += 1

        print(f"  ↑ {len(uploaded_files)} Bilder live\n")

    ftp.quit()

    print("=" * 55)
    print(f"✅ {total_ok} Bilder deployed · {total_fail} Fehler")
    print()
    print("Betroffene Blogs (jetzt mit echten Depositphotos-Bildern):")
    for slug in MAPPING:
        print(f"  🌐 https://automation-cango-app-empire.com/blogs/{slug}.html")
    print()
    print("Restliche Blogs behalten Unsplash-Bilder (keine Depositphotos verfügbar):")
    print("  → crypto-web3, trading, finanzen-versicherung, ki-tech,")
    print("    automationen, artikel-pkv-vs-gkv-2026, artikel-bitcoin-institutionen-2026,")
    print("    artikel-claude-vs-chatgpt-unternehmen-2026")

if __name__ == "__main__":
    main()
