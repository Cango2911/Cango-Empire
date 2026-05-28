# n8n Setup Guide — CanGo Jarvis System

**Ziel:** 5 Workflows importieren → aktivieren → Jarvis denkt wirklich

**Stand:** Mai 2026 · Jarvis v2 (Gemini 2.0 Flash, keine Credentials nötig)

---

## SCHRITT 0 — n8n Environment Variables setzen (ZUERST!)

**n8n → Settings (Zahnrad) → Environment Variables → folgende 5 eintragen:**

| Variable | Wert |
|---------|------|
| `GEMINI_API_KEY` | `AIzaSyA-XoFVW5JdWQkMCrExNSXbhhdwI_2lRAM` |
| `SUPABASE_URL` | `https://kekmslytyttcipanwdop.supabase.co` |
| `SUPABASE_ANON_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imtla21zbHl0eXR0Y2lwYW53ZG9wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk0NDk3ODEsImV4cCI6MjA5NTAyNTc4MX0.hMXgc_4Ok294nAY6NlfnZoLtbRONn5woNo4fQyfDViI` |
| `TELEGRAM_BOT_TOKEN` | `8964673248:AAHVuB13ECDoZTdVmxH6KVw5Yl_dysXCSFI` |
| `TELEGRAM_CHAT_ID` | `7396952825` |

> **Warum wichtig?** Die Workflows verwenden `{{ $env.GEMINI_API_KEY }}` etc. als Platzhalter.
> Diese Platzhalter werden NUR aufgelöst, wenn die Werte in n8n selbst eingetragen sind —
> `scripts/.env` auf dem Mac ist für n8n unsichtbar.

Nach dem Eintragen: n8n **neu starten** oder kurz warten (1–2 Min) damit die Vars aktiv sind.

---

## SCHRITT 1 — Jarvis Analyzer importieren (Pflicht)

```
scripts/n8n_jarvis_analyzer.json
```

**n8n → New Workflow → Import from JSON → Datei hochladen → Active (oben rechts)**

- Kein Credential-Setup nötig (v2 nutzt HTTP Request + Env-Vars)
- Webhook-URL nach Aktivierung:
  ```
  https://n8n.automation-cango-app-empire.com/webhook/jarvis-analyze
  ```
- Diese URL in `website/intern/daily-todo-master.html` eintragen:
  → Seite öffnen → Jarvis-Block ganz oben → Webhook-URL-Feld → **Webhook speichern**

### Testen (nach Aktivierung):
```bash
curl -X POST https://n8n.automation-cango-app-empire.com/webhook/jarvis-analyze \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-05-28","dayName":"Donnerstag","daysLeft":3,"monthRevenue":0,"monthGoal":2870,"monthPct":0,"revenueGap":2870,"streak":1,"energyLevel":7,"doneTodayPct":0}'
```

**Erwartete Antwort:**
```json
{
  "missions": [{"rank":1,"task":"...","pillar":"Coaching","why":"...","tools":[]}],
  "daily_focus": "Umsatz-Lücke schließen...",
  "alert": null
}
```

---

## SCHRITT 2 — Task Queue importieren (Telegram Start/Skip/Done)

```
scripts/n8n_task_confirm.json
```

- Importieren → Aktivieren
- Benötigt: `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` (bereits in Env-Vars aus Schritt 0)

---

## SCHRITT 3 — Brainstorm Bots importieren (Morgen/Abend/Woche)

```
scripts/n8n_brainstorm_bots.json
```

- Importieren → Aktivieren
- Läuft automatisch per Cron (07:30, 18:00, Sonntag 19:00)
- Benötigt: `GEMINI_API_KEY` (bereits in Env-Vars)

---

## SCHRITT 4 — Voice Report (optional)

```
scripts/n8n_voice_report.json
```

- Importieren → Aktivieren
- Sprachnachricht an `@CanGo_ToDo_Master_bot` → Energie-Level wird gespeichert

---

## SCHRITT 5 — Eskalation (optional, nach den anderen)

```
scripts/n8n_escalation_workflow.json
```

---

## Fehlerbehebung

### "Jarvis antwortet nicht" / leere Response

1. **Env-Vars prüfen:** n8n → Settings → Environment Variables → alle 5 vorhanden?
2. **Workflow aktiv?** Oben rechts muss "Active" (grün) stehen, nicht "Inactive"
3. **Execution Logs prüfen:** n8n → Executions → letzte Ausführung anklicken → welcher Node ist rot?
4. **Gemini-Node rot?** → `GEMINI_API_KEY` in Env-Vars falsch/fehlt
5. **Supabase-Node rot?** → `SUPABASE_URL` / `SUPABASE_ANON_KEY` in Env-Vars prüfen

### Seite zeigt "Regel-Engine" statt "Jarvis via n8n"

→ Webhook-URL noch nicht in der Seite gespeichert:
Seite öffnen → Jarvis-Block → Webhook-URL-Feld ausfüllen → **Webhook speichern** klicken

---

## Env-Vars Übersicht (alle in n8n Settings eingetragen)

| Variable | Status |
|---------|--------|
| `GEMINI_API_KEY` | ✅ eingetragen (Schritt 0) |
| `SUPABASE_URL` | ✅ eingetragen (Schritt 0) |
| `SUPABASE_ANON_KEY` | ✅ eingetragen (Schritt 0) |
| `TELEGRAM_BOT_TOKEN` | ✅ eingetragen (Schritt 0) |
| `TELEGRAM_CHAT_ID` | ✅ eingetragen (Schritt 0) |

> **Hinweis:** Kein Anthropic-Key nötig. Jarvis v2 läuft mit Gemini 2.0 Flash (kostenlos im Free Tier).
