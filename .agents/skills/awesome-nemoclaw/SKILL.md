---
name: awesome-nemoclaw
version: 1.0.0
description: "Awesome NemoClaw — YAML-Presets, Rezepte und Deployment-Patterns für NemoClaw (NVIDIA OpenShell Sandbox-Runtime für OpenClaw). 18 fertige Network-Policy-Presets: Stripe, AWS, GCP, Cloudflare, Vercel, GitLab, Google Workspace, HubSpot, Confluence, Sentry, Airtable, Notion, Linear, Algolia, Neon, Supabase, Zendesk, Teams. Least-Privilege: Nur explizit erlaubte Endpoints/Methoden werden durchgelassen."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-nemoclaw
license: MIT
type: agent-skill
tags:
  - nemoclaw
  - nvidia
  - openclaw
  - network-policy
  - sandbox
  - security
---

# Awesome NemoClaw

## Was ist NemoClaw?

**NemoClaw** ist eine Open-Source Runtime-Schicht für OpenClaw innerhalb einer kontrollierten NVIDIA OpenShell Sandbox. OpenClaw ist das Agent-Framework; NemoClaw fügt hinzu:
- Sandboxing und Isolation
- Policy-basierte Netzwerkkontrolle
- Inference-Routing
- Operationale Werkzeuge

## Installation

```bash
# NemoClaw installieren
curl -fsSL https://nvidia.com/nemoclaw.sh | bash

# Agent verbinden
nemoclaw my-assistant connect
```

## Policy Presets

Fertige Netzwerk-Policy-Bundles für gängige Dienste (Least-Privilege-Prinzip).

| Preset | Datei | Erlaubte Endpoints |
|--------|-------|-------------------|
| Stripe | `presets/stripe.yaml` | api.stripe.com /v1/** (GET, POST) |
| AWS | `presets/aws.yaml` | AWS-API-Endpoints |
| GCP | `presets/gcp.yaml` | Google Cloud APIs |
| Cloudflare | `presets/cloudflare.yaml` | Cloudflare APIs |
| Vercel | `presets/vercel.yaml` | Vercel Deployment APIs |
| GitLab | `presets/gitlab.yaml` | GitLab REST/GraphQL |
| Google Workspace | `presets/google-workspace.yaml` | Google APIs |
| HubSpot | `presets/hubspot.yaml` | api.hubspot.com |
| Confluence | `presets/confluence.yaml` | Atlassian APIs |
| Sentry | `presets/sentry.yaml` | sentry.io APIs |
| Airtable | `presets/airtable.yaml` | api.airtable.com |
| Notion | `presets/notion.yaml` | api.notion.com |
| Linear | `presets/linear.yaml` | api.linear.app |
| Algolia | `presets/algolia.yaml` | Algolia Search APIs |
| Neon | `presets/neon.yaml` | Neon Postgres APIs |
| Supabase | `presets/supabase.yaml` | Supabase APIs |
| Zendesk | `presets/zendesk.yaml` | Zendesk Support APIs |
| Teams | `presets/teams.yaml` | Microsoft Teams APIs |

## Preset-Format (YAML)

```yaml
preset:
  name: service-name
  description: "Beschreibung (Least-Privilege)"

network_policies:
  service:
    endpoints:
      - host: api.service.com
        port: 443
        protocol: rest
        enforcement: enforce
        tls: terminate
        rules:
          - allow: { method: GET, path: "/v1/**" }
          - allow: { method: POST, path: "/v1/**" }
```

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-nemoclaw
- NemoClaw Docs: https://docs.nvidia.com/nemoclaw/
- NVIDIA OpenShell: https://github.com/NVIDIA/OpenShell
