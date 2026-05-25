---
name: skillx
version: 1.0.0
description: SkillX.sh — KI-Agent Skills Marketplace. Web-Marketplace + CLI-Tool + Hybrid Search Engine. 500+ Skills mit Leaderboard, Ratings, Semantic Search (bge-base-en-v1.5 + FTS5 + RRF). CLI: npx skillx-sh search/use/find/report/publish. Claude Code Plugin Marketplace mit skill-creator und skillx Plugins.
author: nextlevelbuilder
source: https://github.com/nextlevelbuilder/skillx
license: MIT
tags: [skills, marketplace, cli, search, hybrid-search, claude-code, ai-agent, cloudflare]
platforms: [claude-code, cursor, codex, gemini-cli, copilot, opencode, windsurf]
---

# SkillX.sh — AI Agent Skills Marketplace

> *"The Only Skill That Your AI Agent Needs."*

Kombiniert Web-Marketplace, CLI-Tool und Hybrid Search Engine für KI-Agent Skills.

## CLI Nutzung

```bash
# Installieren
npm install -g skillx-sh

# Skills suchen
npx skillx search "data processing"
npx skillx find "code review"       # interaktive Suche

# Skill verwenden
npx skillx use skill-creator
npx skillx use "email validation" --search   # suchen + verwenden

# Mehrere Skills gleichzeitig
npx skillx use skill1 skill2 skill3

# Ergebnis melden
npx skillx report --outcome success --duration 1234

# API-Key konfigurieren
npx skillx config set SKILLX_API_KEY sk_prod_...

# Skill veröffentlichen
npx skillx publish
```

## Enthaltene Claude Code Plugins

### skill-creator (v3.0.0)
Eval-gesteuerte Skill-Erstellung optimiert für Skillmark-Benchmarks.

```bash
/plugin install skill-creator@skillx-marketplace
```

### skillx (v1.0.0)
Marketplace-Integration: Skills direkt aus dem Agent suchen und verwenden.

```bash
/plugin marketplace add nextlevelbuilder/skillx
/plugin install skillx@skillx-marketplace
```

## Architektur

| Komponente | Technologie |
|------------|-------------|
| **Web** | React Router v7 + Cloudflare Workers + SSR |
| **Datenbank** | Cloudflare D1 (SQLite) + Drizzle ORM |
| **Search** | FTS5 + Vectorize (bge-base-en-v1.5, 768-dim) + RRF Fusion |
| **Auth** | Better Auth + GitHub OAuth |
| **Cache** | Cloudflare KV (5min TTL) |
| **Storage** | R2 (Assets), Workers AI (Embeddings) |
| **CLI** | Commander.js + chalk + ora + conf (`skillx-sh`) |

## Leaderboard & Scoring

Composite Scoring Algorithm:
- **Install Score** — Installationsanzahl (log-normalisiert)
- **Quality Score** — Ratings + Reviews + Favoriten
- **Signal Score** — Aktualität + GitHub-Stars + Boost

## Hybrid Search

```
Query → FTS5 Keyword Search → Reciprocal Rank Fusion (RRF)
     → Vectorize Semantic Search (768-dim) ↗
     → Boost Scoring (favorites, recency, stars)
```

Latenz: <800ms p95

## Skill Creator References

17 Referenz-Dokumente unter `.claude/skills/skill-creator/references/`:
- `skill-anatomy-and-requirements.md` — Skill-Struktur
- `eval-infrastructure-guide.md` — Eval-System
- `benchmark-optimization-guide.md` — Benchmark-Optimierung
- `plugin-marketplace-overview.md` — Marketplace
- `yaml-frontmatter-reference.md` — YAML-Metadaten
- `writing-effective-instructions.md` — Best Practices
- und 11 weitere
