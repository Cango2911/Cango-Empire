---
name: awesome-codex-subagents
version: 1.0.0
description: "Awesome Codex Subagents — 136 spezialisierte OpenAI-Codex-Subagenten in 10 Kategorien (VoltAgent, MIT). TOML-Format (name/description/model/model_reasoning_effort/sandbox_mode/developer_instructions). Smart Model Routing: gpt-5.4 (Architektur/Security) vs. gpt-5.3-codex-spark (Suche/Docs). Sandbox-Modi: read-only (Reviewer) oder workspace-write (Developer). Explizite Delegation erforderlich — kein Auto-Spawn. Installation: ~/.codex/agents/ (global) oder .codex/agents/ (Projekt)."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-codex-subagents
license: MIT
type: agent-skill
tags:
  - codex
  - openai
  - subagents
  - agents
  - ai-agents
  - developer-tools
  - orchestration
  - gpt-5
---

# Awesome Codex Subagents

## Was sind Codex Subagents?

Subagents sind spezialisierte AI-Assistenten für OpenAI Codex, definiert als `.toml`-Dateien. Im Unterschied zu Claude Code Subagents (Markdown + YAML-Frontmatter) verwendet Codex ein natives TOML-Format. **Wichtig: Codex spawnt Subagents NICHT automatisch** — explizite Delegation im Prompt ist erforderlich.

**Vorteile:**
- **Isolierter Kontext** — Jeder Subagent hat ein eigenes Context Window
- **Domänen-Expertise** — Spezialisierte `developer_instructions` für jede Aufgabe
- **Smart Model Routing** — gpt-5.4 für tiefes Reasoning, gpt-5.3-codex-spark für schnelle Tasks
- **Sandbox-Kontrolle** — `read-only` für Reviewer/Auditoren, `workspace-write` für Developer

## Subagent-Dateiformat (TOML)

```toml
name = "subagent-name"
description = "When this agent should be invoked"
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Du bist ein [Rolle] mit Expertise in [Bereich]...

Working mode:
1. Schritt 1
2. Schritt 2

Focus on:
- Punkt 1
- Punkt 2
"""
```

### Speicherorte

| Typ | Pfad | Verfügbarkeit | Priorität |
|-----|------|---------------|-----------|
| Projekt-Subagenten | `.codex/agents/` | Nur aktuelles Projekt | Höher |
| Globale Subagenten | `~/.codex/agents/` | Alle Projekte | Niedriger |

## Smart Model Routing

| Modell | Wann | Beispiele |
|--------|------|-----------|
| `gpt-5.4` | Tiefes Reasoning — Architektur, Security-Audits, Finanzlogik | `security-auditor`, `architect-reviewer`, `fintech-engineer` |
| `gpt-5.3-codex-spark` | Schnelles Scannen, Synthese, leichtere Tasks | `search-specialist`, `docs-researcher`, `agent-installer` |

## Sandbox-Philosophie

| Modus | Wann | Beispiele |
|-------|------|---------|
| `read-only` | Reviewer, Auditoren — analysieren ohne zu modifizieren | `code-reviewer`, `security-auditor`, `architect-reviewer` |
| `workspace-write` | Developer, Engineers — Dateien erstellen und ändern | `python-pro`, `backend-developer`, `devops-engineer` |

## Installation

```bash
# Global (alle Projekte)
mkdir -p ~/.codex/agents
cp categories/01-core-development/backend-developer.toml ~/.codex/agents/

# Projekt-spezifisch
mkdir -p .codex/agents
cp categories/04-quality-security/reviewer.toml .codex/agents/
```

## Explizite Delegation (Beispiele)

```text
# PR-Review Workflow
Review this branch with parallel subagents. Have reviewer look for
correctness, security, and missing tests. Have docs_researcher verify
the framework APIs. Wait for both and summarize with file references.

# Bug-Investigation Workflow
Investigate the broken settings flow. Have code_mapper trace the owning
code paths, browser_debugger reproduce the bug, and frontend_developer
propose the smallest fix. Wait for read-heavy agents first.

# Repo-Exploration Workflow
Use search_specialist to locate payment retry code, knowledge_synthesizer
to summarize the current design, and refactoring_specialist to propose a
minimal refactor plan. Return a concrete action list.
```

---

## 10 Kategorien — vollständige Subagent-Liste

### 01. Core Development (12 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `api-designer` | REST und GraphQL API Vertragsdesign, Evolution, Kompatibilität |
| `backend-developer` | Server-seitige APIs, Datenbankgrenzen, Skalierung |
| `code-mapper` | Codebase-Erkundung, Ownership-Mapping, Abhängigkeitsverfolgung |
| `electron-pro` | Desktop-App-Entwicklung mit Electron |
| `frontend-developer` | UI/UX-Spezialist für React, Vue, Angular |
| `fullstack-developer` | End-to-End Feature-Entwicklung (DB + API + Frontend) |
| `graphql-architect` | GraphQL Schema und Federation-Experte |
| `microservices-architect` | Distributed Systems Designer |
| `mobile-developer` | Cross-Platform Mobile-Spezialist |
| `ui-designer` | Visual Design und Interaction-Spezialist |
| `ui-fixer` | UI-Bugs, Rendering-Probleme, Layout-Korrekturen |
| `websocket-engineer` | Echtzeit-Kommunikations-Spezialist |

### 02. Language Specialists (27 Agents)

| Subagent | Sprache/Framework |
|----------|------------------|
| `angular-architect` | Angular |
| `cpp-pro` | C++ |
| `csharp-developer` | C# |
| `django-developer` | Django/Python |
| `dotnet-core-expert` | .NET Core |
| `dotnet-framework-4.8-expert` | .NET Framework 4.8 |
| `elixir-expert` | Elixir |
| `erlang-expert` | Erlang |
| `flutter-expert` | Flutter/Dart |
| `golang-pro` | Go |
| `java-architect` | Java |
| `javascript-pro` | JavaScript |
| `kotlin-specialist` | Kotlin |
| `laravel-specialist` | Laravel/PHP |
| `nextjs-developer` | Next.js |
| `php-pro` | PHP |
| `powershell-5.1-expert` | PowerShell 5.1 |
| `powershell-7-expert` | PowerShell 7 |
| `python-pro` | Python |
| `rails-expert` | Ruby on Rails |
| `react-specialist` | React |
| `rust-engineer` | Rust |
| `spring-boot-engineer` | Spring Boot/Java |
| `sql-pro` | SQL |
| `swift-expert` | Swift/iOS |
| `typescript-pro` | TypeScript |
| `vue-expert` | Vue.js |

### 03. Infrastructure (16 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `azure-infra-engineer` | Azure Cloud Infrastruktur |
| `cloud-architect` | Multi-Cloud Architektur |
| `database-administrator` | Datenbank-Administration |
| `deployment-engineer` | CI/CD und Deployment-Pipelines |
| `devops-engineer` | DevOps Best Practices |
| `devops-incident-responder` | Incident Response für DevOps |
| `docker-expert` | Container und Docker |
| `incident-responder` | Allgemeiner Incident Responder |
| `kubernetes-specialist` | Kubernetes und Container-Orchestrierung |
| `network-engineer` | Netzwerk-Infrastruktur |
| `platform-engineer` | Platform Engineering |
| `security-engineer` | Security Engineering |
| `sre-engineer` | Site Reliability Engineering |
| `terraform-engineer` | Terraform IaC |
| `terragrunt-expert` | Terragrunt und DRY-IaC-Orchestrierung |
| `windows-infra-admin` | Active Directory, DNS, DHCP, GPO |

### 04. Quality & Security (16 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `accessibility-tester` | WCAG-Compliance und Barrierefreiheits-Tests |
| `ad-security-reviewer` | Active Directory Security und GPO-Audit |
| `architect-reviewer` | Architektur-Reviews |
| `browser-debugger` | Browser-Reproduktion und Client-seitiges Debugging |
| `chaos-engineer` | Chaos Engineering und Resilienztests |
| `code-reviewer` | Code-Qualitäts-Guardian |
| `compliance-auditor` | Regulatorische Compliance-Prüfungen |
| `debugger` | Erweitertes Debugging |
| `error-detective` | Fehleranalyse und Root-Cause |
| `penetration-tester` | Ethical Hacking |
| `performance-engineer` | Performance-Optimierung |
| `powershell-security-hardening` | PowerShell Security Hardening |
| `qa-expert` | Test-Automatisierungs-Spezialist |
| `reviewer` | PR-Review für Korrektheit, Security, Regressionen |
| `security-auditor` | Sicherheitslücken-Experte |
| `test-automator` | Test-Framework-Spezialist |

### 05. Data & AI (12 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `ai-engineer` | AI-System-Design und -Deployment |
| `data-analyst` | Datenanalyse und Visualisierung |
| `data-engineer` | Datenpipeline-Architekt |
| `data-scientist` | Analyse und Insights |
| `database-optimizer` | Datenbank-Performance-Spezialist |
| `llm-architect` | LLM-Workflow-Architekt (Prompts, Tools, Retrieval, Evaluation) |
| `machine-learning-engineer` | ML-Systeme |
| `ml-engineer` | Machine Learning-Spezialist |
| `mlops-engineer` | MLOps und Modell-Deployment |
| `nlp-engineer` | Natural Language Processing |
| `postgres-pro` | PostgreSQL-Experte |
| `prompt-engineer` | Prompt-Optimierung und Instruction Design |

### 06. Developer Experience (13 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `build-engineer` | Build-Systeme und Toolchains |
| `cli-developer` | CLI-Tools und Kommandozeilen-Apps |
| `dependency-manager` | Package und Dependency Management |
| `documentation-engineer` | Technische Dokumentation |
| `dx-optimizer` | Developer Experience Optimierung |
| `git-workflow-manager` | Git-Workflows und Branching |
| `legacy-modernizer` | Legacy-Code-Modernisierung |
| `mcp-developer` | Model Context Protocol Spezialist |
| `powershell-module-architect` | PowerShell Module und Profile-Architektur |
| `powershell-ui-architect` | PowerShell UI (WinForms, WPF, Metro, TUI) |
| `refactoring-specialist` | Code-Refactoring |
| `slack-expert` | Slack-Platform und @slack/bolt |
| `tooling-engineer` | Developer-Tooling |

### 07. Specialized Domains (12 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `api-documenter` | API-Dokumentations-Spezialist |
| `blockchain-developer` | Web3, Crypto und Smart Contracts |
| `embedded-systems` | Embedded und Real-time Systems |
| `fintech-engineer` | Fintech und Banking-Systeme |
| `game-developer` | Game Development |
| `iot-engineer` | IoT-Systeme |
| `m365-admin` | Microsoft 365, Exchange Online, Teams, SharePoint |
| `mobile-app-developer` | Mobile App Entwicklung |
| `payment-integration` | Payment-Systeme (Stripe etc.) |
| `quant-analyst` | Quantitative Analyse |
| `risk-manager` | Risikobewertung und -management |
| `seo-specialist` | Search Engine Optimization |

### 08. Business & Product (11 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `business-analyst` | Anforderungs-Spezialist |
| `content-marketer` | Content Marketing |
| `customer-success-manager` | Customer Success |
| `legal-advisor` | Recht und Compliance |
| `product-manager` | Product Strategy |
| `project-manager` | Projektmanagement |
| `sales-engineer` | Technischer Vertrieb |
| `scrum-master` | Agile / Scrum |
| `technical-writer` | Technisches Schreiben |
| `ux-researcher` | User Research |
| `wordpress-master` | WordPress-Entwicklung und -Optimierung |

### 09. Meta & Orchestration (10 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `agent-installer` | Subagents aus GitHub installieren |
| `agent-organizer` | Multi-Agent-Koordination |
| `context-manager` | Kontext-Optimierung |
| `error-coordinator` | Fehlerbehandlung und Recovery |
| `it-ops-orchestrator` | IT-Operations-Workflow-Orchestrierung |
| `knowledge-synthesizer` | Wissens-Aggregation |
| `multi-agent-coordinator` | Erweiterte Multi-Agent-Orchestrierung |
| `performance-monitor` | Agent-Performance-Optimierung |
| `task-distributor` | Task-Verteilung |
| `workflow-orchestrator` | Komplexe Workflow-Automatisierung |

### 10. Research & Analysis (7 Agents)

| Subagent | Beschreibung |
|----------|-------------|
| `competitive-analyst` | Wettbewerbs-Intelligence |
| `data-researcher` | Daten-Entdeckung und -Analyse |
| `docs-researcher` | Dokumentations-basierte API- und Framework-Verifikation |
| `market-researcher` | Marktanalyse und Consumer Insights |
| `research-analyst` | Umfassende Recherche |
| `search-specialist` | Erweiterte Informations-Recherche |
| `trend-analyst` | Trend-Erkennung und Prognosen |

---

## Unterschied zu Claude Code Subagents

| Merkmal | Codex Subagents | Claude Code Subagents |
|---------|----------------|----------------------|
| Format | `.toml` | `.md` mit YAML-Frontmatter |
| Pfad | `.codex/agents/` | `.claude/agents/` |
| Modell-Feld | `model = "gpt-5.4"` | `model: sonnet` |
| Auto-Spawn | ❌ Nein (explizit) | ✅ Ja (automatisch) |
| Sandbox | `sandbox_mode` | `tools:` |
| Hersteller | OpenAI Codex | Anthropic Claude Code |

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-codex-subagents
- VoltAgent: https://github.com/VoltAgent/voltagent
- OpenAI Codex Subagents Docs: https://developers.openai.com/codex/subagents
- Discord: https://s.voltagent.dev/discord
