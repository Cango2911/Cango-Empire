---
name: awesome-claude-design
version: 1.0.0
description: "Awesome Claude Design — 68 DESIGN.md-Dateien speziell für Claude Design (claude.ai/design). Jede Datei beschreibt ein Marken-Designsystem (Farben, Typographie, Komponenten), das Claude Design in ein vollständiges UI-System (Tokens, Komponenten, Preview Assets) umwandelt. Workflow: DESIGN.md hochladen → Claude Design scaffoldet vollständiges Design-System in einem Schuss. Format: Google Stitch DESIGN.md-Standard. Unterschied zu awesome-design-md: optimiert für Claude Design Workspace (persistent design system), nicht nur Chat-Kontext."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-claude-design
license: MIT
type: agent-skill
tags:
  - claude-design
  - design-md
  - design-system
  - ui
  - anthropic
---

# Awesome Claude Design

## Was ist Claude Design?

[Claude Design](https://claude.ai/design) ist Anthropics Design-fokussierter Workspace. Er hält ein persistentes Design-System für dein Projekt — Tokens, Komponenten und Preview Assets, nicht nur Chat-Swatches.

Workflow:
1. DESIGN.md aus dieser Sammlung auswählen
2. Bei claude.ai/design hochladen
3. Claude scaffoldet vollständiges Design-System: Farb-Tokens, Typographie, Buttons, Cards, Nav, UI-Kit

## Unterschied zu awesome-design-md

| | awesome-design-md | awesome-claude-design |
|--|-------------------|----------------------|
| Für | Allgemeine AI-Agents | Claude Design spezifisch |
| Output | UI-Generierung im Chat | Persistentes Design-System |
| Workspace | Claude Code, Cursor, etc. | claude.ai/design |

## DESIGN.md Format

Gleicher Google Stitch Standard — YAML-Frontmatter + 9 Sektionen:
- Farb-Tokens (primary, ink, canvas, hairline, muted, surface-*)
- Typographie-Hierarchie
- Komponenten-Styling
- Layout-Prinzipien
- Do's & Don'ts

## Verwendung

**Option A: Design System**
1. claude.ai/design → Create new design system
2. DESIGN.md unter "Add assets" hochladen

**Option B: Prototype**
1. Neues Prototype erstellen
2. DESIGN.md im Chat anhängen
3. Prompt: "Create a design system from this DESIGN.md"

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-claude-design
- Claude Design: https://claude.ai/design
- DESIGN.md Format: https://getdesign.md/what-is-design-md
