# Domain-Bindung: automation-cango-app-empire.com

## Aktuelle Situation
- **Domain:** automation-cango-app-empire.com
- **Aktuell:** Website läuft auf `31.97.56.197:8080`
- **Ziel:** Website über Domain erreichbar machen

## Schritt 1: DNS-Einstellungen prüfen

1. Gehe zu deinem Domain-Provider (wo du die Domain gekauft hast)
2. Prüfe DNS-Einstellungen:
   - **A-Record:** `automation-cango-app-empire.com` → `31.97.56.197`
   - **A-Record:** `www.automation-cango-app-empire.com` → `31.97.56.197` (optional)

## Schritt 2: Nginx Proxy Manager konfigurieren

1. **Öffne Nginx Proxy Manager:**
   - URL: `http://31.97.56.197:81`
   - Login mit deinen Credentials

2. **Erstelle neuen Proxy Host:**
   - Klicke auf "Proxy Hosts" → "Add Proxy Host"

3. **Details:**
   - **Domain Names:** `automation-cango-app-empire.com`
   - **Scheme:** `http`
   - **Forward Hostname / IP:** `automation-cango-app-empire-web` (Container-Name)
   - **Forward Port:** `80`
   - **Block Common Exploits:** ✅
   - **Websockets Support:** ✅ (falls nötig)

4. **SSL-Zertifikat hinzufügen:**
   - Klicke auf "SSL" Tab
   - **SSL Certificate:** "Request a new SSL Certificate"
   - **Force SSL:** ✅
   - **HTTP/2 Support:** ✅
   - **HSTS Enabled:** ✅
   - **Email:** Deine E-Mail-Adresse
   - Klicke auf "Save"

5. **Warte auf Zertifikat:**
   - Das Let's Encrypt Zertifikat wird automatisch erstellt (kann 1-2 Minuten dauern)

## Schritt 3: Container-Namen prüfen

Falls der Container-Name nicht funktioniert:

```bash
# Prüfe Container-Namen
docker ps | grep automation-cango

# Falls der Name anders ist, verwende:
# Forward Hostname: nginx-proxy-manager-5tiw-automation-cango-app-empire-web-1
# Forward Port: 80
```

## Schritt 4: Testen

1. Warte 5-10 Minuten (DNS-Propagation)
2. Teste: `http://automation-cango-app-empire.com`
3. Nach SSL: `https://automation-cango-app-empire.com`

## Alternative: Direkt über Nginx (ohne Proxy Manager)

Falls Nginx Proxy Manager nicht funktioniert, kannst du direkt einen Nginx-Container konfigurieren:

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./www:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    container_name: automation-cango-app-empire-web
    restart: unless-stopped
```

## Troubleshooting

**Problem:** Domain zeigt nicht auf Website
- **Lösung:** Prüfe DNS-Einstellungen, warte auf Propagation (bis zu 48h)

**Problem:** SSL-Zertifikat wird nicht erstellt
- **Lösung:** Prüfe ob Port 80 und 443 offen sind, prüfe DNS-Einstellungen

**Problem:** 502 Bad Gateway
- **Lösung:** Prüfe Container-Name und Port in Nginx Proxy Manager
