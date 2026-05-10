#!/usr/bin/env python3
"""
🚀 UPLOAD FIXIERTE DATEIEN
==========================
Lädt die korrigierten produkte.html und ueber-uns.html hoch
"""

import ftplib
from pathlib import Path

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
SCRIPT_DIR = Path(__file__).parent

# Pfade zu den Dateien
PRODUKTE_FILE = SCRIPT_DIR / "produkte.html"
UEBER_UNS_FILE = SCRIPT_DIR / "ueber-uns.html"

print("=" * 60)
print("🚀 UPLOAD FIXIERTE DATEIEN")
print("=" * 60)
print()

# Prüfe ob Dateien existieren
if not PRODUKTE_FILE.exists():
    print(f"❌ {PRODUKTE_FILE} nicht gefunden!")
    exit(1)

if not UEBER_UNS_FILE.exists():
    print(f"❌ {UEBER_UNS_FILE} nicht gefunden!")
    exit(1)

print(f"✅ Dateien gefunden:")
print(f"   - produkte.html: {PRODUKTE_FILE.stat().st_size:,} Bytes")
print(f"   - ueber-uns.html: {UEBER_UNS_FILE.stat().st_size:,} Bytes")
print()

try:
    # Verbindung herstellen
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print("✅ FTP verbunden")
    print()
    
    # 1. Upload produkte.html
    print("📤 Lade produkte.html hoch...")
    with open(PRODUKTE_FILE, 'rb') as f:
        ftp.storbinary('STOR produkte.html', f)
    
    # Setze Berechtigungen
    try:
        ftp.sendcmd('SITE CHMOD 644 produkte.html')
        print("   ✅ produkte.html hochgeladen + Berechtigungen gesetzt")
    except:
        print("   ✅ produkte.html hochgeladen")
    
    # Prüfe Größe
    try:
        size = ftp.size('produkte.html')
        local_size = PRODUKTE_FILE.stat().st_size
        print(f"   📊 Größe: Server={size:,} Bytes, Lokal={local_size:,} Bytes")
        if size == local_size:
            print("   ✅ Größe stimmt überein")
        else:
            print(f"   ⚠️  Größen-Unterschied: {abs(size - local_size)} Bytes")
    except:
        print("   ⚠️  Größen-Prüfung nicht möglich")
    print()
    
    # 2. Upload ueber-uns.html
    print("📤 Lade ueber-uns.html hoch...")
    with open(UEBER_UNS_FILE, 'rb') as f:
        ftp.storbinary('STOR ueber-uns.html', f)
    
    # Setze Berechtigungen
    try:
        ftp.sendcmd('SITE CHMOD 644 ueber-uns.html')
        print("   ✅ ueber-uns.html hochgeladen + Berechtigungen gesetzt")
    except:
        print("   ✅ ueber-uns.html hochgeladen")
    
    # Prüfe Größe
    try:
        size = ftp.size('ueber-uns.html')
        local_size = UEBER_UNS_FILE.stat().st_size
        print(f"   📊 Größe: Server={size:,} Bytes, Lokal={local_size:,} Bytes")
        if size == local_size:
            print("   ✅ Größe stimmt überein")
        else:
            print(f"   ⚠️  Größen-Unterschied: {abs(size - local_size)} Bytes")
    except:
        print("   ⚠️  Größen-Prüfung nicht möglich")
    print()
    
    ftp.quit()
    
    print("=" * 60)
    print("✅ UPLOAD ERFOLGREICH!")
    print("=" * 60)
    print()
    print("🧪 WICHTIG: Cache leeren!")
    print("   1. Chrome DevTools öffnen (F12)")
    print("   2. Network → 'Disable cache' aktivieren")
    print("   3. Hard Refresh: Cmd+Shift+R (mehrmals)")
    print()
    print("🔗 Teste jetzt:")
    print("   - https://automation-cango-app-empire.com/produkte.html")
    print("   - https://automation-cango-app-empire.com/ueber-uns.html")
    print()
    
except Exception as e:
    print(f"❌ Fehler: {e}")
    import traceback
    traceback.print_exc()
