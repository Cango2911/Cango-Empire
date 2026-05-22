# n8n Setup Guide — CanGo Jarvis System

**Ziel:** 5 Workflows importieren → aktivieren → Jarvis denkt wirklich

---

## 0. Voraussetzungen

- n8n läuft (Hostinger VPS oder n8n Cloud)
- Alle Env-Vars aus `docs/n8n/n8n-env-vars.env` eingetragen
- Supabase Tabellen existieren (bereits erledigt: `kekmslytyttcipanwdop`)

---

## 1. Anthropic API Key holen (5 Minuten)

1. `console.anthropic.com` → API Keys → **+ Create Key**
2. Name: `cango-jarvis`
3. Key kopieren → in n8n: Settings → Environment Variables:
   ```
   ANTHROPIC_API_KEY = sk-ant-...
   ```

---

## 2. Workflows importieren (Reihenfolge wichtig)

### Workflow 1 — Jarvis Analyzer (Pflicht)
```
scripts/n8n_jarvis_analyzer.json
```
- In n8n: **New Workflow → Import from JSON**
- Nach Import: **Activate** (oben rechts)
- Webhook-URL kopieren (Production URL):
  ```
  https://DEINE-N8N-DOMAIN/webhook/jarvis-analyze
  ```
- Diese URL in `website/intern/daily-todo-master.html` im Jarvis-Block eintragen:
  - Seite öffnen → Jarvis-Block ganz oben → Webhook-URL-Feld → eintragen → **Webhook speichern**

### Workflow 2 — Task Queue (Telegram Start/Skip/Done)
```
scripts/n8n_task_confirm.json
```
- Importieren → Aktivieren
- Callback-Trigger URL nicht ändern (ist intern)

### Workflow 3 — Brainstorm Bots (Morgen/Abend/Woche)
```
scripts/n8n_brainstorm_bots.json
```
- Importieren → Aktivieren
- Läuft automatisch per Cron (07:30, 18:00, Sonntag 19:00)

### Workflow 4 — Voice Report (Whisper → Energie)
```
scripts/n8n_voice_report.json
```
- Importieren → Aktivieren
- Sprachnachricht an `@CanGo_ToDo_Master_bot` → Whisper transkribiert → energyLevel gespeichert

### Workflow 5 — Eskalation (Block-Timer)
```
scripts/n8n_escalation_workflow.json
```
- Importieren → Aktivieren (optional, nach den anderen)

---

## 3. n8n Credentials einrichten

In n8n → **Credentials** → folgende anlegen:

| Credential | Typ | Wert |
|-----------|-----|------|
| Anthropic | Anthropic API | `ANTHROPIC_API_KEY` |
| Supabase | HTTP Header Auth | URL + Anon Key |
| Telegram Bot | Telegram Bot API | `TELEGRAM_BOT_TOKEN` |

---

## 4. Testen

```
# 1. Jarvis Analyzer manuell triggern:
curl -X POST https://DEINE-N8N-DOMAIN/webhook/jarvis-analyze \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-05-22","monthRevenue":0,"monthGoal":2870,"energyLevel":7}'

# 2. Erwartete Antwort:
{
  "missions": [{"rank":1,"task":"...","pillar":"...","why":"..."}],
  "daily_focus": "...",
  "alert": null
}
```

---

## 5. In der Seite aktivieren

1. `https://automation-cango-app-empire.com/intern/daily-todo-master.html` öffnen
2. Jarvis-Block → Webhook-URL eintragen → **Webhook speichern**
3. Seite neu laden → Status sollte wechseln von `Regel-Engine` auf `Jarvis via n8n/Claude`

---

## Env-Vars Übersicht (alles was n8n braucht)

| Variable | Wert | Status |
|---------|------|--------|
| `SUPABASE_URL` | `https://kekmslytyttcipanwdop.supabase.co` | ✅ |
| `SUPABASE_ANON_KEY` | `eyJhbGci...` | ✅ |
| `TELEGRAM_BOT_TOKEN` | `8964673248:AAH...` | ✅ |
| `TELEGRAM_CHAT_ID` | Deine Chat-ID | ⬜ noch offen |
| `ANTHROPIC_API_KEY` | `sk-ant-...` | ⬜ noch offen |
| `GEMINI_API_KEY` | `AIzaSyA-...` | ✅ |
