---
name: vercel-ai-sdk-observability
version: 1.0.0
description: "VoltAgent + Vercel AI SDK Observability Example — Zeigt wie VoltAgent-Observability in bestehende Vercel AI SDK-Apps integriert wird. Nutzt OpenTelemetry + VoltAgentExporter + experimental_telemetry. Trackt AI-Calls, Tool-Usage und Multi-Agent-Workflows in der VoltAgent Developer Console. Minimal-Setup: VoltAgentExporter initialisieren + NodeSDK starten + experimental_telemetry: {isEnabled: true} hinzufügen."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/vercel-ai-sdk-observability
license: MIT
type: agent-skill
tags:
  - voltagent
  - vercel-ai-sdk
  - observability
  - opentelemetry
  - tracing
  - typescript
---

# VoltAgent + Vercel AI SDK Observability

## Minimal-Setup

```typescript
import { VoltAgentExporter } from "@voltagent/vercel-ai-exporter";
import { NodeSDK } from "@opentelemetry/sdk-node";
import { getNodeAutoInstrumentations } from "@opentelemetry/auto-instrumentations-node";

const voltAgentExporter = new VoltAgentExporter({
  publicKey: process.env.VOLTAGENT_PUBLIC_KEY,
  secretKey: process.env.VOLTAGENT_SECRET_KEY,
});

const sdk = new NodeSDK({
  traceExporter: voltAgentExporter,
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start();

// Dann in jedem generateText/streamText Aufruf:
const result = await generateText({
  model: openai("gpt-4o-mini"),
  prompt: "Hello!",
  experimental_telemetry: { isEnabled: true },
});
```

## Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key
VOLTAGENT_PUBLIC_KEY=your_voltagent_public_key
VOLTAGENT_SECRET_KEY=your_voltagent_secret_key
```

## Was wird getrackt

- Alle `generateText` / `streamText` Aufrufe
- Tool-Aufrufe und Ergebnisse
- Token-Usage
- Multi-Agent-Workflows
- Latenz und Fehler

## Referenzen

- GitHub: https://github.com/VoltAgent/vercel-ai-sdk-observability
- VoltOps Console: https://console.voltagent.dev/
- Vercel AI SDK: https://sdk.vercel.ai/
