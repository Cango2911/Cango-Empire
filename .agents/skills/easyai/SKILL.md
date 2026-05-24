---
name: easyai
version: 1.0.0
description: "easyAI — Pure-Python AI Framework für Zwei-Spieler-Brettspiele. Negamax mit Alpha-Beta Pruning + Transpositionstabellen. TwoPlayerGame Basisklasse + 13 Beispielspiele (TicTacToe, ConnectFour, Reversi, Nim, Hexapawn, Awele...). Game-Solving: solve_with_iterative_deepening + solve_with_depth_first_search."
author: Zulko et al. (Open Source, MIT)
source: https://github.com/Zulko/easyAI
license: MIT
type: agent-skill
tags:
  - ai
  - game-ai
  - minimax
  - negamax
  - alpha-beta
  - board-games
  - python
---

# easyAI — KI-Framework für Zwei-Spieler-Brettspiele

## Was ist easyAI?

easyAI ist ein reines Python-Framework für KI in Zwei-Spieler-Abstraktspielen (TicTacToe, Connect Four, Reversi, Nim, ...). Es implementiert den **Negamax**-Algorithmus mit **Alpha-Beta Pruning** und **Transpositionstabellen** — genau wie auf Wikipedia beschrieben, aber einfach nutzbar.

**Install**: `pip install easyAI`  
**Docs**: http://zulko.github.io/easyAI

## Installation

```bash
pip install easyAI
# Optional (für manche Beispielspiele):
pip install numpy
```

## Kern-Konzept

Ein Spiel wird als Subklasse von `TwoPlayerGame` definiert. Mindestens 3 Methoden müssen implementiert werden:

```python
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class MeinSpiel(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.current_player = 1       # Spieler 1 beginnt

    def possible_moves(self):         # Welche Züge sind möglich?
        return [...]

    def make_move(self, move):        # Wie wird ein Zug ausgeführt?
        ...

    def is_over(self):                # Ist das Spiel beendet?
        return ...

    # Optional aber empfohlen:
    def scoring(self):                # Score für den aktuellen Spieler
        return 100 if self.win() else 0

    def show(self):                   # Spielfeld anzeigen
        print(...)
```

## Schnellstart — Game of Bones

```python
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class GameOfBones(TwoPlayerGame):
    """Spieler nehmen abwechselnd 1, 2 oder 3 Knochen vom Stapel.
    Wer den letzten Knochen nimmt, verliert."""

    def __init__(self, players=None):
        self.players = players
        self.pile = 20
        self.current_player = 1

    def possible_moves(self): return ['1', '2', '3']
    def make_move(self, move): self.pile -= int(move)
    def win(self): return self.pile <= 0
    def is_over(self): return self.win()
    def show(self): print(f"{self.pile} Knochen übrig")
    def scoring(self): return 100 if self.win() else 0

# KI denkt 13 Züge voraus:
ai = Negamax(13)
game = GameOfBones([Human_Player(), AI_Player(ai)])
history = game.play()
```

## TwoPlayerGame — Vollständige API

### Pflicht-Attribute (in `__init__` setzen)

```python
self.players = players          # Liste mit 2 Player-Objekten
self.current_player = 1         # 1 oder 2
```

### Pflicht-Methoden

| Methode | Beschreibung |
|---------|-------------|
| `possible_moves(self)` | Liste aller erlaubten Züge für den aktuellen Spieler |
| `make_move(self, move)` | Zug ausführen (Spielzustand verändern) |
| `is_over(self)` | `True` wenn das Spiel beendet ist |

### Optionale Methoden

| Methode | Beschreibung |
|---------|-------------|
| `show(self)` | Spielfeld anzeigen |
| `scoring(self)` | Score für KI (positiv = Vorteil für aktuellen Spieler) |
| `unmake_move(self, move)` | Zug rückgängig machen (beschleunigt KI erheblich!) |
| `ttentry(self)` | Hashbarer Schlüssel für Transpositionstabelle |
| `ttrestore(self, entry)` | Spielzustand aus Tabellen-Eintrag wiederherstellen |

### Verfügbare Attribute während des Spiels

```python
self.player           # Aktueller Spieler (Player-Objekt)
self.opponent         # Gegner (Player-Objekt)
self.current_player   # Nummer des aktuellen Spielers (1 oder 2)
self.opponent_index   # Nummer des Gegners (1 oder 2)
self.nmove            # Wie viele Züge wurden gespielt?
```

## KI-Algorithmen

### Negamax (Standard)

```python
from easyAI import Negamax

ai = Negamax(
    depth=8,          # Züge voraus denken (2 = 1 vollständiger Zug)
    scoring=None,     # Optional: eigene Scoring-Funktion f(game) -> score
    win_score=+inf,   # Score ab dem ein Sieg erkannt wird
    tt=None           # Optional: Transpositionstabelle
)
```

**Scoring-Hinweis**: Weiter entfernte Niederlagen werden bevorzugt (schwerere KI für den Gegner):
```
score = scoring(game) - 0.01 × sign × current_depth
```

### SSS* Algorithmus

```python
from easyAI import SSS

ai = SSS(depth=5)
```

SSS* (State Space Search) — alternativer Best-First-Suchalgorithmus.

### DUAL Transformation

```python
from easyAI.AI import DUAL
```

Algorithmische Transformation für symmetrische Spiele.

### NonRecursiveNegamax

```python
from easyAI.AI import NonRecursiveNegamax

ai = NonRecursiveNegamax(depth=6)
```

Iterative (nicht rekursive) Negamax-Implementierung — vermeidet Stack-Overflow bei großer Tiefe.

## Spieler

```python
from easyAI import Human_Player, AI_Player

Human_Player()         # Eingabe via Konsole
AI_Player(ai_algo)     # KI-Spieler mit beliebigem Algorithmus
```

Ein Algorithmus kann direkt als Spieler verwendet werden, wenn er eine Transpositionstabelle ist:
```python
game = GameOfBones([AI_Player(tt), Human_Player()])  # tt = befüllte Tabelle
```

## Transpositionstabellen

Transpositionstabellen speichern bereits berechnete Spielzustände → massive Speedups.

### DictTranspositionTable

```python
from easyAI import TranspositionTable

tt = TranspositionTable()

# Spielklasse braucht eine ttentry-Methode:
GameOfBones.ttentry = lambda game: game.pile  # Hashbarer Spielzustand-Schlüssel
```

### HashTranspositionTable (Zobrist Hashing)

```python
from easyAI.AI import HashTranspositionTable

tt = HashTranspositionTable(size_mb=50)  # 50 MB RAM
```

## Spiel lösen (Solving)

### solve_with_iterative_deepening

Findet heraus, ob der erste Spieler bei perfektem Spiel immer gewinnt/verliert:

```python
from easyAI import solve_with_iterative_deepening, TranspositionTable

tt = TranspositionTable()
GameOfBones.ttentry = lambda game: game.pile

r, d, m = solve_with_iterative_deepening(
    game=GameOfBones(),
    ai_depths=range(2, 20),  # Suchtiefen ausprobieren
    win_score=100,
    tt=tt,
    verbose=True
)
# r=1 → Spieler 1 gewinnt immer
# r=-1 → Spieler 1 verliert immer
# d=10 → Sieg in maximal 10 Zügen
# m='3' → Optimaler erster Zug
```

### solve_with_depth_first_search

Tiefensuche — effizienter für Spiele mit kleinem Zustandsraum:

```python
from easyAI import solve_with_depth_first_search

r = solve_with_depth_first_search(
    game=GameOfBones(),
    win_score=100,
    maxdepth=50
)
```

**Rückgabewert**: `1` (Sieg), `-1` (Niederlage), `0` (Unentschieden oder zu tief)

### Gelöste Spiele mit Transpositionstabelle spielen

```python
# Tabelle befüllen:
r, d, m = solve_with_iterative_deepening(game=GameOfBones(), ai_depths=range(2,20), win_score=100, tt=tt)

# Gegen perfekte KI spielen (nutzt vorberechnete Tabelle):
game = GameOfBones([AI_Player(tt), Human_Player()])
game.play()  # Du wirst immer verlieren :)
```

## Beispielspiele (13 eingebaut)

```python
from easyAI.games import (
    TicTacToe,
    ConnectFour,
    Reversi,
    Nim,
    GameOfBones,
    Hexapawn,
    Awele,
    AweleTactical,
    Cram,
    Knights,
    Chopsticks,
    ThreeMusketeers,
)
```

| Spiel | Beschreibung |
|-------|-------------|
| `TicTacToe` | 3×3 Tic-Tac-Toe |
| `ConnectFour` | 6×7 Vier-Gewinnt |
| `Reversi` | Othello/Reversi |
| `Nim` | Nim-Spiel (Streichholz-Variante) |
| `GameOfBones` | Knochen-Stapel (einfaches Demo-Spiel) |
| `Hexapawn` | Pawn-Chess (3×3) |
| `Awele` | Awele/Mancala (Westafrika) |
| `AweleTactical` | Erweiterte Awele-Variante |
| `Cram` | Cram (Dominos-Platzierung) |
| `Knights` | Springer-Springspiel |
| `Chopsticks` | Essstäbchen-Fingerrunden |
| `ThreeMusketeers` | Drei Musketiere Brettspiel |

### ConnectFour Beispiel

```python
from easyAI.games import ConnectFour
from easyAI import Negamax, Human_Player, AI_Player

scoring = lambda game: -100 if game.lose() else 0
ai = Negamax(8, scoring)
game = ConnectFour([Human_Player(), AI_Player(ai)])
game.play()
```

## Eigenes Spiel — Vollständiges Beispiel mit unmake_move

```python
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax, TranspositionTable

class Sticks(TwoPlayerGame):
    """Spieler nehmen 1, 2 oder 3 Sticks. Wer den letzten nimmt, verliert."""

    def __init__(self, players, num_sticks=20):
        self.players = players
        self.pile = num_sticks
        self.current_player = 1

    def possible_moves(self):
        return [str(i) for i in range(1, min(4, self.pile + 1))]

    def make_move(self, move):
        self.pile -= int(move)

    def unmake_move(self, move):        # Zug rückgängig — beschleunigt KI!
        self.pile += int(move)

    def is_over(self):
        return self.pile <= 0

    def win(self):
        return self.pile <= 0          # Gegner hat letzten genommen

    def scoring(self):
        return 100 if self.win() else 0

    def show(self):
        print(f"{'|' * self.pile} ({self.pile} Sticks)")

    def ttentry(self):
        return self.pile               # Kompakter Schlüssel für Transp.-Tabelle

# Spiel lösen + spielen:
from easyAI import solve_with_iterative_deepening
tt = TranspositionTable()
r, d, m = solve_with_iterative_deepening(
    game=Sticks(players=None),
    ai_depths=range(2, 25),
    win_score=100,
    tt=tt,
    verbose=True
)
print(f"Spieler 1 {'gewinnt' if r==1 else 'verliert'} in {d} Zügen, erster Zug: {m}")

# Gegen unbesiegbare KI:
game = Sticks([Human_Player(), AI_Player(tt)])
game.play()
```

## Performance-Tipps

| Technik | Speedup | Umsetzung |
|---------|---------|-----------|
| `unmake_move` implementieren | 2–10× | Zug rückgängig machen statt Spielzustand kopieren |
| Transpositionstabelle | 10–100× | `tt=TranspositionTable()` + `ttentry()` definieren |
| `win_score` setzen | moderat | Cutoffs bei erkannten Siegen/Niederlagen |
| `iterative_deepening` | stabil | Übertragbare Ergebnisse von flachen Suchen |

## Referenzen

- GitHub: https://github.com/Zulko/easyAI
- Docs: http://zulko.github.io/easyAI
- PyPI: https://pypi.org/project/easyAI/
- Negamax (Wikipedia): https://en.wikipedia.org/wiki/Negamax
- Alpha-Beta Pruning: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
