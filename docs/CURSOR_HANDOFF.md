# Cursor Handoff — CanGo Daily Todo Master

**Stand:** Mai 2026 | Branch: `claude/cango-todo-master-expand-huosk`
**Speicherort:** `website/intern/` — internes Feature, nicht öffentlich zugänglich
**Zuletzt aktualisiert:** Umstrukturierung → intern/ Ordner + Neuer Telegram-Bot + Nanobana-Klärung

---

## Was das System ist

Ein KI-gesteuertes persönliches Betriebssystem für Canberk Kivilcim (CanGo App Empire).
Kein Framework — reines HTML/CSS/JS + n8n Automations-Backend.

**Vision:** Seite öffnen → Jarvis analysiert Situation → 3–5 priorisierte Aufgaben mit Begründung.

---

## Kern-Dateien

```
website/intern/daily-todo-master.html  ← Hauptseite (intern, noindex, self-contained)
website/intern/index.html              ← Landing-Page für interne Tools
website/intern/.htaccess               ← X-Robots-Tag: noindex,nofollow
scripts/n8n_jarvis_analyzer.json       ← Das Gehirn: Claude analysiert → JSON Missions
scripts/n8n_brainstorm_bots.json       ← 4-Flow Suite: Morgen/Abend/Woche/Gemini
scripts/n8n_task_confirm.json          ← Telegram Queue: Start/Skip/Done + Micro-Step
scripts/n8n_voice_report.json          ← Sprachnachricht → Whisper → Energie-Level
scripts/n8n_escalation_workflow.json   ← Block-Timer Eskalation
scripts/n8n_avatar_pipeline.json       ← HeyGen Video-Produktion
scripts/.env                           ← API Keys (NIE committen, git-ignored)
```

---

## Design-System (NICHT ÄNDERN)

```css
--bg: #05070c          /* Hintergrund */
--orange: #F97316      /* Primärfarbe */
--navy-700: #111c30    /* Cards */
--font-body: 'Outfit', 'DM Sans', sans-serif
--font-mono: 'JetBrains Mono', monospace
--radius-lg: 12px
```

---

## Jarvis Intelligence Layer (Kern-Logik)

### Wie es funktioniert

1. `buildJarvisContext()` liest aus localStorage: Umsatz, Streak, Outreach, Energie-Level
2. POST an n8n-Webhook (`/jarvis-analyze`) mit dem Kontext-Objekt
3. Claude `claude-opus-4-7` analysiert und gibt JSON zurück:
   ```json
   { "missions": [{"rank":1,"task":"...","pillar":"...","why":"...","tools":[]}], "daily_focus":"...", "alert":null }
   ```
4. Offline-Fallback: `renderJarvisOffline(ctx)` — regelbasierte Priorisierung ohne API

### Kontext-Objekt (was an Claude gesendet wird)
```javascript
{
  date, dayName, daysLeft,
  monthRevenue, monthGoal, monthPct, revenueGap,
  streak, lastOutreach, doneTodayPct,
  energyLevel,      // 1–10, aus Abend-Slider
  moodCheck,        // true wenn energyLevel >= 5
  deepRestNeeded,   // true wenn < 3
  maxTasksPensum,   // 2/3/5 je nach Energie
  vision: { goal:9900000, yearRevenue, delta, monthlyNeed, focusSignal }
}
```

### Energie-System
- **Slider 1–10** im Abend-Review → `localStorage MOOD_KEY = 'cango_mood_YYYY-MM-DD'`
- `deepRestNeeded` (<3) → Banner + nur 2 Tasks + Pflichtpause als Mission #1
- `maxTasksPensum` steuert wie viele Missions Jarvis liefert

---

## Navi-Modus (Ein-Aufgaben-Ansicht)

```javascript
// Zustand
localStorage 'cango_navi_mode'     // '1' = an, '0' = aus
localStorage 'cango_navi_idx_TODAY' // aktueller Index

// Funktionen
toggleNaviMode()      // Button oben im Jarvis-Block
naviAdvance()         // Erledigt → nächste Aufgabe
naviReset()           // Alle erledigt → Reset
```

---

## localStorage Keys (alle)

| Key | Inhalt |
|-----|--------|
| `cango_todo_YYYY-MM-DD` | Checkbox-Status des Tages |
| `cango_outreach_v2` | Outreach-Tabelle (Array) |
| `cango_streak_v1` | `{current, best, last}` |
| `cango_finance_YYYY-MM` | `{total, entries[]}` |
| `cango_vision` | Jahresumsatz-Eingabe (€) |
| `cango_mood_YYYY-MM-DD` | Energie-Level (1–10) |
| `cango_navi_mode` | Navi-Modus an/aus |
| `cango_navi_idx_YYYY-MM-DD` | Aktueller Mission-Index |
| `cango_jarvis_cfg` | `{webhookUrl}` |
| `cango_jarvis_cache_YYYY-MM-DD` | Jarvis-Missions (täglich gecacht) |
| `cango_notif_config` | Eskalations-Webhook Config |
| `cango_block_state_YYYY-MM-DD` | Block Start/Done Status |
| `cango_bots_v2` | Bot-Tabelle |

---

## n8n Workflows — Setup-Reihenfolge

### 1. Jarvis Analyzer (Pflicht für KI-Missions)
```
scripts/n8n_jarvis_analyzer.json importieren
→ Webhook-URL: https://[n8n-domain]/webhook/jarvis-analyze
→ In daily-todo-master.html im Jarvis-Block eintragen
```

### 2. Task-Queue (täglicher Telegram-Push)
```
scripts/n8n_task_confirm.json importieren
→ Tabelle in Supabase anlegen (SQL unten)
→ Bot muss Webhook-Modus haben (nicht Polling)
```

### 3. Brainstorm Bots (optional, aber wertvoll)
```
scripts/n8n_brainstorm_bots.json importieren
→ GEMINI_API_KEY in n8n Env-Vars
→ Cron läuft automatisch
```

### Supabase SQL (einmalig ausführen)
```sql
-- Jarvis Gedächtnis
CREATE TABLE jarvis_missions (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  date date UNIQUE,
  missions jsonb,
  daily_focus text,
  context jsonb,
  created_at timestamptz DEFAULT now()
);

-- Task Bestätigungen (für Task-Queue)
CREATE TABLE task_confirmations (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  date date,
  task_rank int,
  status text DEFAULT 'pending',
  skip_count int DEFAULT 0,
  started_at timestamptz,
  completed_at timestamptz,
  UNIQUE(date, task_rank)
);

-- Outreach Leads
CREATE TABLE outreach_leads (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  company text,
  email text,
  status text,
  created_at timestamptz DEFAULT now()
);
```

---

## Offene Aufgaben für Cursor

### Priorität 1 — Aktivierung (ohne diese läuft nichts live)

- [x] **Supabase anlegen**: `kekmslytyttcipanwdop` · eu-central-1 · URL + Key in `.env` ✅
- [x] **SQL-Tabellen erstellt**: jarvis_missions, task_confirmations, outreach_leads, avatar_productions, knowledge_base ✅
- [ ] **TELEGRAM_CHAT_ID**: `/start` an `@CanGo_ToDo_Master_bot` → ID aus Telegram API holen
- [ ] **n8n Jarvis-Webhook-URL** in `website/intern/daily-todo-master.html` Jarvis-Block eintragen
- [ ] **Supabase-Keys in n8n Env-Vars** eintragen: `SUPABASE_URL` + `SUPABASE_ANON_KEY`

### Priorität 2 — Dashboard-Verbesserungen

- [ ] **Monatsumsatz aus localStorage validieren**: `saveFinance()` prüfen ob Wert korrekt summiert
- [ ] **AppSumo LTD-Zähler**: Subtitle sagt noch "14 Tools" → auf 19 updaten
- [ ] **Mobile-Optimierung Jarvis-Block**: KPI-Pills auf kleinen Screens testen
- [ ] **Jarvis-System-Prompt erweitern**: "Nanobana"-Tool einbauen wenn Canberk den Namen klärt

### Priorität 3 — Neue Features

- [ ] **Emergency-Override-Button**: Manuelles Veto für Jarvis-Missions (setzt Cache zurück, triggert Offline-Priorisierung mit benutzerdefiniertem Fokus)
- [ ] **Stripe/Sheet Umsatz-Sync**: Automatischer Einnahmen-Feed statt manuelle Eingabe
- [ ] **Whisper lokal auf VPS**: `pip install openai-whisper && whisper --model small` statt OpenAI API

### Was NICHT geändert werden soll

- `.env` Datei — nie committen
- Design-System Farben (`--orange`, `--bg`, etc.)
- localStorage Key-Namen (breaking change)
- n8n Workflow-Namen (verweisen aufeinander)

---

## Aktuelle API Keys (in .env, NIE ins Repo committen)

| Key | Wert/Status | Bot |
|-----|-------------|-----|
| `GEMINI_API_KEY` | ✅ eingetragen | Brainstorm + Content-Ideen |
| `TELEGRAM_BOT_TOKEN` | ✅ `@CanGo_ToDo_Master_bot` (NEU) | Jarvis Task-Queue, Briefings |
| `TELEGRAM_BOT_TOKEN_OLD` | ✅ `@Cango_master_bot` (ALT) | Eskalation, Avatar-Pipeline |
| `TELEGRAM_CHAT_ID` | ⬜ **FEHLT — Priorität 1** | Beide Bots senden hierhin |
| `SUPABASE_URL` | ✅ `https://kekmslytyttcipanwdop.supabase.co` | Missions, Task-Confirm, Outreach |
| `SUPABASE_ANON_KEY` | ✅ eingetragen (in .env) | Supabase Auth |
| `GOOGLE_MAPS_API_KEY` | ⬜ optional | outreach_sniper.py |
| `OPENAI_API_KEY` | ⬜ optional | Whisper Voice-to-Text |
| `GSHEETS_SERVICE_ACCOUNT_JSON` | ⬜ lokal auf Mac | Agency Funnel Sync |

### TELEGRAM_CHAT_ID holen (30 Sekunden)
1. Telegram → `@CanGo_ToDo_Master_bot` → `/start` senden
2. Im Browser aufrufen:
   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```
3. `result[0].message.chat.id` — diese Zahl in `.env` und n8n eintragen

---

## Nanobana — Geklärt

**"Nanobana"** = **Nano-Banana** — ein Blog-Cover-Generator-Workflow.
- Generiert automatisch Titelbild-Thumbnails für Blog-Posts
- Ist Content-Tool, kein Teil des Todo-Masters
- Optional: Mit Montags-Content-Posts verknüpfen (Gemini generiert Post → Nano-Banana generiert Bild)
- Liegt in Cursor-Workspace als `docs/n8n/nano-banana-blog-cover-workflow.json`

---

## Zwei Repos — Klare Trennung

| Repo | Inhalt | Git-Branch |
|------|--------|-----------|
| `Cango-Empire` (dieses) | daily-todo-master.html, n8n Workflows, Jarvis | `claude/cango-todo-master-expand-huosk` |
| `Cango-Empire` (lokal Mac) | Agency Funnel Python, GSheets Sync, outreach_sniper.py | `main` (Cursor) |

**Problem:** Cursor hat `daily-todo-master.html` und n8n-JSONs ins Python-Repo gelegt.
**Fix:** Die HTML-Datei gehört ins Website-Repo (dieses hier), nicht ins Python-Repo.

---

## Git-Workflow

```bash
# Branch
git checkout claude/cango-todo-master-expand-huosk

# Commit
git add website/intern/ scripts/
git commit -m "feat: ..."
git push -u origin claude/cango-todo-master-expand-huosk
```

---

## Bekannte Bugs (bereits gefixt)

- ✅ `n8n_task_confirm.json`: Node "Calc-Skip berechnen" falsch referenziert → gefixt auf "Skip-Count berechnen"
- ✅ CSS-Klasse `esc-info` fehlte → ergänzt
- ✅ Notification-Panel IDs stimmten nicht mit JS überein → gefixt

---

*Letzte Aktualisierung: 2026-05-22*
