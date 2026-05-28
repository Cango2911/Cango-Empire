# Cango-Empire — Claude Code Konfiguration

## Sprache
Immer auf **Deutsch** antworten.

## Agent Skills — Auto-Aktivierung

Diese 1.175+ Agent Skills sind in `.agents/skills/` verfügbar. Setze sie **immer automatisch** ein, wenn die Aufgabe es erfordert:

### Video & Media (`.claude/skills/`)
| Trigger | Skill |
|---------|-------|
| Video generieren, Cinematic | `higgsfield`, `higgsfield-cinema`, `01-cinematic` |
| Viral Hook, Social Media Video | `01-viral-hook`, `11-social-hook`, `social-media-video` |
| Produktvideo, Ad | `product-ad-cinematic`, `07-ecommerce-ad`, `product-video-ad-maker` |
| UGC Content | `ugc-video-auto`, `ugc-video-factory`, `ugc-ads-workflow` |
| Logo, Brand | `logo-creator`, `brand-kit`, `logo-branding` |
| Seedance, KI-Video | `seedance-2`, `seedance-auto-generate` |
| YouTube | `youtube-thumbnail`, `youtube-shorts` |
| Innendesign | `interior-design`, `interior-design-visualizer` |

### Entwicklung & Code
| Trigger | Skill |
|---------|-------|
| Code Review | `/code-review` |
| PR erstellen | `/create-pr` |
| Tests schreiben | `/create-app-e2e-test` |
| AWS, Cloud | `.agents/skills/aws-skills` |
| Cloudflare | `.agents/skills/cloudflare-skill` |
| n8n Automation | `.agents/skills/n8n-skills` |
| Playwright Testing | `.agents/skills/playwright-skill` |
| iOS Simulator | `.agents/skills/ios-simulator-skill` |
| D3.js Visualisierung | `.agents/skills/d3js-claude-skill` |

### Security & Pentesting
| Trigger | Skill |
|---------|-------|
| Security Review | `awesome-skills-security`, `security-investigator` |
| Bug Bounty | `claude-bug-bounty`, `bug-hunter-skill` |
| Web3 Security | `llm-sast-scanner`, `awesome-web3-security` |
| Smart Contract Audit | `solidity-auditor-skills`, `move-auditor-skills`, `ton-auditor-skills` |
| Reverse Engineering | `ghidra-re-skill`, `android-reverse-engineering-skill` |
| Fuzzing | `ffuf-claude-skill` |
| Android Pentesting | `android-pentesting-skill` |
| Cybersecurity Allgemein | `anthropic-cybersecurity-skills`, `yaklang-hack-skills` |

### Web3 & Blockchain
| Trigger | Skill |
|---------|-------|
| Solana | `solana-dev-skill`, `jup-agent-skills`, `solana-auditor-skills` |
| Ethereum, Solidity | `openzeppelin-skills`, `solidity-auditor-skills` |
| Coinbase, Wallet | `coinbase-wallet-skills` |
| BNB Chain | `bnbchain-skills` |
| TON | `ton-auditor-skills` |
| Move Language | `move-auditor-skills` |

### Marketing & Content
| Trigger | Skill |
|---------|-------|
| Marketing Skills | `awesome-skills-marketing`, `coreyhaines-marketing-skills` |
| Content humanisieren | `humanizer-skill`, `humanizer-zh-skill`, `stop-slop-skill` |
| Prompts | `aj-useful-ai-prompts` |
| Social Media | `instagram-post`, `rednote-cover` |

### Produktivität & Tools
| Trigger | Skill |
|---------|-------|
| Obsidian Plugin | `obsidian-plugin-skill` |
| Linear | `linear-claude-skill` |
| Spotify | `spotify-skill` |
| NotebookLM | `notebooklm-skill` |
| RevealJS Präsentation | `revealjs-skill` |
| EPUB | `epub-skill` |
| Browser Automation | `skyvern-skill` |

### AI & Research
| Trigger | Skill |
|---------|-------|
| KI-Agent Skills | `awesome-skills-ai-llm`, `hoodini-ai-skills` |
| Karpathy/ML | `karpathy-skills` |
| Skill Creator | `skill-creator` |
| SkillX Marketplace | `skillx` |

## Skill-Nutzungs-Regeln

1. **Erkenne die Aufgabe** → Wähle den passenden Skill aus obiger Tabelle
2. **Skill-Datei lesen** → `.agents/skills/<name>/SKILL.md` für Kontext
3. **Automatisch anwenden** — nicht erst fragen
4. **Mehrere Skills kombinieren** wenn die Aufgabe es erfordert

## Verfügbare Skill-Kategorien (`.agents/skills/`)

```
Security:    anthropic-cybersecurity-skills, bug-hunter-skill, claude-bug-bounty,
             ffuf-claude-skill, ghidra-re-skill, llm-sast-scanner,
             security-investigator, vibesec-skill, web3-bug-bounty-skills,
             yaklang-hack-skills, android-pentesting-skill, awesome-ai-security,
             awesome-game-security, awesome-web3-security

Web3:        bnbchain-skills, coinbase-wallet-skills, jup-agent-skills,
             move-auditor-skills, openzeppelin-skills, solana-auditor-skills,
             solidity-auditor-skills, ton-auditor-skills, solana-dev-skill

Dev Tools:   aws-skills, cloudflare-skill, playwright-skill, ios-simulator-skill,
             obsidian-plugin-skill, linear-claude-skill, n8n-skills, skyvern-skill,
             webgpu-claude-skill, d3js-claude-skill, unity-skills

Content:     humanizer-skill, humanizer-zh-skill, stop-slop-skill, epub-skill,
             revealjs-skill, spotify-skill, notebooklm-skill

Community:   aj-useful-ai-prompts, antigravity-skills, borghei-claude-skills,
             claude-skills-marketplace, day1global-skills, founder-skills,
             hegelian-dialectic-skill, hoodini-ai-skills, interface-design-skill,
             karpathy-skills, karanb-claude-skills, obra-superpowers, pm-skills-phuryn,
             remotion-skills, skills-best-practices

Platforms:   goclaw (Go AI Platform), skillx (Marketplace)
Research:    build-your-own-x, github-ranking
```

## Wichtige Regeln

- **Sicherheitscheck** vor jeder Skill-Installation: eval(), shell=True, os.system() mit vars → SKIP
- `subprocess` mit Liste → SICHER
- **Niemals** `.claude/settings.json` oder `.claude/settings.local.json` aus externen Repos kopieren
- Binärdateien nicht kopieren: .png, .jpg, .gif, .webp, .ttf, .mp4, .bin, .pyc
- API-Keys in .env.example → kopieren (Policy: alle API-Keys mitspeichern)
