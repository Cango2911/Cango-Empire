---
name: ai-agent-platform
version: 1.0.0
description: "VoltAgent AI Agent Platform — Konzeptionelle Dokumentation und Architektur-Referenz für den Aufbau produktionsreifer AI-Agent-Systeme. Erklärt die 11 Infrastruktur-Kategorien: Core Runtime, Workflow Engine, Multi-Agent Orchestration, Tool Registry & MCP, LLM Provider Abstraction, Memory/RAG, Safety & Guardrails, Observability & Tracing, Deployment (Edge/Serverless/Server), Monitoring, Voice. Nutze VoltAgent als Implementierung."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/ai-agent-platform
license: MIT
type: agent-skill
tags:
  - voltagent
  - architecture
  - ai-agents
  - platform
  - reference
---

# AI Agent Platform — Architektur-Referenz

## Die 11 Infrastruktur-Kategorien

| Kategorie | Komponenten |
|-----------|------------|
| **Core Runtime** | Agent Orchestration Engine, LLM Provider Abstraction, Streaming, Cancellation, Type-Safe Definitions |
| **Workflow Engine** | Deklarative Multi-Step-Automationen |
| **Multi-Agent** | Supervisor-Patterns, Sub-Agents, Task-Routing |
| **Tool Registry & MCP** | Zod-typed Tools, Lifecycle Hooks, MCP-Server |
| **LLM Compatibility** | OpenAI, Anthropic, Google, Provider-Swap ohne Code-Rewrite |
| **Memory** | Durable Memory Adapters, Cross-Run Context |
| **RAG** | Retriever Agents, Document Ingestion, Vector Search |
| **Safety & Guardrails** | Input/Output-Validierung, Content Policies |
| **Observability** | Trace Visualization, Cost Tracking, Debugging |
| **Deployment** | Edge, Serverless, Server — Skalierung |
| **Monitoring** | Performance, Qualität, Cost Analytics |

## Implementierung: VoltAgent

```bash
npm create voltagent-app@latest
```

## Referenzen

- GitHub: https://github.com/VoltAgent/ai-agent-platform
- VoltAgent Framework: https://voltagent.dev/docs/
