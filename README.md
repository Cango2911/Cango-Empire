# Cango Empire Website

## Überblick
Website für CanGo Empire - Marketing Automation Platform

## Struktur
- `website/` - HTML-Dateien
- `scripts/` - Python Scripts für Deployment und Wartung
- `docs/` - Dokumentation
- `docker/` - Docker Konfiguration

## Deployment
Die Website läuft auf Docker mit Nginx.

## Domain
- Domain: automation-cango-app-empire.com
- Server: 31.97.56.197:8080

## Scripts
- `upload_to_docker_www.py` - Upload HTML-Dateien ins Docker-Verzeichnis
- `move_sections_correct.py` - Verschiebe News-Sektionen
- `fix_index_html.py` - Korrigiere index.html

Siehe `docs/DOMAIN_BINDUNG_ANLEITUNG.md` für Domain-Konfiguration.
