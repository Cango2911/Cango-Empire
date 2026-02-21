# 🚀 CanGo Empire - n8n + Claude Code Superkraft

## 📋 Übersicht

Komplette Enterprise-Automatisierung mit:
- **n8n** (RepoCloud) als Orchestrator
- **Claude Code** als Super-Agent auf Hostinger VPS
- **Twingate** Zero Trust Security
- **Slack** für Approvals & Notifications

---

## 🖥️ Dein VPS

- **Hostname:** `srv1105698.hstgr.cloud`
- **IP:** `31.97.56.197`
- **OS:** Ubuntu 24.04
- **SSH:** `ssh root@31.97.56.197`

---

## 📚 Dokumentation

### Haupt-Anleitung
- **`superkraft-setup-guide.md`** - Komplette Highend-Anleitung (Deutsch)

### VPS-Setup
- **`HOSTINGER_VPS_KONFIGURATION.md`** - Detaillierte VPS-Konfiguration
- **`QUICK_START_VPS.md`** - Schnellstart in 5 Minuten

### Integrationen
- **`SLACK_SETUP_ANLEITUNG.md`** - Slack Integration Setup
- **`CLAUDE_CODE_INSTALLATION_HOSTINGER.md`** - Claude Code Installation

### Workflows
Alle n8n Workflows befinden sich in `/workflows/`:
- `n8n_Claude_Code_Executor.json` - Haupt-Subworkflow
- `n8n_Session_Manager.json` - Session-Verwaltung
- `n8n_Health_Check_Monitor.json` - System-Überwachung
- `n8n_Approval_Handler.json` - Telegram Approvals
- `n8n_Slack_Approval_Handler.json` - Slack Approvals
- `n8n_Slack_Notifications.json` - Slack Notifications
- `n8n_Website_Monitor.json` - Website-Monitoring

### Docker
- `docker/docker-compose-claude-code.yml` - Claude Code Container
- `docker/docker-compose-n8n.yml` - n8n Container (optional)

### Scripts
- `scripts/setup-claude-code.sh` - Automatische Claude Code Installation

---

## 🚀 Quick Start

### 1. VPS vorbereiten

```bash
ssh root@31.97.56.197
```

Siehe: `QUICK_START_VPS.md`

### 2. n8n Workflows importieren

1. Öffne RepoCloud n8n
2. Importiere alle Workflows aus `/workflows/`
3. Konfiguriere SSH Credentials:
   - Host: `srv1105698.hstgr.cloud`
   - Port: `22`
   - Username: `root`

### 3. Slack einrichten

Siehe: `SLACK_SETUP_ANLEITUNG.md`

---

## 📁 Dateistruktur

```
OnlineAgentur CanGo/
├── workflows/                    # n8n Workflow JSON-Dateien
│   ├── n8n_Claude_Code_Executor.json
│   ├── n8n_Session_Manager.json
│   ├── n8n_Health_Check_Monitor.json
│   ├── n8n_Slack_Approval_Handler.json
│   └── ...
├── docker/                      # Docker Compose Dateien
│   ├── docker-compose-claude-code.yml
│   └── docker-compose-n8n.yml
├── scripts/                     # Helper-Scripts
│   └── setup-claude-code.sh
├── claude-skills/               # Claude Code Skills
│   ├── marketing-skill.md
│   ├── unifi-skill.md
│   └── api-skill.md
├── superkraft-setup-guide.md    # Haupt-Anleitung
├── HOSTINGER_VPS_KONFIGURATION.md
├── QUICK_START_VPS.md
├── SLACK_SETUP_ANLEITUNG.md
└── README.md                    # Diese Datei
```

---

## ✅ Checkliste

### VPS Setup
- [ ] SSH-Verbindung funktioniert
- [ ] Docker installiert
- [ ] Verzeichnisstruktur erstellt
- [ ] Claude Code Container läuft
- [ ] Claude Code installiert

### n8n Setup
- [ ] RepoCloud n8n erreichbar
- [ ] Workflows importiert
- [ ] SSH Credentials konfiguriert
- [ ] Test-Workflow erfolgreich

### Integrationen
- [ ] Slack App erstellt
- [ ] Slack Credentials in n8n
- [ ] Telegram Bot (optional)
- [ ] Twingate (optional)

---

## 🆘 Support

Bei Problemen:
1. Prüfe die entsprechenden Anleitungen
2. Siehe Troubleshooting-Sektionen
3. Prüfe n8n Execution Logs
4. Prüfe Docker Container Logs

---

*CanGo Empire Automation System | Version 2.0 | 2025-01-27T16:28:00Z*

