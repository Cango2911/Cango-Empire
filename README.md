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

**Empfohlen (VPS mit SSH):** Lokales `website/` per rsync hochladen:
```bash
./scripts/deploy_rsync_vps.sh
```
Benötigt funktionierenden SSH-Login (`ssh root@31.97.56.197`) und optional `CANGO_SSH_*` in `.env` (siehe `.env.example`). SSH-Key einrichten (`ssh-copy-id`), dann kein Passwort bei jedem Deploy.

**Alternativ:** FTP über `python3 scripts/upload_full_to_hostinger.py` (Zugangsdaten in `.env`).

## Domain
- Domain: automation-cango-app-empire.com
- Server: 31.97.56.197:8080

## Scripts
- `upload_to_docker_www.py` - Upload HTML-Dateien ins Docker-Verzeichnis
- `move_sections_correct.py` - Verschiebe News-Sektionen
- `fix_index_html.py` - Korrigiere index.html

Siehe `docs/DOMAIN_BINDUNG_ANLEITUNG.md` für Domain-Konfiguration.

## Secrets / API-Keys
- Die **statische Website** (`website/`) braucht **keine** API-Keys im Browser; das Short-Form-Studio arbeitet lokal im Client.
- **Skripte** (`scripts/`) lesen Zugangsdaten aus **`.env` im Repo-Root** (siehe `.env.example`). Niemals `.env` committen — steht in `.gitignore`.
- **FTP:** Alle Upload-Skripte nutzen `scripts/cango_env.py` und erwarten `FTP_PASS` (und optional `FTP_HOST` / `FTP_USER`) in `.env`. Keine Passwörter mehr im Python-Quelltext.
- Weitere Keys (OpenAI, n8n, …) nur für Workflows/Automation; siehe `docs/n8n/` und jeweilige Skripte.
