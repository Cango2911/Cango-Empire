---
name: goclaw
version: 1.0.0
description: GoClaw — Multi-Tenant AI Agent Platform (Go). 8-Stage Agent Pipeline, 4-Mode Prompt System, 3-Tier Memory, 20+ LLM Provider, 7 Messaging Channels (Telegram, Discord, Slack, WhatsApp, Zalo, Feishu). Single Binary, PostgreSQL, AES-256-GCM Encryption, RBAC. Built-in Skills: docx, pdf, pptx, xlsx, skill-creator.
author: nextlevelbuilder
source: https://github.com/nextlevelbuilder/goclaw
license: CC BY-NC 4.0
tags: [ai-agent, multi-tenant, go, llm, platform, gateway, postgresql, websocket, docker]
platforms: [claude-code, cursor, codex, gemini-cli, copilot, opencode, windsurf]
---

# GoClaw — Multi-Tenant AI Agent Platform

Multi-Agent AI Gateway gebaut in Go. Produktionsreif, Single Binary, ~25 MB.

## Kernfeatures

| Feature | Details |
|---------|---------|
| **8-Stage Agent Pipeline** | context → history → prompt → think → act → observe → memory → summarize |
| **4-Mode Prompt System** | Full / Task / Minimal / None mit Cache-Optimierung |
| **3-Tier Memory** | Working → Episodic (Session Summaries) → Semantic (Knowledge Graph) |
| **Knowledge Vault** | Dokument-Registry, [[wikilinks]], Hybrid Search (FTS + pgvector) |
| **Agent Teams** | Shared Task Boards, Inter-Agent Delegation (sync/async), 3 Orchestration Modes |
| **Self-Evolution** | Metrics → Suggestions → Auto-Adapt mit Guardrails |
| **Multi-Tenant PostgreSQL** | Per-User Workspaces, AES-256-GCM Encryption, RBAC |
| **20+ LLM Provider** | Anthropic, OpenAI, OpenRouter, Groq, DeepSeek, Gemini, Mistral, xAI, Claude CLI, Codex, ACP |
| **7 Messaging Channels** | Telegram, Discord, Slack, Zalo OA, Zalo Personal, Feishu/Lark, WhatsApp |
| **Observability** | Built-in LLM Tracing, optionales OpenTelemetry OTLP |

## Quick Start (Docker)

```bash
./prepare-env.sh          # .env generieren
docker compose up -d      # Starten
# Web Dashboard: http://localhost:18790
```

## Enthaltene Skills

| Skill | Beschreibung |
|-------|-------------|
| `skills/docx/` | DOCX-Verarbeitung, Track Changes, Kommentare |
| `skills/pdf/` | PDF-Formulare, Feld-Extraktion, Bounding Boxes |
| `skills/pptx/` | PowerPoint-Bearbeitung, Thumbnails, pptxgenjs |
| `skills/xlsx/` | Excel-Neuberechnung via LibreOffice |
| `skills/skill-creator/` | Eval-gesteuerte Skill-Erstellung, Benchmarking |
| `skills/_shared/office/` | Gemeinsame Office-Utilities, ISO/ECMA XSD Schemas |

## Tech Stack

- **Backend:** Go 1.26, gorilla/websocket, pgx/v5, golang-migrate
- **Web UI:** React 19, Vite 6, TypeScript, Tailwind CSS 4, Radix UI
- **Desktop:** Wails v2 (SQLite) — Single Binary ohne PostgreSQL
- **Database:** PostgreSQL 18 + pgvector / SQLite (Desktop)

## Dokumentation

Alle 30+ Architekturdokumente unter `docs/`:
- `docs/00-architecture-overview.md` — Gesamtarchitektur
- `docs/01-agent-loop.md` — 8-Stage Pipeline
- `docs/02-providers.md` — LLM Provider System
- `docs/09-security.md` — 5-Layer Security
- `docs/14-skills-runtime.md` — Skills Runtime
- `docs/23-multi-tenant-architecture.md` — Multi-Tenant System
- `api-reference.md` — HTTP API Referenz
- `websocket-protocol.md` — WebSocket RPC Protokoll
