#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CanGo Empire – Depositphotos sortieren + Blogs automatisch zuweisen + FTP deploy.
Schritt 1: Bilder nach Nische in Ordner sortieren.
Schritt 2: Beste Bilder pro Blog-Artikel automatisch auswählen.
Schritt 3: FTP Upload.
"""
import ftplib, shutil
from pathlib import Path

DOWNLOADS = Path("/Users/canberkkivilcim/Downloads")
ROOT      = Path(__file__).parent.parent
POOL      = ROOT / "website" / "images" / "stock-pool"
IMG_DIR   = ROOT / "website" / "images" / "blog-sections"
IMG_DIR.mkdir(parents=True, exist_ok=True)

from cango_env import ftp_credentials

FTP_HOST, FTP_USER, FTP_PASS = ftp_credentials()
REMOTE   = "/docker/nginx-proxy-manager-5tiw/www"

# ── Schritt 1: Nischen-Sortierung (visuell geprüft) ───────────────────────────
NISCHEN = {
    "immobilien": [
        "Depositphotos_11497591_XL.jpg",    # Modernes Haus mit Pool / Abend
        "Depositphotos_116102506_XL.jpg",   # Modernes Haus beleuchtet bei Nacht
        "Depositphotos_166488312_XL.jpg",   # Familie mit Makler beim Hausbesuch
        "Depositphotos_167932260_XL.jpg",   # Umzugskartons vor Backsteinhaus
        "Depositphotos_181553704_XL.jpg",   # Hände halten kleines Hausmodell
        "Depositphotos_182028964_XL.jpg",   # Makler übergibt Schlüssel an Paar
        "Depositphotos_18468017_XL.jpg",    # Einstöckiges Backsteinhaus mit Garten
        "Depositphotos_192115056_XL.jpg",   # Modernes zweistöckiges weißes Haus
        "Depositphotos_194489554_XL.jpg",   # Modernes Wohnzimmer Innenraum
        "Depositphotos_204323480_XL.jpg",   # Glückliche Familie vor neuem Haus
        "Depositphotos_209894484_XL.jpg",   # Modernes minimalistisches Haus
        "Depositphotos_209898378_XL.jpg",   # Luxus-Wohnzimmer mit Kamin
        "Depositphotos_219687160_XL.jpg",   # Makler zeigt Haus an Kunden
        "Depositphotos_222087092_XL.jpg",   # Makler übergibt Schlüssel
        "Depositphotos_262184220_XL.jpg",   # Makler diskutiert Haus mit Käufer
        "Depositphotos_27009191_XL.jpg",    # Paar hält kleines Haus mit Bäumen
        "Depositphotos_32842075_XL.jpg",    # Paar umarmt sich vor modernem Haus
        "Depositphotos_338985112_XL.jpg",   # Junges Paar zeigt Schlüssel / neues Haus
        "Depositphotos_347474960_XL.jpg",   # Paar feiert mit Schlüssel zum neuen Haus
        "Depositphotos_38651493_XL.jpg",    # Modernes Backsteinhaus weiß
        "Depositphotos_43555575_XL.jpg",    # Paar umarmt sich vor Haus
        "Depositphotos_46127855_XL.jpg",    # Paar hält Miniaturhaus
        "Depositphotos_51673827_XL.jpg",    # Paar auf Sofa mit Immobilienmakler
        "Depositphotos_541022436_XL.jpg",   # Elegantes zweistöckiges Haus mit Tor
        "Depositphotos_564806392_XL.jpg",   # Modernes weißes Haus mit schwarzen Akzenten
        "Depositphotos_664926302_XL.jpg",   # Luftaufnahme neues Haus Vorort
        "Depositphotos_668169948_XL.jpg",   # Elegantes Wohnzimmer Innenraum
        "Depositphotos_698170366_XL.jpg",   # Eleganter Hausflur mit Treppe
        "Depositphotos_700683604_XL.jpg",   # Modernes schwarzes Backsteinhaus
        "Depositphotos_756612564_XL.jpg",   # Luftaufnahme moderne Vorstadthäuser
        "Depositphotos_77744932_XL.jpg",    # Orange-weißes modernes Architekturhaus
        "Depositphotos_78614118_XL.jpg",    # Paar Handschlag mit Immobilienmakler
        "Depositphotos_788210678_XL.jpg",   # Modernes Backsteinhaus minimales Design
        "Depositphotos_85002538_XL.jpg",    # Elegantes Wohnzimmer mit Kamin
        "Depositphotos_8657542_XL.jpg",     # Eleganter Hausflur große Treppe
        "Depositphotos_8682668_XL.jpg",     # Luxus-Wohnzimmer mit Kamin
        "Depositphotos_8716836_XL.jpg",     # Modernes schwarzes Haus große Fenster
        "Depositphotos_87217232_XL.jpg",    # Paar Handschlag mit Immobilienmakler
    ],
    "solar": [
        "Depositphotos_206148856_XL.jpg",   # Techniker installiert Solarpanele auf Dach
        "Depositphotos_219685948_XL.jpg",   # Familie diskutiert Solarpanele am Haus
        "Depositphotos_21969917_XL.jpg",    # Solarpanele auf Dach / blauer Himmel
        "Depositphotos_220242586_XL.jpg",   # Techniker inspiziert Solaranlage
        "Depositphotos_24706113_XL.jpg",    # Techniker installiert große Solaranlage
        "Depositphotos_249312888_XL.jpg",   # Großes Solarfeld / Industrieanlage
        "Depositphotos_265895674_XL.jpg",   # Massives Solarpanel-Dach Industrieanlage
        "Depositphotos_28191355_XL.jpg",    # Backsteinhaus mit Solarpanelen auf Dach
        "Depositphotos_315216994_XL.jpg",   # Solarfeld bei Sonnenuntergang
        "Depositphotos_321818332_XL.jpg",   # Diagramm Solarenergie Verteilung Häuser
        "Depositphotos_335542270_XL.jpg",   # Mehrere Wohnhäuser mit Solardächern
        "Depositphotos_44067027_XL.jpg",    # Bunte Häuser mit Solarpanelen auf Dach
        "Depositphotos_478852100_XL.jpg",   # Techniker installiert Solarsystem auf Dach
        "Depositphotos_574363878_XL.jpg",   # Moderne Solarpanele auf Wohnhaus
        "Depositphotos_6395035_XL.jpg",     # Haus mit Solar und Thermalkollektoren
    ],
    "karriere": [
        "Depositphotos_195980124_XL.jpg",   # Business-Team beim Meeting am Tisch
        "Depositphotos_195982144_XL.jpg",   # Profi präsentiert beim Office-Meeting
        "Depositphotos_209195854_XL.jpg",   # Mann präsentiert vor Publikum mit Whiteboard
        "Depositphotos_209198656_XL.jpg",   # Business-Team gibt High-Five / Erfolg
        "Depositphotos_38183621_XL.jpg",    # Mann spricht vor großem Seminar-Publikum
        "Depositphotos_469514772_XL.jpg",   # Publikum stellt Fragen beim Seminar
        "Depositphotos_521295052_XL.jpg",   # Diverse Gruppe beim Seminar mit Speaker
        "Depositphotos_54060009_XL.jpg",    # Frau präsentiert Charts vor Business-Team
        "Depositphotos_647547666_XL.jpg",   # Großes Seminar-Publikum mit Profi-Speaker
        "Depositphotos_81645574_XL.jpg",    # Businessman und Frau geben Handschlag
        "Depositphotos_89996026_XL.jpg",    # Profi spricht zu Publikum auf Konferenz
    ],
    "coaching": [
        "Depositphotos_273411318_XL.jpg",   # Wortwolke Coaching und Begriffe
        "Depositphotos_369744646_XL.jpg",   # Person berührt Coaching Digital-Screen
        "Depositphotos_384110436_XL.jpg",   # Mann präsentiert Coaching-Vortrag auf Konferenz
        "Depositphotos_5111838_XL.jpg",     # Coaching Mentorship Grafik auf Touchscreen
        "Depositphotos_50020023_XL.jpg",    # Frau zeigt Coaching-Tablet mit Icons
        "Depositphotos_693208702_XL.jpg",   # Gelbe Coaching-Taste auf Tastatur
        "Depositphotos_712848692_XL.jpg",   # Coaching & Mentoring Text-Grafik Design
        "Depositphotos_715077332_XL.jpg",   # Tablet zeigt Coaching-Konzepte Skizze
        "Depositphotos_818216776_XL.jpg",   # Mann zeichnet Erfolgsplan / Motivations-Diagramm
        "Depositphotos_86049626_XL.jpg",    # Want → Can → Do Coaching Motivation
    ],
}

# ── Schritt 2: Blog-Zuordnung (beste Bilder pro Artikel) ──────────────────────
# Format: slug → [hero, section-1, section-2, section-3]
# Bilder aus den Nischen-Ordnern, thematisch präzise zugeordnet

BLOG_ASSIGNMENT = {
    # ── IMMOBILIEN ÜBERBLICK ──────────────────────────────────────────────────
    "immobilien": {
        "hero": ("immobilien", "Depositphotos_11497591_XL.jpg"),    # Modernes Haus Pool
        "s1":   ("immobilien", "Depositphotos_166488312_XL.jpg"),   # Familie mit Makler
        "s2":   ("immobilien", "Depositphotos_194489554_XL.jpg"),   # Modernes Wohnzimmer
        "s3":   ("immobilien", "Depositphotos_167932260_XL.jpg"),   # Umzug / neues Zuhause
    },

    # ── EIGENTUMSWOHNUNG KAUFEN ───────────────────────────────────────────────
    "artikel-eigentumswohnung-kaufen-2026": {
        "hero": ("immobilien", "Depositphotos_338985112_XL.jpg"),   # Paar mit Schlüssel
        "s1":   ("immobilien", "Depositphotos_78614118_XL.jpg"),    # Handschlag Makler (Kosten/Notar)
        "s2":   ("immobilien", "Depositphotos_51673827_XL.jpg"),    # Beratung auf Sofa (Finanzierung)
        "s3":   ("immobilien", "Depositphotos_8716836_XL.jpg"),     # Modernes Haus (Energieeffizienz)
    },

    # ── ENERGIE & SOLAR ÜBERBLICK ─────────────────────────────────────────────
    "energie-solar": {
        "hero": ("solar", "Depositphotos_21969917_XL.jpg"),         # Solarpanele Dach blauer Himmel
        "s1":   ("solar", "Depositphotos_206148856_XL.jpg"),        # Techniker installiert Panele
        "s2":   ("solar", "Depositphotos_249312888_XL.jpg"),        # Großes Solarfeld (Speicher-Kontext)
        "s3":   ("solar", "Depositphotos_219685948_XL.jpg"),        # Familie + Solar (ganzheitlich)
    },

    # ── SOLARANLAGE RATGEBER ──────────────────────────────────────────────────
    "artikel-solaranlage-ratgeber-2026": {
        "hero": ("solar", "Depositphotos_574363878_XL.jpg"),        # Moderne Solarpanele Wohnhaus
        "s1":   ("solar", "Depositphotos_6395035_XL.jpg"),          # Haus Solar + Thermalkollektoren (Kosten)
        "s2":   ("solar", "Depositphotos_315216994_XL.jpg"),        # Solarfeld Sonnenuntergang (Förderung)
        "s3":   ("solar", "Depositphotos_478852100_XL.jpg"),        # Techniker Dach Montage (Anbieter)
    },

    # ── KARRIERE & HR ─────────────────────────────────────────────────────────
    "karriere-hr": {
        "hero": ("karriere", "Depositphotos_195980124_XL.jpg"),     # Business Team Meeting
        "s1":   ("karriere", "Depositphotos_54060009_XL.jpg"),      # Präsentation Charts (Skills)
        "s2":   ("karriere", "Depositphotos_647547666_XL.jpg"),     # Großes Seminar Publikum (Remote)
        "s3":   ("karriere", "Depositphotos_81645574_XL.jpg"),      # Handschlag (Selbstständigkeit)
    },

    # ── COACHING & MINDSET ────────────────────────────────────────────────────
    "coaching-mindset": {
        "hero": ("coaching", "Depositphotos_384110436_XL.jpg"),     # Coaching Vortrag Konferenz
        "s1":   ("coaching", "Depositphotos_818216776_XL.jpg"),     # Erfolgsplan zeichnen (Growth Mindset)
        "s2":   ("coaching", "Depositphotos_86049626_XL.jpg"),      # Want→Can→Do (Systeme/Willenskraft)
        "s3":   ("coaching", "Depositphotos_5111838_XL.jpg"),       # Mentorship Touchscreen (Coaching)
    },

    # ── PRODUKTIVITÄT & ADHS ─────────────────────────────────────────────────
    "artikel-produktivitaet-adhs-systeme": {
        "hero": ("coaching", "Depositphotos_369744646_XL.jpg"),     # Digital Coaching Screen
        "s1":   ("karriere", "Depositphotos_209198656_XL.jpg"),     # Team High-Five (klassische Tipps)
        "s2":   ("coaching", "Depositphotos_273411318_XL.jpg"),     # Wortwolke Coaching (drei Säulen)
        "s3":   ("coaching", "Depositphotos_693208702_XL.jpg"),     # Coaching Key Tastatur (KI & ADHS)
    },
}

# ── Schritt 1 ausführen: Nischen-Ordner erstellen und Bilder sortieren ─────────
def sort_into_niches():
    print("📂 Sortiere Bilder in Nischen-Ordner...\n")
    for nische, files in NISCHEN.items():
        nische_dir = POOL / nische
        nische_dir.mkdir(parents=True, exist_ok=True)
        ok = 0
        for fname in files:
            src = DOWNLOADS / fname
            if src.exists():
                dest = nische_dir / fname
                if not dest.exists():
                    shutil.copy2(src, dest)
                ok += 1
            else:
                print(f"  ⚠ Nicht gefunden: {fname}")
        print(f"  ✓ {nische:15s} → {ok}/{len(files)} Bilder in stock-pool/{nische}/")
    print()

# ── Schritt 2: Bilder den Blogs zuweisen ─────────────────────────────────────
def assign_to_blogs():
    print("🎯 Weise Bilder den Blog-Artikeln zu...\n")
    assigned = {}
    for slug, imgs in BLOG_ASSIGNMENT.items():
        assigned[slug] = {}
        for key, (nische, fname) in imgs.items():
            src = POOL / nische / fname
            if not src.exists():
                # Fallback: direkt aus Downloads
                src = DOWNLOADS / fname
            if key == "hero":
                dest_name = f"{slug}-hero.jpg"
            else:
                n = key[1]
                dest_name = f"{slug}-section-{n}.jpg"
            dest = IMG_DIR / dest_name
            if src.exists():
                shutil.copy2(src, dest)
                assigned[slug][key] = dest_name
            else:
                print(f"  ✗ Fehlt: {fname} für {slug}/{key}")
        print(f"  ✓ {slug}")
    print()
    return assigned

# ── FTP Deploy ────────────────────────────────────────────────────────────────
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

def ftp_upload_file(ftp, local, name):
    try:
        with open(local, "rb") as f:
            ftp.storbinary(f"STOR {name}", f)
        return True
    except Exception as e:
        print(f"  ✗ FTP {name}: {e}")
        return False

def deploy_via_ftp(assigned):
    print("📤 FTP Upload...\n")
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, 21, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        print("  ✅ FTP verbunden\n")
    except Exception as e:
        print(f"  ❌ FTP: {e}")
        return

    remote_imgs = f"{REMOTE}/images/blog-sections"
    ftp_ensure_dir(ftp, remote_imgs)

    total = 0
    for slug, imgs in assigned.items():
        ftp_ensure_dir(ftp, remote_imgs)
        ftp.cwd(remote_imgs)
        for key, dest_name in imgs.items():
            local = IMG_DIR / dest_name
            if local.exists():
                if ftp_upload_file(ftp, local, dest_name):
                    total += 1
        print(f"  ↑ {slug} ({len(imgs)} Bilder)")

    ftp.quit()
    print(f"\n  ✅ {total} Dateien hochgeladen")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("\n" + "="*60)
    print("CanGo Empire – Bilder sortieren + zuweisen + deployen")
    print("="*60 + "\n")

    sort_into_niches()
    assigned = assign_to_blogs()
    deploy_via_ftp(assigned)

    print("\n" + "="*60)
    print("✅ Fertig!")
    print()
    print("📁 Nischen-Ordner:")
    for nische in NISCHEN:
        count = len(list((POOL / nische).glob("*.jpg")))
        print(f"   stock-pool/{nische}/ → {count} Bilder")
    print()
    print("🌐 Live-Blogs mit Depositphotos-Bildern:")
    for slug in BLOG_ASSIGNMENT:
        print(f"   https://automation-cango-app-empire.com/blogs/{slug}.html")
    print()
    print("💡 Neue Bilder hinzufügen:")
    print("   1. Depositphotos-Bild in ~/Downloads/ speichern")
    print("   2. In NISCHEN{} und BLOG_ASSIGNMENT{} eintragen")
    print("   3. Skript erneut ausführen")

if __name__ == "__main__":
    main()
