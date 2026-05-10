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
Benötigt funktionierenden SSH-Login und optional `CANGO_SSH_*` in `.env` (siehe `.env.example`). Auf dem Hostinger-VPS ist SSH oft **Port 2222** (`ssh -p 2222 root@31.97.56.197`), nicht 22. SSH-Key: `ssh-copy-id -p 2222 root@31.97.56.197`.

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
