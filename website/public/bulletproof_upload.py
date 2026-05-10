#!/usr/bin/env python3
"""
🛡️ BULLETPROOF UPLOAD
=====================
Validiert Dateien BEVOR Upload
Verhindert Beschädigung
"""

import ftplib
from pathlib import Path
import hashlib

FTP_HOST = "145.223.115.121"
FTP_USER = "u447057499.automation-cango-app-empire.com"
FTP_PASS = "Cango2911@"

DOC_ROOT = "/"
SCRIPT_DIR = Path(__file__).parent

def validate_html_file(file_path):
    """Validiert HTML-Datei bevor Upload"""
    content = file_path.read_text(encoding='utf-8')
    
    errors = []
    warnings = []
    
    # Kritische Checks
    if '<!DOCTYPE html>' not in content:
        errors.append("❌ Kein DOCTYPE gefunden")
    
    if '<html' not in content:
        errors.append("❌ Kein <html> Tag gefunden")
    
    if '</html>' not in content:
        errors.append("❌ Kein </html> Tag gefunden")
    
    if '<body' not in content:
        errors.append("❌ Kein <body> Tag gefunden")
    
    if '</body>' not in content:
        errors.append("❌ Kein </body> Tag gefunden")
    
    # Warnungen
    body_count = content.count('<body')
    if body_count > 1:
        warnings.append(f"⚠️  Mehrere <body> Tags gefunden: {body_count}")
    
    if body_count == 0:
        errors.append("❌ KEIN <body> Tag gefunden!")
    
    # Prüfe ob Content vorhanden ist
    body_match = content.find('<body')
    if body_match != -1:
        body_content = content[body_match:content.find('</body>')]
        if len(body_content) < 500:
            warnings.append("⚠️  Body-Content scheint sehr kurz zu sein")
    
    return errors, warnings

def calculate_file_hash(file_path):
    """Berechnet MD5 Hash der Datei"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def upload_file_safe(ftp, local_path, remote_path, description):
    """Upload mit Validierung"""
    print(f"📤 {description}...")
    
    # 1. Validiere Datei
    errors, warnings = validate_html_file(local_path)
    
    if errors:
        print(f"   ❌ VALIDIERUNGSFEHLER:")
        for error in errors:
            print(f"      {error}")
        return False
    
    if warnings:
        print(f"   ⚠️  Warnungen:")
        for warning in warnings:
            print(f"      {warning}")
    
    # 2. Berechne Hash
    local_hash = calculate_file_hash(local_path)
    print(f"   📊 MD5 Hash: {local_hash[:16]}...")
    
    # 3. Upload
    try:
        with open(local_path, 'rb') as f:
            ftp.storbinary(f'STOR {remote_path}', f)
        print(f"   ✅ Upload erfolgreich")
        
        # 4. Verifiziere Upload
        try:
            server_size = ftp.size(remote_path)
            local_size = local_path.stat().st_size
            if server_size == local_size:
                print(f"   ✅ Größe verifiziert: {server_size:,} Bytes")
            else:
                print(f"   ⚠️  Größen-Unterschied: Server={server_size:,}, Lokal={local_size:,}")
        except:
            print(f"   ⚠️  Größen-Verifizierung nicht möglich")
        
        # 5. Setze Berechtigungen
        try:
            ftp.sendcmd(f'SITE CHMOD 644 {remote_path}')
            print(f"   ✅ Berechtigungen gesetzt (644)")
        except:
            print(f"   ⚠️  Berechtigungen konnten nicht gesetzt werden")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Upload fehlgeschlagen: {e}")
        return False

print("=" * 60)
print("🛡️  BULLETPROOF UPLOAD")
print("=" * 60)
print()

# Prüfe Dateien
produkte_file = SCRIPT_DIR / "produkte.html"
ueber_uns_file = SCRIPT_DIR / "ueber-uns.html"

if not produkte_file.exists():
    print(f"❌ {produkte_file} nicht gefunden!")
    exit(1)

if not ueber_uns_file.exists():
    print(f"❌ {ueber_uns_file} nicht gefunden!")
    exit(1)

print("✅ Dateien gefunden")
print(f"   - produkte.html: {produkte_file.stat().st_size:,} Bytes")
print(f"   - ueber-uns.html: {ueber_uns_file.stat().st_size:,} Bytes")
print()

# FTP-Verbindung
print("📤 Verbinde zu FTP...")
try:
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, 21, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(DOC_ROOT)
    print("✅ FTP verbunden")
    print()
except Exception as e:
    print(f"❌ FTP Fehler: {e}")
    exit(1)

# Upload produkte.html
print("=" * 60)
print("1️⃣  PRODUKTE.HTML")
print("=" * 60)
print()
success_produkte = upload_file_safe(ftp, produkte_file, "produkte.html", "Lade produkte.html hoch")
print()

# Upload ueber-uns.html
print("=" * 60)
print("2️⃣  UEBER-UNS.HTML")
print("=" * 60)
print()
success_ueber_uns = upload_file_safe(ftp, ueber_uns_file, "ueber-uns.html", "Lade ueber-uns.html hoch")
print()

ftp.quit()

# Finale Zusammenfassung
print("=" * 60)
if success_produkte and success_ueber_uns:
    print("✅ ALLE DATEIEN ERFOLGREICH HOCHGELADEN!")
else:
    print("⚠️  UPLOAD MIT WARNUNGEN ABGESCHLOSSEN")
print("=" * 60)
print()
print("🧪 WICHTIG: Cache leeren!")
print("   1. Chrome DevTools (F12) → Network → 'Disable cache' aktivieren")
print("   2. Hard Refresh: Cmd+Shift+R (mehrmals)")
print("   3. Oder: Chrome → Einstellungen → Datenschutz → Browserdaten löschen")
print()
print("📋 Teste jetzt:")
print("   - https://automation-cango-app-empire.com/produkte.html")
print("   - https://automation-cango-app-empire.com/ueber-uns.html")
print()
