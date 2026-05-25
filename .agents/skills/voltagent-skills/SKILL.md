---
name: voltagent-skills
version: 1.0.0
description: "VoltAgent Official Agent Skills — 4 offizielle Skills für das VoltAgent TypeScript-Framework. create-voltagent: CLI-Setup und manuelles Bootstrapping für neue Projekte. voltagent-best-practices: Architektur- und Nutzungsmuster für Agents, Workflows, Memory, Server. voltagent-core-reference: VoltAgent-Klassen-Optionen und Lifecycle-Methoden. voltagent-docs-bundle: Eingebettete Docs aus @voltagent/core/docs für versionsgenaue Dokumentation. Installation: npx skills add VoltAgent/skills"
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/skills
license: MIT
type: agent-skill
tags:
  - voltagent
  - typescript
  - agent-skills
  - framework
  - official
---

# VoltAgent Official Skills

Offizielle Agent Skills für Coding-Agents, die mit dem VoltAgent-Framework arbeiten.

## Installation

```bash
npx skills add VoltAgent/skills
```

## Die 4 Skills

### `create-voltagent`
Vollständiger Guide für neue VoltAgent-Projekte. CLI-Flow und manuelles Setup.

**Trigger**: User möchte ein VoltAgent-Projekt erstellen
```bash
npm create voltagent-app@latest
```

### `voltagent-best-practices`
Architektur- und Nutzungsmuster:
- Agent-Definition und Konfiguration
- Workflow-Design
- Memory-Adapter auswählen
- Server-Setup (Hono, Express)
- Multi-Agent-Patterns

### `voltagent-core-reference`
Vollständige Referenz für `@voltagent/core`:
- `VoltAgent` Klassen-Optionen
- `Agent` Lifecycle-Methoden
- `Workflow` API
- Memory, Tools, Guardrails

### `voltagent-docs-bundle`
Eingebettete Dokumentation aus `@voltagent/core/docs` — versionsgenaue Dokumentation direkt aus dem Package.

## Referenzen

- GitHub: https://github.com/VoltAgent/skills
- VoltAgent Framework: https://voltagent.dev/docs/
- npm: https://www.npmjs.com/package/@voltagent/core
