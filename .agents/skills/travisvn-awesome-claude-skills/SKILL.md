---
name: travisvn-awesome-claude-skills
description: Kuratierte Awesome List für Claude Skills von travisvn. Enthält offizielle Anthropic Skills, Community Skills, Vergleichstabellen (Skills vs MCP vs System Prompts vs Subagents), Sicherheitsrichtlinien, Troubleshooting, FAQ und Tutorials. Nutze diesen Skill um Claude Skills zu entdecken, zu verstehen und zu vergleichen.
license: MIT
metadata:
  author: travisvn
  source: https://github.com/travisvn/awesome-claude-skills
compatibility: Claude Code, Claude.ai, any AI coding agent
allowed-tools: Read
---

# Awesome Claude Skills (travisvn)

Kuratierte Referenz für Claude Skills — offizielle + Community Skills, Architektur, Sicherheit, FAQ.

## 🎯 Offizielle Anthropic Skills

### Dokumente
- **docx** — Word-Dokumente (tracked changes, comments, formatting)
- **pdf** — PDF-Manipulation (extract, create, merge, split, forms)
- **pptx** — PowerPoint (layouts, templates, charts, automation)
- **xlsx** — Excel (formulas, formatting, data analysis, viz)

### Design & Creative
- **algorithmic-art** — Generative Art mit p5.js (flow fields, particles)
- **canvas-design** — Visual Art als .png/.pdf
- **slack-gif-creator** — Animierte GIFs für Slack

### Development
- **frontend-design** — Anti-"AI Slop"-Design, React + Tailwind
- **web-artifacts-builder** — HTML Artifacts mit React + Tailwind + shadcn/ui
- **mcp-builder** — MCP-Server für externe APIs erstellen
- **webapp-testing** — Playwright UI-Testing für lokale Web-Apps

### Communication
- **brand-guidelines** — Anthropic Brand Colors + Typography
- **internal-comms** — Status Reports, Newsletters, FAQs

### Skill Creation
- **skill-creator** — Interaktives Q&A zum Skill-Erstellen

## 🌟 Community Skills

| Skill | Beschreibung |
|-------|-------------|
| [obra/superpowers](https://github.com/obra/superpowers) | 20+ Skills: TDD, Debugging, `/brainstorm`, `/write-plan`, `/execute-plan` |
| [ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) | iOS App-Navigation und -Testing via Automation |
| [ffuf-web-fuzzing](https://github.com/jthack/ffuf_claude_skill) | Web Fuzzing für Penetration Testing |
| [playwright-skill](https://github.com/lackeyjb/playwright-skill) | Browser-Automation mit Playwright |
| [claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) | D3.js Datenvisualisierungen |
| [Trail of Bits Security](https://github.com/trailofbits/skills) | CodeQL/Semgrep, Code Auditing, Vulnerability Detection |
| [Expo Skills](https://github.com/expo/skills) | Offizielle Expo-Skills für Mobile Dev |
| [shadcn/ui](https://ui.shadcn.com/docs/skills) | shadcn Component-Kontext + Pattern-Enforcement |
| [get-shit-done](https://github.com/gsd-build/get-shit-done) | Meta-Prompting, Context Engineering, Spec-Driven Dev |
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | HTML-Präsentationen aus PowerPoint |
| [loki-mode](https://github.com/asklokesh/claudeskill-loki-mode) | 37 AI Agents in 6 Swarms — komplettes Startup-System |

## 💡 Wann was verwenden?

| Tool | Wann |
|------|------|
| **Skills** | Wiederverwendbares Prozeduralwissen über Conversations hinweg |
| **Prompts** | Einmalige Anweisungen und sofortiger Kontext |
| **Projects** | Persistentes Hintergrundwissen im Workspace |
| **Subagents** | Unabhängige Task-Ausführung mit spezifischen Berechtigungen |
| **MCP** | Claude mit externen Datenquellen verbinden |

**Faustregel:** Schreibst du denselben Prompt immer wieder? → Erstelle einen Skill.

## Skills vs MCP

| Feature | Skills | MCP |
|---------|--------|-----|
| Zweck | Task-spezifisches Expertise + Workflows | Externe Daten-/API-Integration |
| Portabilität | Überall gleich (Claude.ai, Code, API) | Benötigt Server-Konfiguration |
| Token-Effizienz | ~100 Token bis geladen | Variiert |
| Beste Nutzung | Wiederholbare Tasks, Dokument-Workflows | DB-Zugriff, API-Integrationen |

## Skills vs System Prompts

| Feature | Skills | System Prompts |
|---------|--------|----------------|
| Struktur | Ordner mit YAML + Scripts | Reiner Text |
| Wiederverwendung | Versioniert, teilbar, komposierbar | Copy-Paste |
| Laden | On-Demand (nur wenn relevant) | Immer im Kontext |
| Wartung | Zentrale Updates | Manuelle Updates pro Conversation |

## 🔒 Sicherheit

- Nur Skills aus vertrauenswürdigen Quellen installieren
- SKILL.md und alle Scripts vor Aktivierung prüfen
- [Weaponizing Claude Code Skills](https://medium.com/@yossifqassim/weaponizing-claude-code-skills-from-5-5-to-remote-shell-a14af2d109c9) — Bekannte Angriffsvektoren lesen

## Progressive Disclosure Architektur

1. **Metadata (~100 Token)**: Claude scannt verfügbare Skills
2. **Full Instructions (<5k Token)**: Laden wenn relevant
3. **Bundled Resources**: Nur bei Bedarf laden

Quelle: https://github.com/travisvn/awesome-claude-skills
