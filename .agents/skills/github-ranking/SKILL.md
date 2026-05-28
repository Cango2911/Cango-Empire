---
name: github-ranking
version: 1.0.0
description: GitHub Ranking — Top 100 meistgestarrete und geforkte Repositories nach Sprache (EvanLi, täglich auto-aktualisiert)
author: EvanLi
source: https://github.com/EvanLi/Github-Ranking
license: MIT
tags: [github, ranking, stars, forks, trending, statistics, open-source]
platforms: [claude-code, cursor, codex, gemini-cli, copilot, opencode, windsurf]
---

# GitHub Ranking Skill

Tägliche Auto-Updates der meistgestarteten und geforteten GitHub-Repositories weltweit. Abdeckt 34 Programmiersprachen + Gesamt-Rankings.

## Was dieser Skill bietet

- **Top 100 Stars** — Die 100 meistgestarteten Repos aller Sprachen
- **Top 100 Forks** — Die 100 meistgeforteten Repos aller Sprachen
- **34 Sprachen-Rankings**: ActionScript, C, C#, C++, Clojure, CoffeeScript, CSS, Dart, DM, Elixir, Go, Groovy, Haskell, HTML, Java, JavaScript, Julia, Kotlin, Lua, MATLAB, Objective-C, Perl, PHP, PowerShell, Python, R, Ruby, Rust, Scala, Shell, Swift, TeX, TypeScript, Vim script

## Nutzung

```
# Top 100 gesamte Stars ansehen
cat Top100/Top-100-stars.md

# Top 100 Python-Repos
cat Top100/Python.md

# Top 100 JavaScript-Repos
cat Top100/JavaScript.md

# Top 100 Rust-Repos
cat Top100/Rust.md
```

## Datenfelder

Jede Ranking-Tabelle enthält: Rang, Projektname (Link), Stars, Forks, Sprache, Open Issues, Beschreibung, Letzter Commit

## Daten aktualisieren (GitHub GraphQL API)

```bash
pip install -r requirements.txt
# GitHub Access Token in ../access_token.txt speichern
cd source && python process.py
```

## Unterstützte Sprachen (Top100/)

| Datei | Beschreibung |
|-------|-------------|
| Top-100-stars.md | Alle Sprachen nach Stars |
| Top-100-forks.md | Alle Sprachen nach Forks |
| Python.md | Top Python-Repos |
| JavaScript.md | Top JS-Repos |
| TypeScript.md | Top TS-Repos |
| Go.md | Top Go-Repos |
| Rust.md | Top Rust-Repos |
| Java.md | Top Java-Repos |
| C.md | Top C-Repos |
| CPP.md | Top C++-Repos |
| CSharp.md | Top C#-Repos |
| ...und 25 weitere Sprachen | |
