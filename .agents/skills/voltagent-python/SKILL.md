---
name: voltagent-python
version: 1.0.0
description: "VoltAgent Python SDK — Modernes, type-sicheres und async-fähiges Python SDK für AI-Agent-Observability und Tracing. Trackt LLM-Workflows, Agent-Interaktionen und Tool-Nutzung mit umfassender Telemetrie. Async Context Manager API: sdk.trace() → trace.add_agent() → agent.add_tool(). Unterstützt: Token-Usage, Multi-Agent-Hierarchien, Custom Events, Tags, Metadata. pip install voltagent"
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/voltagent-python
license: MIT
type: agent-skill
tags:
  - voltagent
  - python
  - observability
  - tracing
  - telemetry
  - async
---

# VoltAgent Python SDK

## Installation

```bash
pip install voltagent
```

## Async Context Manager API

```python
from voltagent import VoltAgentSDK

sdk = VoltAgentSDK(
    base_url="https://api.voltagent.dev",
    public_key="your-public-key",
    secret_key="your-secret-key",
    auto_flush=True,
    flush_interval=5
)

async with sdk.trace(
    agentId="customer-support-v1",
    input={"query": "Frage..."},
    userId="user-123",
    tags=["support"]
) as trace:

    async with trace.add_agent({
        "name": "Support Agent",
        "input": {"task": "Aufgabe"},
        "instructions": "Du bist ein hilfreicher Agent.",
    }) as agent:

        tool = await agent.add_tool({
            "name": "knowledge-base-search",
            "input": {"query": "Suchbegriff"}
        })
        await tool.success(output={"results": [...]})

        await agent.success(output={"response": "Antwort!"})
```

## Klassen-Hierarchie

```
VoltAgentSDK
└── TraceContextManager (sdk.trace())
    └── AgentContextManager (trace.add_agent())
        ├── ToolContextManager (agent.add_tool())
        ├── MemoryContextManager (agent.add_memory())
        └── RetrieverContextManager (agent.add_retriever())
```

## Schlüssel-Features

- **Async/Sync** — Context Manager für beide Modi
- **Auto-Flush** — Automatisches Senden im Hintergrund
- **Token-Tracking** — Input/Output Token-Zählung
- **Custom Events** — Beliebige Events hinzufügen
- **Multi-Agent** — Hierarchische Traces
- **Type-Safety** — Vollständige TypedDict-Definitionen

## Referenzen

- GitHub: https://github.com/VoltAgent/voltagent-python
- PyPI: https://pypi.org/project/voltagent/
- VoltOps Console: https://console.voltagent.dev/
