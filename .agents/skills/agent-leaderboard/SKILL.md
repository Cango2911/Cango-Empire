---
name: agent-leaderboard
description: Agent Leaderboard — Live-Ranking der beliebtesten KI-Agent-Repositories auf GitHub, täglich aktualisiert. Trackt 5 Kategorien mit insgesamt 6456+ Repos: Agent Skills (1785), MCP Server (1569), Prompt Libraries (1146), AI Frameworks (1251), Auto Research (705). Nutze diesen Skill um die aktuell trendenden KI-Agent-Ökosystem-Repos zu entdecken und zu vergleichen. Daten unter .agents/plugins/agent-leaderboard/data/.
license: MIT
metadata:
  author: jaychempan
  source: https://github.com/jaychempan/Agent-Leaderboard
  website: https://agentskills.media
  updated: "2026-05-24"
compatibility: Claude Code, any AI coding agent
allowed-tools: Bash, Read
---

# Agent Leaderboard

Live-Ranking der beliebtesten KI-Agent-Repositories auf GitHub, gerankt nach Stars und täglich aktualisiert. Website: [agentskills.media](https://agentskills.media)

## 5 Boards, 6456+ Repositories

| Board | Repos | Inhalt |
|-------|------:|-------|
| 🛠 Agent Skills | 1785 | Installierbare Skills für Claude Code, Cursor, Codex, Copilot, Gemini |
| 🔌 MCP Server | 1569 | Model Context Protocol Server für erweiterte Agent-Tool-Nutzung |
| 📚 Prompt Libraries | 1146 | System-Prompts, Prompt-Sammlungen, Prompt-Engineering-Guides |
| 🏗 AI Frameworks | 1251 | Agent-Orchestrierung, Multi-Agent-Plattformen, LLM-App-Scaffolding |
| 🔬 Auto Research | 705 | Autonome Deep-Research-Agents und KI-Recherche-Tools |

## Datenzugriff

Alle Daten als JSON unter `.agents/plugins/agent-leaderboard/data/`:

```bash
# Agent Skills laden
python3 -c "
import json
d = json.load(open('.agents/plugins/agent-leaderboard/data/data.json'))
for r in d['repos'][:10]:
    print(f'{r[\"full_name\"]} ★{r[\"stars\"]}')
"
```

## Top 15 Agent Skills (Stand: 2026-05-24)

| # | Repository | Stars | Kategorie |
|---|-----------|------:|----------|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | ★204.293 | Agentic Skills Framework |
| 2 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | ★189.459 | Claude Performance Optimizer |
| 3 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | ★155.838 | Java Interview & Backend Guide |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | ★150.370 | Claude Code CLAUDE.md (Karpathy) |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | ★139.894 | Offizielle Anthropic Agent Skills |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | ★102.755 | Real Engineers Skills |
| 7 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | ★82.091 | UI/UX Design Intelligence |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | ★79.209 | Cross-Platform Agent Assistant |
| 9 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | ★77.733 | Persistent Context across Sessions |
| 10 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | ★77.613 | Chief Agent Operator |
| 11 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | ★68.256 | Long-Horizon SuperAgent Harness |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | ★64.108 | Token-Reduktion (−65%) für Claude |
| 13 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | ★61.498 | Curated Claude Skills List |
| 14 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | ★59.197 | Best Agent Harness |
| 15 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | ★54.594 | Claude Code Best Practices |

## Agent Skills nach Kategorie

| Kategorie | Repos |
|-----------|------:|
| 🤖 Claude | 1085 |
| ⚡ Codex | 378 |
| ✨ Other AI | 399 |
| 🦞 OpenClaw | 337 |
| 🎯 Cursor | 211 |
| ✦ Gemini | 152 |
| 🚀 Copilot | 133 |
| 🪽 Hermes Agent | 41 |
| 🐋 DeepSeek | 30 |

## Top 5 MCP Server

| Repository | Stars | Beschreibung |
|-----------|------:|-------------|
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | ★87.744 | Curated MCP Server Collection |
| [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | ★58.097 | AI-driven Trend Monitor |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | ★41.438 | Chrome DevTools für Agents |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | ★32.941 | Playwright MCP Server |
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | ★30.118 | GitHub Offizieller MCP Server |

## Top 5 AI Frameworks

| Repository | Stars | Beschreibung |
|-----------|------:|-------------|
| [obra/superpowers](https://github.com/obra/superpowers) | ★204.295 | Agentic Skills Framework |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | ★137.508 | The Agent Engineering Platform |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | ★80.839 | High-Throughput LLM Inference |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | ★79.039 | Multi-Agent Financial Trading |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | ★68.244 | Multi-Agent Software Company |

## Daten aktualisieren (optional)

```bash
# Benötigt: pip install requests  +  GitHub Token
python3 .agents/plugins/agent-leaderboard/scripts/fetch_data.py --token $GITHUB_TOKEN
python3 .agents/plugins/agent-leaderboard/scripts/fetch_mcp.py --token $GITHUB_TOKEN
python3 .agents/plugins/agent-leaderboard/scripts/fetch_frameworks.py --token $GITHUB_TOKEN
python3 .agents/plugins/agent-leaderboard/scripts/fetch_prompts.py --token $GITHUB_TOKEN
python3 .agents/plugins/agent-leaderboard/scripts/fetch_auto_research.py --token $GITHUB_TOKEN
```

## JSON-Struktur

```python
import json

# Agent Skills
d = json.load(open('.agents/plugins/agent-leaderboard/data/data.json'))
# d['meta'] — total, updated_at, min_stars
# d['categories'] — Kategorien mit count
# d['repos'] — Liste aller Repos mit: full_name, stars, description, topics, use_cases

# MCP / Frameworks / Prompts / Auto Research: gleiche Struktur
```

Website: https://agentskills.media | Quelle: https://github.com/jaychempan/Agent-Leaderboard
