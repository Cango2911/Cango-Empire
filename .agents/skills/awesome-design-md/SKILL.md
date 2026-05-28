---
name: awesome-design-md
version: 1.0.0
description: "Awesome DESIGN.md — Kuratierte Sammlung von 73 DESIGN.md-Dateien für AI-Agents (Google Stitch-Format). Jede Datei enthält: Farbpalette mit Hex-Werten, Typographie-Hierarchie, Komponenten-Styling (Buttons/Cards/Inputs/Navigation), Layout-Prinzipien, Depth-System, Do's & Don'ts, Responsive Behavior, Agent-Prompt-Guide. Marken: Stripe, Apple, Tesla, Spotify, Notion, Linear, Figma, Supabase, Vercel, Claude, Ferrari, Lamborghini, Bugatti, BMW, Nike u.v.m."
author: VoltAgent (Open Source, MIT)
source: https://github.com/VoltAgent/awesome-design-md
license: MIT
type: agent-skill
tags:
  - design
  - design-system
  - ui
  - css
  - typography
  - color-palette
  - ai-agent
  - google-stitch
  - design-md
---

# Awesome DESIGN.md

## Was ist DESIGN.md?

[DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) ist ein von Google Stitch eingeführtes Konzept: Eine Klartext-Designsystem-Datei, die AI-Agents lesen, um konsistente UI zu generieren.

```
AGENTS.md   → Coding-Agents   → Wie das Projekt gebaut wird
DESIGN.md   → Design-Agents   → Wie das Projekt aussehen soll
```

**Verwendung**: DESIGN.md-Datei ins Projektstamm kopieren, dann Agent anweisen:
> "Build me a page that looks like this" → pixel-perfekte UI

## Datei-Format (Google Stitch DESIGN.md-Standard)

Jede DESIGN.md enthält YAML-Frontmatter + 9 Markdown-Sektionen:

```yaml
---
version: alpha
name: brand-design-analysis
description: "Design-Philosophie in einem Satz"

colors:
  primary: "#hex"
  ink: "#hex"
  canvas: "#hex"
  # weitere Tokens...

typography:
  display-xl:
    fontFamily: "..."
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  # weitere Stufen...
---
```

### 9 Sektionen jeder DESIGN.md

| # | Sektion | Inhalt |
|---|---------|--------|
| 1 | Visual Theme & Atmosphere | Stimmung, Dichte, Design-Philosophie |
| 2 | Color Palette & Roles | Semantische Namen + Hex + Funktion |
| 3 | Typography Rules | Schriftfamilien, vollständige Hierarchie |
| 4 | Component Stylings | Buttons, Cards, Inputs, Navigation mit Zuständen |
| 5 | Layout Principles | Abstands-Skala, Grid, Whitespace-Philosophie |
| 6 | Depth & Elevation | Schatten-System, Surface-Hierarchie |
| 7 | Do's and Don'ts | Design-Guardrails und Anti-Patterns |
| 8 | Responsive Behavior | Breakpoints, Touch-Targets, Collapsing |
| 9 | Agent Prompt Guide | Farb-Referenz, fertige Prompts |

## Vollständige Marken-Sammlung (73 Marken)

### AI & LLM-Plattformen

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Claude** | Warme Creme, Serif-Headlines, Korall-CTAs | `#cc785c` Terrakotta |
| **Cohere** | Enterprise, lebhafte Gradienten, Dashboard | — |
| **ElevenLabs** | Dunkle cinematische UI, Audio-Waveform-Ästhetik | — |
| **Minimax** | Fettes Dark Interface, Neon-Akzente | — |
| **Mistral AI** | Französischer Minimalismus, Lila-Töne | — |
| **Ollama** | Terminal-first, monochrom, simpel | — |
| **OpenCode AI** | Developer-zentriert, dunkles Theme | — |
| **Replicate** | Weiße Leinwand, Code-first | — |
| **Runway** | Editorial, Filmfestival-Ästhetik, schwarze Pill-CTAs | — |
| **Together AI** | Technisch, Blueprint-Stil | — |
| **VoltAgent** | Void-Black, Emerald-Akzent, Terminal-nativ | — |
| **xAI** | Stark monochrom, futuristischer Minimalismus | — |

### Developer Tools & IDEs

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Cursor** | Schlankes Dark Interface, Gradient-Akzente | — |
| **Expo** | Dark Theme, enge Buchstabenabstände, Code-zentriert | — |
| **Lovable** | Verspielt, Gradienten, freundliche Dev-Ästhetik | — |
| **Raycast** | Dunkles Chrome, lebhafte Gradient-Akzente | — |
| **Superhuman** | Premium Dark UI, Keyboard-first, Lila-Glow | — |
| **Vercel** | Schwarz-Weiß-Präzision, Geist-Font | `#000000` |
| **Warp** | Dunkle IDE-UI, Block-basiertes Command-UI | — |

### Backend, Database & DevOps

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **ClickHouse** | Gelb-akzentuiert, technische Dokumentation | — |
| **Composio** | Modernes Dark, bunte Integrations-Icons | — |
| **HashiCorp** | Enterprise-clean, Schwarz-Weiß | — |
| **MongoDB** | Grünes Blatt-Branding, Entwickler-Dokumentation | — |
| **PostHog** | Verspieltes Igel-Branding, Developer-Dark | — |
| **Sanity** | Dark Editorial, 112px Display-Type, Korall-CTA | — |
| **Sentry** | Dark Dashboard, Daten-dicht, Pink-Lila | — |
| **Supabase** | Dark Emerald, Code-first | `#3ecf8e` |

### Productivity & SaaS

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Cal.com** | Neutral, clean, Developer-orientiert | — |
| **Intercom** | Freundliches Blau, Conversational UI | — |
| **Linear** | Ultra-minimal, präzise, Lila-Akzent | `#5e6ad2` |
| **Mintlify** | Grün-akzentuiert, leseoptimiert | — |
| **Notion** | Warmer Minimalismus, Serif-Headlines, weiche Flächen | — |
| **Resend** | Minimales Dark, Monospace-Akzente | — |
| **Zapier** | Warmes Orange, freundliche Illustration | — |

### Design & Creative Tools

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Airtable** | Farbenfroh, freundlich, Datenstruktur | — |
| **Clay** | Organische Formen, weiche Gradienten | — |
| **Figma** | Lebhaft mehrfarbig, verspielt aber professionell | — |
| **Framer** | Fettes Schwarz-Blau, Motion-first | — |
| **Miro** | Helles Gelb, unendliche Canvas-Ästhetik | `#ffd02f` |
| **Webflow** | Blau-akzentuiert, polierte Marketing-Site | — |

### Fintech & Crypto

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Binance** | Binance-Gelb auf Monochrom, Trading-Urgency | `#f0b90b` |
| **Coinbase** | Sauberes Blau, Vertrauen, institutionell | — |
| **Kraken** | Lila Dark UI, Daten-dichte Dashboards | — |
| **Mastercard** | Warme Creme, Orbital-Pill-Formen | — |
| **Revolut** | Schlankes Dark, Gradient-Cards, Fintech-Präzision | — |
| **Stripe** | Lila Gradienten, 300-Weight-Eleganz | `#533afd` |
| **Wise** | Helles Grün, freundlich und klar | — |

### E-Commerce & Retail

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Airbnb** | Warmes Korall, Fotografie-getrieben, abgerundet | `#ff5a5f` |
| **Meta** | Fotografie-first, binäre Flächen, Meta-Blau CTAs | — |
| **Nike** | Monochrom, massives Uppercase Futura, Full-Bleed | — |
| **Shopify** | Dark-first, Neon-Grün, ultra-leichte Display-Type | — |
| **Starbucks** | Vier-Ebenen Erd-Grün, warme Creme, SoDoSans | — |

### Media & Consumer Tech

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **Apple** | Premium Whitespace, SF Pro, cinematische Bilder | — |
| **IBM** | Carbon Design System, strukturiertes Blau | — |
| **NVIDIA** | Grün-Schwarz-Energie, technische Power | `#76b900` |
| **Pinterest** | Rot-Akzent, Masonry Grid, Bild-first | `#e60023` |
| **PlayStation** | Drei-Flächen-Layout, Cyan Hover-Interaktion | — |
| **Slack** | — | — |
| **SpaceX** | Stark Schwarz-Weiß, Full-Bleed, futuristisch | — |
| **Spotify** | Lebhaftes Grün auf Dark, fette Type, Album-Art | `#1db954` |
| **The Verge** | Acid-Mint + Ultraviolett, Manuka Display-Type | — |
| **Uber** | Fettes Schwarz-Weiß, enge Type, urbane Energie | — |
| **Vodafone** | Monumentales Uppercase, Vodafone-Rot | `#e60000` |
| **WIRED** | Papier-Weiß Broadsheet, Custom Serif, Blau-Links | — |

### Automotive

| Marke | Design-Sprache | Primärfarbe |
|-------|----------------|-------------|
| **BMW** | Dunkle Premium-Flächen, präzise Deutsche Ästhetik | — |
| **BMW M** | Motorsport-Kontrast, M-Farb-Akzente | — |
| **Bugatti** | Cinema-Black, Monochrom, monumentale Display-Type | — |
| **Ferrari** | Chiaroscuro Schwarz-Weiß, Ferrari-Rot, extrem sparsam | `#da291c` |
| **Lamborghini** | True Black Cathedral, Gold-Akzent, LamboType | — |
| **Renault** | Aurora-Gradienten, NouvelR Typeface, Zero-Radius | — |
| **Tesla** | Radikale Subtraktion, cinematische Full-Viewport-Fotografie | — |

## Verwendung mit AI-Agents

### Methode 1: Direkt ins Projekt kopieren

```bash
# DESIGN.md einer Marke ins Projekt-Root kopieren
cp design-md/stripe/DESIGN.md ./DESIGN.md
```

Dann dem Agent sagen:
```
Build me a landing page that matches the design system in DESIGN.md
```

### Methode 2: Als Kontext in Prompts

```
Using the Stripe design system (purple gradient background #533afd, 
Sohne font weight 300, tight letter-spacing, pill buttons), 
create a pricing page.
```

### Methode 3: Google Stitch

DESIGN.md wird von [Google Stitch](https://stitch.withgoogle.com/) nativ gelesen für UI-Generierung.

### Effektive Agent-Prompts

```
# Allgemein
"Follow the DESIGN.md in the project root for all UI decisions"

# Spezifisch
"Build a card component using the Vercel design system: 
black/white, Geist font, 1px hairline borders"

# Mehrere Marken kombinieren
"Use Stripe's color palette with Linear's spacing and 
Notion's typography hierarchy"
```

## Farb-Token-Konventionen

Alle DESIGN.md-Dateien verwenden konsistente semantische Farbnamen:

| Token | Bedeutung |
|-------|-----------|
| `primary` | Haupt-Akzentfarbe / CTA-Farbe |
| `ink` | Haupt-Textfarbe |
| `canvas` | Hintergrundfarbe |
| `hairline` | Border-/Trennlinien-Farbe |
| `muted` | Sekundärer Text |
| `surface-*` | Karten-/Flächen-Varianten |
| `on-primary` | Text auf primary-Hintergrund |

## Referenzen

- GitHub: https://github.com/VoltAgent/awesome-design-md
- DESIGN.md Format: https://stitch.withgoogle.com/docs/design-md/format/
- Google Stitch: https://stitch.withgoogle.com/docs/design-md/overview/
- Alle DESIGN.md-Vorschauen: https://getdesign.md/
- VoltAgent: https://github.com/VoltAgent/voltagent
