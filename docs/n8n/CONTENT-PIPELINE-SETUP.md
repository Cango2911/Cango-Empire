# CanGo Empire – Content Pipeline Setup

**Ziel:** Täglich 06:30 Uhr werden automatisch 6 Blog-Artikel generiert,
mit Depositphotos-Bildern versehen und live auf der Website deployt.

---

## Architektur

```
n8n (VPS) ─── täglich 06:30 ──► 6 Nischen nacheinander
  │
  ├─ GPT-4o: Keyword + Gliederung generieren
  ├─ GPT-4o: Vollständigen Artikel schreiben (950–1200 Wörter)
  ├─ blog_generator.py auf VPS ausführen:
  │    ├─ Depositphotos API: Login → 4 Bilder suchen + downloaden
  │    ├─ Markdown → HTML konvertieren
  │    ├─ Blog-HTML in /docker/nginx-proxy-manager-5tiw/www/blogs/ speichern
  │    └─ blogs.html aktualisieren (neue Karte ganz oben)
  └─ Slack: Erfolg/Fehler melden
```

---

## Schritt 1 – Python-Skript auf VPS einrichten

SSH auf den VPS und folgendes ausführen:

```bash
# Verzeichnis anlegen
mkdir -p /opt/cango

# blog_generator.py kopieren (aus diesem Repo)
# Option A: via git pull (wenn Repo auf VPS geklont)
cp /pfad/zum/repo/scripts/blog_generator.py /opt/cango/

# Option B: direkt mit scp vom Mac
scp scripts/blog_generator.py root@145.223.115.121:/opt/cango/

# Ausführbar machen
chmod +x /opt/cango/blog_generator.py

# .env anlegen (Credentials)
cp .env.example /opt/cango/.env
nano /opt/cango/.env
```

**Ausfüllen in `/opt/cango/.env`:**
```bash
DP_API_KEY=DEIN_ENTERPRISE_KEY
DP_USER=dein.login@email.com
DP_PASS=DeinPasswort
OPENAI_API_KEY=sk-proj-...
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
CANGO_WWW_ROOT=/docker/nginx-proxy-manager-5tiw/www
```

**Test – manuell ausführen:**
```bash
cd /opt/cango
source .env

echo '{
  "title": "KI-Tools für Freelancer 2026",
  "niche": "KI & Tech",
  "niche_slug": "ki-tech",
  "dp_keyword": "artificial intelligence technology business",
  "section_keywords": ["machine learning computer", "ai business office", "digital innovation tech"],
  "excerpt": "KI ist kein Zukunftsthema mehr – sie ist heute Alltag. Was Freelancer 2026 wirklich brauchen.",
  "meta_description": "Die besten KI-Tools für Freelancer 2026: Ehrlicher Vergleich, Praxiserfahrung, klare Empfehlungen.",
  "content_markdown": "## Warum KI für Freelancer jetzt Pflicht ist\n\nWer 2026 noch ohne KI-Tools arbeitet, verliert Zeit und Aufträge. Die Frage ist nicht ob, sondern welche Tools wirklich helfen.\n\n## Die 5 KI-Tools, die sich wirklich lohnen\n\n**ChatGPT Plus** bleibt die Basis: 20€/Monat für unbegrenzte GPT-4o Nutzung. Für Texte, Code, Übersetzungen und Recherche.\n\n## Kosten vs. Nutzen: Was rechnet sich?\n\nEin durchschnittlicher Freelancer spart mit KI-Tools 8–12 Stunden pro Woche. Bei einem Stundensatz von 60€ sind das 480–720€ monatlicher Mehrwert.",
  "tags": ["KI", "Tools", "Freelancer", "Produktivität"]
}' | python3 /opt/cango/blog_generator.py
```

Erwartete Ausgabe:
```json
{"success": true, "slug": "2026-05-05-ki-tools-fur-freelancer-2026", "url": "https://automation-cango-app-empire.com/blogs/2026-05-05-ki-tools-fur-freelancer-2026.html", ...}
```

---

## Schritt 2 – n8n Workflow importieren

1. n8n öffnen (z. B. `http://145.223.115.121:5678`)
2. **Workflows → Import from File**
3. Datei wählen: `docs/n8n/workflows/n8n_content_pipeline_v1.json`
4. Workflow öffnet sich → noch **nicht aktivieren**

---

## Schritt 3 – Umgebungsvariablen in n8n setzen

In n8n: **Settings → Environment Variables** (oder `.env` auf dem VPS):

| Variable | Wert |
|---|---|
| `OPENAI_API_KEY` | `sk-proj-...` |
| `SLACK_WEBHOOK_URL` | `https://hooks.slack.com/...` |

> **Hinweis:** `DP_API_KEY`, `DP_USER`, `DP_PASS` werden direkt vom
> Python-Skript aus `/opt/cango/.env` geladen – müssen nicht in n8n eingetragen werden.

---

## Schritt 4 – Erster manueller Testlauf

1. Workflow öffnen → **Execute Workflow** (Play-Button)
2. Beobachte den Ablauf im n8n-Editor
3. Prüfe nach ~3 Minuten:
   - Slack-Nachricht erhalten?
   - Neue Datei in `/docker/nginx-proxy-manager-5tiw/www/blogs/`?
   - `blogs.html` hat neue Karte ganz oben?
   - Blog live: `https://automation-cango-app-empire.com/blogs/YYYY-MM-DD-...html`

---

## Schritt 5 – Workflow aktivieren

Wenn der Testlauf erfolgreich war:
1. **Toggle „Active"** oben rechts im Workflow → grün
2. Ab sofort läuft der Workflow täglich um 06:30 Uhr (Berlin-Zeit)

---

## Troubleshooting

### DP-Bilder werden nicht geladen
- Prüfe `/opt/cango/.env`: Sind `DP_API_KEY`, `DP_USER`, `DP_PASS` korrekt?
- Test: `curl -d "dp_command=loginEnterprise&dp_apikey=KEY&dp_login_user=USER&dp_login_password=PASS" https://api.depositphotos.com`
- Antwort sollte `"type":"success"` und `"sessionid"` enthalten

### OpenAI gibt kein JSON zurück
- Das `response_format: {"type": "json_object"}` im HTTP-Request-Node erzwingt JSON
- Bei Fehler: im n8n Execution Log prüfen was GPT-4o zurückgegeben hat

### blog_generator.py schlägt fehl
- Manuell testen (siehe Schritt 1)
- Logs im n8n: "blog_generator.py ausführen" Node → `stderr`-Ausgabe lesen
- Häufige Ursache: `CANGO_WWW_ROOT` Pfad falsch → in `.env` prüfen

### blogs.html wird nicht aktualisiert
- Marker `<!-- NEUE BLOG-CARDS -->` muss in `blogs.html` vorhanden sein
- Prüfen: `grep -n "NEUE BLOG-CARDS" /docker/nginx-proxy-manager-5tiw/www/blogs.html`

### Permission-Fehler beim Schreiben
```bash
chown -R www-data:www-data /docker/nginx-proxy-manager-5tiw/www
chmod -R 755 /docker/nginx-proxy-manager-5tiw/www
```

---

## Nischen anpassen

Im n8n-Workflow, Node **"6 Nischen definieren"**, kannst du:
- `keywords_hint` für jede Nische anpassen (beeinflusst GPT-4o Themenauswahl)
- Neue Nischen hinzufügen (Array erweitern)
- Nischen temporär deaktivieren (aus Array entfernen)

Beispiel für neue Nische:
```json
{
  "slug": "crypto-web3",
  "name": "Crypto & Web3",
  "niche": "Crypto & Web3",
  "icon": "₿",
  "keywords_hint": "Bitcoin, Ethereum, DeFi, NFT, Krypto-Steuern, Web3-Investitionen"
}
```

---

## Dateistruktur nach erstem Lauf

```
/docker/nginx-proxy-manager-5tiw/www/
├── blogs.html                              ← neue Karte oben eingefügt
├── blogs/
│   ├── 2026-05-05-ki-tools-freelancer.html ← neu generiert
│   └── ... (bestehende Blogs)
└── images/
    └── blog-sections/
        ├── 2026-05-05-ki-tools-freelancer-hero.jpg     ← Depositphotos
        ├── 2026-05-05-ki-tools-freelancer-section-1.jpg
        ├── 2026-05-05-ki-tools-freelancer-section-2.jpg
        └── 2026-05-05-ki-tools-freelancer-section-3.jpg
```
