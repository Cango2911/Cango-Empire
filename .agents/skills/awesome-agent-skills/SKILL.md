---
name: awesome-agent-skills
version: 1.0.0
description: "Awesome Agent Skills — Kuratierte Sammlung von 1.424+ Agent Skills von 50+ offiziellen Teams und Organisationen. Cross-Agent-kompatibel: Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Antigravity. Kategorien: AI-Plattformen (Anthropic, Venice.ai, VoltAgent), Cloud-Provider (Vercel, Cloudflare, Netlify), Google (Stitch, Workspace CLI), Developer Tools (Expo, Hugging Face), Security (Trail of Bits), Monitoring (Sentry, Datadog), Frameworks (Angular, Stripe, Supabase), Community. Website: officialskills.sh"
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-agent-skills
license: MIT
type: agent-skill
tags:
  - agent-skills
  - claude-code
  - codex
  - cursor
  - gemini-cli
  - github-copilot
  - opencode
  - windsurf
  - cross-agent
  - curated-list
---

# Awesome Agent Skills

## Was sind Agent Skills?

Agent Skills sind spezialisierte Wissenspakete für AI-Coding-Assistenten. Sie erweitern Agents um domänenspezifisches Wissen (APIs, Frameworks, Best Practices) ohne den Kontext zu überladen.

**Cross-Agent-Kompatibilität**: Gleiche SKILL.md-Dateien funktionieren in Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Windsurf und Antigravity.

Website zum Durchsuchen: **https://officialskills.sh**

## Speicherpfade je AI-Assistent

| Tool | Projekt-Pfad | Globaler Pfad |
|------|-------------|---------------|
| Antigravity | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Gemini CLI | `.gemini/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |

## Installation

```bash
# Einzelne Skill-Datei (Beispiel: Stripe)
npx skills add stripe

# VoltAgent Skills
npx skills add voltagent/create-voltagent

# Anthropic Skills
npx skills add anthropic/docx
```

---

## Offizielle Provider — Vollständige Liste

### Anthropic (16 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `docx` | DOCX-Dateien lesen und erstellen |
| `pptx` | PowerPoint-Präsentationen erstellen |
| `xlsx` | Excel-Tabellen erstellen und bearbeiten |
| `pdf` | PDF-Dateien lesen und verarbeiten |
| `algorithmic-art` | Algorithmische Kunst und generative Grafik |
| `canvas-design` | Canvas-API für 2D-Grafik |
| `frontend-design` | Frontend-Designs und UI-Komponenten |
| `slack-gif-creator` | GIFs für Slack erstellen |
| `theme-factory` | Design-Themes generieren |
| `web-artifacts-builder` | Web-Artefakte und -Komponenten bauen |
| `mcp-builder` | MCP-Server entwickeln |
| `webapp-testing` | Web-App-Tests automatisieren |
| `brand-guidelines` | Markenrichtlinien umsetzen |
| `internal-comms` | Interne Kommunikation und Docs |
| `skill-creator` | Neue Agent Skills erstellen |
| `template` | Skill-Template-Vorlage |

### VoltAgent (4 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `create-voltagent` | VoltAgent-Projekte erstellen und konfigurieren |
| `voltagent-best-practices` | VoltAgent Best Practices |
| `voltagent-core-reference` | VoltAgent Core API-Referenz |
| `voltagent-docs-bundle` | VoltAgent vollständige Dokumentation |

### Venice.ai (19 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `api-overview` | Venice.ai API-Übersicht |
| `auth` | Authentifizierung |
| `chat` | Chat-Completions |
| `responses` | Response-API |
| `embeddings` | Text-Embeddings |
| `image-generate` | Bildgenerierung |
| `image-edit` | Bildbearbeitung |
| `audio-speech` | Text-to-Speech |
| `audio-music` | Musikgenerierung |
| `audio-transcription` | Audio-Transkription |
| `video` | Video-Generierung |
| `models` | Modell-Auswahl und -Konfiguration |
| `characters` | KI-Charaktere |
| `api-keys` | API-Key-Management |
| `billing` | Abrechnung und Credits |
| `x402` | X402 Payment Protocol |
| `crypto-rpc` | Crypto RPC-Integration |
| `augment` | Augment API |
| `errors` | Fehlerbehandlung |

### Vercel (7 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `v0` | v0 UI-Generierung |
| `ai-sdk` | Vercel AI SDK |
| `deployment` | Vercel Deployments |
| `edge-functions` | Edge Functions |
| `next-js` | Next.js mit Vercel |
| `postgres` | Vercel Postgres |
| `blob` | Vercel Blob Storage |

### Cloudflare (8 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `workers` | Cloudflare Workers |
| `pages` | Cloudflare Pages |
| `kv` | KV-Storage |
| `d1` | D1 SQLite-Datenbank |
| `r2` | R2 Object Storage |
| `ai` | Cloudflare AI |
| `durable-objects` | Durable Objects |
| `queues` | Cloudflare Queues |

### Netlify (12 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `blobs` | Netlify Blob Storage |
| `connect` | Netlify Connect |
| `deploy` | Netlify Deployments |
| `dev` | Lokale Entwicklung |
| `edge-functions` | Edge Functions |
| `environment-variables` | Umgebungsvariablen |
| `forms` | Netlify Forms |
| `functions` | Serverless Functions |
| `identity` | Netlify Identity/Auth |
| `image-cdn` | Image CDN |
| `sdk` | Netlify SDK |
| `visual-editor` | Visual Editor |

### Google Labs — Stitch (6 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `design-md` | DESIGN.md für AI-Agents |
| `component-library` | Stitch Komponentenbibliothek |
| `prototyping` | Schnelles UI-Prototyping |
| `design-tokens` | Design Token System |
| `theme-builder` | Theme-Generierung |
| `accessibility` | Barrierefreiheitsprüfung |

### Google Workspace CLI (17 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `calendar` | Google Calendar |
| `chat` | Google Chat |
| `docs` | Google Docs |
| `drive` | Google Drive |
| `forms` | Google Forms |
| `gmail` | Gmail |
| `keep` | Google Keep |
| `meet` | Google Meet |
| `sheets` | Google Sheets |
| `slides` | Google Slides |
| `tasks` | Google Tasks |
| `vault` | Google Vault |
| `workspace-admin` | Workspace Admin |
| `contacts` | Google Contacts |
| `groups` | Google Groups |
| `sites` | Google Sites |
| `workspace-sdk` | Workspace SDK |

### Expo (11 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `expo-router` | Expo Router Navigation |
| `eas-build` | EAS Build |
| `eas-submit` | EAS Submit |
| `eas-update` | EAS Update |
| `expo-sdk` | Expo SDK |
| `react-native` | React Native mit Expo |
| `push-notifications` | Push-Benachrichtigungen |
| `auth` | Authentifizierung |
| `sqlite` | SQLite-Datenbank |
| `camera` | Kamera-API |
| `payments` | In-App-Zahlungen |

### Hugging Face (13 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `inference-api` | Inference API |
| `hub` | Model Hub |
| `spaces` | Hugging Face Spaces |
| `datasets` | Dataset-Management |
| `transformers` | Transformers-Library |
| `diffusers` | Diffusers für Bildgenerierung |
| `tokenizers` | Tokenizer-Tools |
| `gradio` | Gradio UI-Framework |
| `text-generation` | Text-Generierung |
| `image-classification` | Bildklassifizierung |
| `speech-recognition` | Spracherkennung |
| `translation` | Übersetzung |
| `zero-shot` | Zero-Shot-Learning |

### Trail of Bits — Security (21 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `smart-contract-audit` | Smart Contract Audits |
| `fuzzing` | Fuzzing-Tests |
| `static-analysis` | Statische Code-Analyse |
| `binary-analysis` | Binäranalyse |
| `cryptography-review` | Kryptographie-Reviews |
| `threat-modeling` | Bedrohungsmodellierung |
| `secure-coding` | Sicheres Programmieren |
| `vulnerability-research` | Sicherheitslücken-Forschung |
| `incident-response` | Incident Response |
| `penetration-testing` | Penetrationstests |
| `red-team` | Red-Team-Operationen |
| `supply-chain` | Supply-Chain-Sicherheit |
| `container-security` | Container-Sicherheit |
| `cloud-security` | Cloud-Sicherheit |
| `mobile-security` | Mobile-App-Sicherheit |
| `web-security` | Web-Sicherheit |
| `api-security` | API-Sicherheit |
| `defi-security` | DeFi-Sicherheit |
| `formal-verification` | Formale Verifikation |
| `hardware-security` | Hardware-Sicherheit |
| `iot-security` | IoT-Sicherheit |

### Sentry (16 Skills)

| Skill | Beschreibung |
|-------|-------------|
| `error-tracking` | Fehler-Tracking |
| `performance` | Performance-Monitoring |
| `releases` | Release-Management |
| `alerts` | Alarme und Benachrichtigungen |
| `integrations` | Drittanbieter-Integrationen |
| `sourcemaps` | Source Map-Upload |
| `sdk-javascript` | JavaScript SDK |
| `sdk-python` | Python SDK |
| `sdk-react` | React SDK |
| `sdk-nextjs` | Next.js SDK |
| `sdk-node` | Node.js SDK |
| `sdk-mobile` | Mobile SDKs |
| `replay` | Session Replay |
| `profiling` | Code-Profiling |
| `ai-insights` | KI-Fehleranalyse |
| `crons` | Cron-Job-Monitoring |

### Weitere offizielle Provider

| Provider | Skills (Auswahl) |
|---------|----------------|
| **Angular** | angular-core, signals, standalone-components, routing, forms, http |
| **Composio** | 150+ Tool-Integrationen für AI-Agents |
| **Supabase** | auth, database, storage, edge-functions, realtime, vector |
| **Stripe** | payments, subscriptions, connect, billing, webhooks, testing |
| **Courier** | push, email, sms, in-app notifications, routing |
| **CallStack** | react-native, performance, debugging, profiling |
| **Better Auth** | auth-flows, sessions, oauth, mfa, organizations |
| **Tinybird** | real-time analytics, pipes, data sources, APIs |
| **HashiCorp** | terraform, vault, consul, nomad, packer |
| **Sanity** | schema, groq, content-lake, studio, webhooks |
| **Firecrawl** | web-scraping, crawling, extraction, llm-ready data |
| **Neon** | serverless-postgres, branching, compute, autoscaling |
| **ClickHouse** | analytics, queries, materialized-views, performance |
| **Remotion** | video-programmatic, react-video, lambda, player |
| **Replicate** | model-deployment, predictions, fine-tuning, webhooks |
| **Typefully** | twitter/x drafts, scheduling, analytics, threads |
| **fal.ai** | AI-Inferenz, Bildgenerierung, Video, Audio |
| **WordPress** | blocks, plugins, themes, REST-API, WP-CLI |
| **OpenAI** | completions, assistants, embeddings, fine-tuning |
| **Figma** | REST-API, Plugins, MCP-Integration, Design-Tokens |
| **Binance** | spot-trading, futures, websockets, API-docs |
| **MiniMax** | Text-to-Video, LLM, TTS, Image |
| **DuckDB** | OLAP queries, extensions, wasm, spatial |
| **GSAP** | animations, scrolltrigger, timeline, plugins |
| **Notion** | databases, blocks, pages, search, API |
| **Resend** | transactional email, React Email, webhooks |
| **MongoDB** | CRUD, aggregation, indexes, Atlas, vector-search |
| **Apollo GraphQL** | schema, resolvers, federation, caching |
| **Auth0** | authentication, authorization, rules, hooks |
| **Brave** | search-API, summarizer, news, video |
| **Browserbase** | headless browser, session-management, automation |
| **CodeRabbit** | AI code review, PR-analysis, suggestions |
| **Coinbase** | CDP, onchain-APIs, wallets, staking |
| **Datadog Labs** | metrics, logs, traces, dashboards, alerts |
| **Firebase** | auth, firestore, storage, functions, hosting |
| **Flutter** | widgets, state-management, platform-channels |
| **Redis** | data-structures, caching, pub-sub, streams |
| **NVIDIA** | CUDA, NIM, NeMo, Triton, GPU-computing |
| **Google Cloud** | BigQuery, GKE, Cloud Run, Vertex AI, Storage |

### Community Skills (Auswahl)

| Autor | Skills |
|-------|--------|
| **Corey Haines** | AI-powered business workflows |
| **Dean Peters** | Developer productivity tools |
| **Paweł Huryn** | Product management, user stories |
| **Addy Osmani** | Performance, web vitals, optimization |
| **Garry Tan** | Startup advice, product strategy |
| **Kim Barrett** | iOS development, Swift best practices |

---

## Qualitätsstandards für Agent Skills

### Beschreibung (Description)
- Dritte Person, spezifische Schlüsselwörter für Agent-Matching
- Beinhaltet: was der Skill macht, wann er verwendet wird, Technologien
- Beispiel: "Implements Stripe payment flows — checkout sessions, subscriptions, webhooks"

### Progressive Disclosure
- Top-Level-Metadaten: unter ~100 Token
- Body: unter 500 Zeilen
- Keine absoluten Pfade
- Nur scoped Tools

### Dateiformat

```yaml
---
name: skill-name
description: "Dritte Person, spezifisch, Schlüsselwörter"
tools: Read, Write, Edit, Bash
---

# Skill Content
```

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-agent-skills
- Website: https://officialskills.sh
- VoltAgent: https://github.com/VoltAgent/voltagent
- Claude Code Docs: https://docs.anthropic.com/en/docs/claude-code/skills
