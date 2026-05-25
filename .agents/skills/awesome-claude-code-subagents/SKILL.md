---
name: awesome-claude-code-subagents
version: 1.0.0
description: "Awesome Claude Code Subagents — Kuratierte Sammlung von 131+ Claude Code Subagenten in 10 Kategorien (VoltAgent, MIT). Jeder Subagent hat YAML-Frontmatter (name, description, tools, model) + spezialisiertes System-Prompt. Kategorien: Core Development, Language Specialists (30+ Sprachen/Frameworks), Infrastructure/DevOps, Quality/Security, Data/AI, Developer Experience, Specialized Domains, Business/Product, Meta/Orchestration, Research/Analysis. Installation: ~/.claude/agents/ (global) oder .claude/agents/ (projekt-spezifisch)."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-claude-code-subagents
license: MIT
type: agent-skill
tags:
  - claude-code
  - subagents
  - agents
  - ai-agents
  - developer-tools
  - orchestration
  - automation
---

# Awesome Claude Code Subagents

## Was sind Claude Code Subagents?

Subagents sind spezialisierte AI-Assistenten für Claude Code, die als eigene Markdown-Dateien definiert werden. Claude Code wählt automatisch den passenden Subagenten, wenn eine Aufgabe dessen Expertise entspricht.

**Vorteile:**
- **Isolierter Kontext** — Jeder Subagent hat ein eigenes Context Window, kein Cross-Contamination
- **Domänen-Expertise** — Maßgeschneiderte Prompts für spezifische Aufgaben
- **Smart Model Routing** — Automatische Zuweisung von opus/sonnet/haiku
- **Granulare Tool-Rechte** — Jeder Agent hat nur die Berechtigungen, die er braucht

## Installation

### Methode 1: Einzelne Dateien kopieren

```bash
# Global (alle Projekte)
cp categories/02-language-specialists/python-pro.md ~/.claude/agents/

# Projekt-spezifisch
cp categories/02-language-specialists/python-pro.md .claude/agents/
```

### Methode 2: Interaktiver Installer

```bash
./install-agents.sh
```

Menü-geführte Auswahl nach Kategorie — installieren und deinstallieren.

### Methode 3: Claude Code Plugin

```bash
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang    # Language Specialists
claude plugin install voltagent-infra   # Infrastructure & DevOps
```

### Methode 4: subagent-catalog Slash Commands

```bash
# Installieren:
cp -r tools/subagent-catalog ~/.claude/commands/

# Dann in Claude Code:
/subagent-catalog:search python
/subagent-catalog:fetch python-pro
/subagent-catalog:list
/subagent-catalog:invalidate    # Cache leeren
```

## Subagent-Dateiformat

```yaml
---
name: subagent-name
description: "Wann dieser Agent aufgerufen werden soll (trigger text)"
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

Du bist ein Senior-[Rolle] mit Expertise in [Bereich]...

Wenn aufgerufen:
1. Schritt 1
2. Schritt 2

Checkliste:
- Punkt 1
- Punkt 2

## Communication Protocol
Inter-Agent-Kommunikation...
```

### Speicherorte

| Typ | Pfad | Verfügbarkeit | Priorität |
|-----|------|---------------|-----------|
| Projekt-Subagenten | `.claude/agents/` | Nur aktuelles Projekt | Höher |
| Globale Subagenten | `~/.claude/agents/` | Alle Projekte | Niedriger |

## Smart Model Routing

| Modell | Wann | Beispiele |
|--------|------|-----------|
| `opus` | Tiefes Reasoning — Architektur, Security-Audits, Finanzlogik | `security-auditor`, `architect-reviewer`, `fintech-engineer` |
| `sonnet` | Alltägliches Coding — Schreiben, Debuggen, Refactoring | `python-pro`, `backend-developer`, `devops-engineer` |
| `haiku` | Schnelle Aufgaben — Docs, Suche, Dependency-Checks | `documentation-engineer`, `seo-specialist`, `build-engineer` |

Überschreiben: `model: inherit` → nutzt Modell der Hauptkonversation.

## Tool-Philosophie

| Typ | Tools | Beispiele |
|-----|-------|-----------|
| Read-only (Reviewer, Auditor) | `Read, Grep, Glob` | `code-reviewer`, `security-auditor` |
| Research | `Read, Grep, Glob, WebFetch, WebSearch` | `research-analyst`, `market-researcher` |
| Code Writer | `Read, Write, Edit, Bash, Glob, Grep` | `python-pro`, `backend-developer` |
| Documentation | `Read, Write, Edit, Glob, Grep, WebFetch, WebSearch` | `documentation-engineer`, `technical-writer` |

---

## 10 Kategorien — vollständige Subagent-Liste

### 01. Core Development — Plugin: `voltagent-core-dev`

| Subagent | Beschreibung |
|----------|-------------|
| `api-designer` | REST und GraphQL API-Architekt |
| `backend-developer` | Server-seitiger Experte für skalierbare APIs |
| `design-bridge` | Design-zu-Code-Übersetzer |
| `electron-pro` | Desktop Application Experte |
| `frontend-developer` | UI/UX-Spezialist für React, Vue, Angular |
| `fullstack-developer` | End-to-End Feature-Entwicklung (DB + API + Frontend) |
| `graphql-architect` | GraphQL Schema und Federation-Experte |
| `microservices-architect` | Distributed Systems Designer |
| `mobile-developer` | Cross-Platform Mobile-Spezialist |
| `ui-designer` | Visual Design und Interaction-Spezialist |
| `websocket-engineer` | Echtzeit-Kommunikations-Spezialist |

### 02. Language Specialists — Plugin: `voltagent-lang`

| Subagent | Sprache/Framework |
|----------|------------------|
| `angular-architect` | Angular |
| `cpp-pro` | C++ |
| `csharp-developer` | C# |
| `django-developer` | Django/Python |
| `dotnet-core-expert` | .NET Core |
| `dotnet-framework-4.8-expert` | .NET Framework 4.8 |
| `elixir-expert` | Elixir |
| `expo-react-native-expert` | Expo/React Native |
| `fastapi-developer` | FastAPI/Python |
| `flutter-expert` | Flutter/Dart |
| `golang-pro` | Go |
| `java-architect` | Java |
| `javascript-pro` | JavaScript |
| `kotlin-specialist` | Kotlin |
| `laravel-specialist` | Laravel/PHP |
| `nextjs-developer` | Next.js |
| `node-specialist` | Node.js |
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
| `symfony-specialist` | Symfony/PHP |
| `typescript-pro` | TypeScript |
| `vue-expert` | Vue.js |

### 03. Infrastructure — Plugin: `voltagent-infra`

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
| `terragrunt-expert` | Terragrunt |
| `windows-infra-admin` | Windows Infrastructure |

### 04. Quality & Security — Plugin: `voltagent-qa`

| Subagent | Beschreibung |
|----------|-------------|
| `accessibility-tester` | Barrierefreiheits-Tests (WCAG) |
| `ad-security-reviewer` | Active Directory Security |
| `ai-writing-auditor` | AI-generierten Text erkennen und verbessern |
| `architect-reviewer` | Architektur-Reviews (opus) |
| `chaos-engineer` | Chaos Engineering und Resilienztests |
| `code-reviewer` | Code-Review-Spezialist |
| `compliance-auditor` | Compliance-Prüfungen |
| `debugger` | Debugging-Experte |
| `error-detective` | Fehleranalyse und Root-Cause |
| `penetration-tester` | Penetration Testing |
| `performance-engineer` | Performance-Optimierung |
| `powershell-security-hardening` | PowerShell Security Hardening |
| `qa-expert` | Quality Assurance |
| `security-auditor` | Sicherheits-Audits (opus) |
| `test-automator` | Test-Automatisierung |
| `ui-ux-tester` | UI/UX Testing |

### 05. Data & AI — Plugin: `voltagent-data`

| Subagent | Beschreibung |
|----------|-------------|
| `ai-engineer` | AI System Engineering |
| `data-analyst` | Datenanalyse und Insights |
| `data-engineer` | Datenpipelines und ETL |
| `data-scientist` | Data Science und Statistik |
| `database-optimizer` | Datenbank-Optimierung |
| `llm-architect` | LLM-System-Architekt |
| `machine-learning-engineer` | ML Engineering |
| `ml-engineer` | Alternative ML-Engineering-Rolle |
| `mlops-engineer` | MLOps und ML-Deployment |
| `nlp-engineer` | Natural Language Processing |
| `postgres-pro` | PostgreSQL-Spezialist |
| `prompt-engineer` | Prompt Engineering |
| `reinforcement-learning-engineer` | Reinforcement Learning |

### 06. Developer Experience — Plugin: `voltagent-dx`

| Subagent | Beschreibung |
|----------|-------------|
| `build-engineer` | Build-Systeme und Toolchains |
| `cli-developer` | CLI-Tools und Kommandozeilen-Apps |
| `dependency-manager` | Dependency Management |
| `documentation-engineer` | Technische Dokumentation |
| `dx-optimizer` | Developer Experience Optimierung |
| `git-workflow-manager` | Git-Workflows und Branching |
| `legacy-modernizer` | Legacy-Code-Modernisierung |
| `mcp-developer` | MCP Server-Entwicklung |
| `powershell-module-architect` | PowerShell Module-Architektur |
| `powershell-ui-architect` | PowerShell UI-Entwicklung |
| `readme-generator` | README und Dokumentationsgenerierung |
| `refactoring-specialist` | Code-Refactoring |
| `slack-expert` | Slack-Integration und Bots |
| `tooling-engineer` | Developer-Tooling |

### 07. Specialized Domains — Plugin: `voltagent-domain`

| Subagent | Beschreibung |
|----------|-------------|
| `api-documenter` | API-Dokumentation |
| `blockchain-developer` | Blockchain und Smart Contracts |
| `embedded-systems` | Embedded Systems und Firmware |
| `fintech-engineer` | Fintech und Banking-Systeme (opus) |
| `game-developer` | Game Development |
| `healthcare-admin` | Healthcare IT und HIPAA |
| `iot-engineer` | IoT-Systeme |
| `m365-admin` | Microsoft 365 Administration |
| `mobile-app-developer` | Mobile App Entwicklung |
| `payment-integration` | Payment-Systeme (Stripe, etc.) |
| `quant-analyst` | Quantitative Analyse |
| `risk-manager` | Risikomanagement |
| `seo-specialist` | Search Engine Optimization |

### 08. Business & Product — Plugin: `voltagent-biz`

| Subagent | Beschreibung |
|----------|-------------|
| `business-analyst` | Business-Anforderungen und -Analyse |
| `content-marketer` | Content Marketing |
| `customer-success-manager` | Customer Success |
| `legal-advisor` | Rechtliche Beratung und Compliance |
| `license-engineer` | Software-Lizenzierung |
| `product-manager` | Product Management |
| `project-manager` | Projektmanagement |
| `sales-engineer` | Technischer Vertrieb |
| `scrum-master` | Agile / Scrum |
| `technical-writer` | Technisches Schreiben |
| `ux-researcher` | UX Research |
| `wordpress-master` | WordPress-Entwicklung |

### 09. Meta & Orchestration — Plugin: `voltagent-meta`

| Subagent | Beschreibung |
|----------|-------------|
| `agent-installer` | Subagents aus diesem Repo via GitHub installieren |
| `agent-organizer` | Multi-Agent-Koordination |
| `codebase-orchestrator` | Sicheres Refactoring-Governance |
| `context-manager` | Kontext-Optimierung |
| `error-coordinator` | Fehlerbehandlung und Recovery |
| `it-ops-orchestrator` | IT-Operations-Workflow-Orchestrierung |
| `knowledge-synthesizer` | Wissens-Aggregation |
| `multi-agent-coordinator` | Erweiterte Multi-Agent-Orchestrierung (opus) |
| `performance-monitor` | Agent-Performance-Optimierung |
| `task-distributor` | Task-Verteilung |
| `workflow-orchestrator` | Komplexe Workflow-Automatisierung |

### 10. Research & Analysis — Plugin: `voltagent-research`

| Subagent | Beschreibung |
|----------|-------------|
| `competitive-analyst` | Wettbewerbs-Intelligence |
| `data-researcher` | Daten-Recherche und -Analyse |
| `market-researcher` | Marktanalyse und Consumer Insights |
| `project-idea-validator` | Projekt-Ideen-Validierung (Go/No-Go) |
| `research-analyst` | Umfassende Recherche |
| `scientific-literature-researcher` | Wissenschaftliche Paper-Suche |
| `search-specialist` | Erweiterte Informations-Recherche |
| `trend-analyst` | Trend-Erkennung und Prognosen |

---

## subagent-catalog — Slash Commands

Nach Installation (`cp -r tools/subagent-catalog ~/.claude/commands/`):

```
/subagent-catalog:search <query>    # Subagenten nach Name/Beschreibung suchen
/subagent-catalog:fetch <name>      # Vollständige Subagent-Definition abrufen
/subagent-catalog:list              # Alle Kategorien durchsuchen
/subagent-catalog:invalidate        # Cache invalidieren (mit --fetch für Sofort-Refresh)
```

Cache-Verhalten: 12 Stunden TTL, gespeichert in `~/.claude/cache/subagent-catalog.md`.

## Eigene Subagents erstellen

```bash
# In Claude Code:
/agents
```

1. Projekt-spezifisch oder global wählen
2. Claude eine Initialversion generieren lassen, dann verfeinern
3. Detaillierte Trigger-Description schreiben (wann wird er aktiviert?)
4. Tool-Zugriff konfigurieren (leer = alle Tools)
5. System-Prompt im integrierten Editor anpassen (`e`)

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-claude-code-subagents
- VoltAgent: https://github.com/VoltAgent/voltagent
- Claude Code Subagents Docs: https://docs.anthropic.com/en/docs/claude-code/sub-agents
- Discord: https://s.voltagent.dev/discord
