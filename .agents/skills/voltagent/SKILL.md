---
name: voltagent
version: 1.0.0
description: "VoltAgent — Open-Source TypeScript AI-Agent-Engineering-Plattform. Core Framework (@voltagent/core): Memory, RAG, Guardrails, Tools, MCP, Voice, Workflow Engine, Supervisors & Sub-Agents, Resumable Streaming. VoltOps Console: Observability, Automation, Deployment, Evals, Guardrails, Prompts. Packages: core, cli, server-hono, rag, libsql, postgres, logger, evals, mcp-server, vercel-ai, anthropic-ai, google-ai, groq-ai, cloudflare-d1, ag-ui, a2a-server, langfuse-exporter, resumable-streams, docs-mcp."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/voltagent
license: MIT
type: agent-skill
tags:
  - voltagent
  - typescript
  - ai-agents
  - framework
  - multi-agent
  - rag
  - mcp
  - observability
---

# VoltAgent Framework

## Quick Start

```bash
npm create voltagent-app@latest
```

## Kernkonzepte

### Agent definieren

```typescript
import { VoltAgent, Agent } from "@voltagent/core";
import { VercelAIProvider } from "@voltagent/vercel-ai";
import { openai } from "@ai-sdk/openai";

const agent = new Agent({
  name: "my-agent",
  description: "Beschreibung wann dieser Agent genutzt wird",
  llm: new VercelAIProvider(),
  model: openai("gpt-4o-mini"),
  tools: [weatherTool],
  memory: new LibSQLMemoryAdapter({ url: "file:memory.db" }),
});

new VoltAgent({ agents: { agent } });
```

### Multi-Agent (Supervisor)

```typescript
const supervisor = new Agent({
  name: "supervisor",
  subAgents: [specialistA, specialistB],
  // Supervisor routet automatisch zu Spezialisten
});
```

### Workflow Engine

```typescript
import { createWorkflow, createStep } from "@voltagent/core";

const workflow = createWorkflow({
  id: "my-workflow",
  steps: [stepA, stepB, stepC],
  // Deklarativ, keine custom Control Flow
});
```

## Package-Übersicht

| Package | Funktion |
|---------|---------|
| `@voltagent/core` | Agent-Runtime, Workflow, Memory, Tools, Guardrails |
| `@voltagent/cli` | CLI-Werkzeuge |
| `@voltagent/server-hono` | HTTP-Server (Hono) |
| `@voltagent/rag` | RAG / Retrieval-Pipeline |
| `@voltagent/libsql` | LibSQL Memory-Adapter |
| `@voltagent/postgres` | PostgreSQL Memory-Adapter |
| `@voltagent/logger` | Pino-Logger-Integration |
| `@voltagent/evals` | Eval-Suite |
| `@voltagent/mcp-server` | MCP Docs Server |
| `@voltagent/vercel-ai` | Vercel AI Provider |
| `@voltagent/anthropic-ai` | Anthropic Provider |
| `@voltagent/google-ai` | Google AI Provider |
| `@voltagent/groq-ai` | Groq Provider |
| `@voltagent/cloudflare-d1` | Cloudflare D1 Adapter |
| `@voltagent/resumable-streams` | Resumable Streaming |
| `@voltagent/langfuse-exporter` | Langfuse Observability |
| `@voltagent/a2a-server` | Agent-to-Agent Server |
| `@voltagent/ag-ui` | AG-UI Integration |
| `@voltagent/docs-mcp` | MCP-Docs-Server für Claude/Cursor |

## MCP Docs Server (für Claude Code / Cursor)

```json
{
  "mcpServers": {
    "voltagent-docs": {
      "command": "npx",
      "args": ["-y", "@voltagent/mcp-docs-server"]
    }
  }
}
```

## Referenzen

- GitHub: https://github.com/VoltAgent/voltagent
- Dokumentation: https://voltagent.dev/docs/
- npm: https://www.npmjs.com/package/@voltagent/core
- Discord: https://s.voltagent.dev/discord
