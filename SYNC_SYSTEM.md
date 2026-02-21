# 🔄 Automatisches Synchronisationssystem

## Übersicht

Alle erstellten/geänderten Dateien werden automatisch synchronisiert zu:

1. **Hostinger Docker** - Server (Website-Dateien)
2. **Docker Desktop** - Lokale Docker-Konfiguration
3. **GitHub (Cango2911)** - Versionskontrolle
4. **PyCharm** - Lokales Repository

## Verwendung

### Einzelne Datei synchronisieren:
```bash
cd /Users/canberkkivilcim/PycharmProjects/Cango-Empire
python3 scripts/sync_all_locations.py path/to/file.html
```

### Alle HTML-Dateien synchronisieren:
```bash
cd /Users/canberkkivilcim/PycharmProjects/Cango-Empire
python3 scripts/sync_all_locations.py
```

## Automatischer Workflow

Wenn ich (AI) eine Datei erstelle oder ändere, wird automatisch:

1. ✅ **Hostinger Docker**: Datei wird ins `/docker/nginx-proxy-manager-5tiw/www/` Verzeichnis hochgeladen
2. ✅ **PyCharm**: Datei wird ins lokale Repository kopiert
3. ✅ **GitHub**: Datei wird committed und gepusht

## Dateitypen

- **HTML-Dateien** → Hostinger Docker + GitHub + PyCharm
- **Python Scripts** → GitHub + PyCharm
- **Dokumentation** → GitHub + PyCharm
- **Docker Config** → GitHub + PyCharm

## Manuelle Synchronisation

Falls automatische Sync nicht funktioniert:

```bash
# 1. Hostinger Docker
python3 scripts/upload_to_docker_www.py

# 2. GitHub
cd /Users/canberkkivilcim/PycharmProjects/Cango-Empire
git add .
git commit -m "Update files"
git push origin main
```

## Konfiguration

Alle Einstellungen in `scripts/sync_all_locations.py`:
- FTP-Verbindung (Hostinger)
- Repository-Pfad (PyCharm/GitHub)
- Docker-Verzeichnis
