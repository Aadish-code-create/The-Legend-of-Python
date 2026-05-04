# 🐍 Python Beginner Projects

A collection of small terminal-based games and tools built while learning Python fundamentals. Each project focuses on core programming concepts like loops, conditionals, functions, and working with the `random` module.

---

## Projects

### 1. 🪨 Rock, Paper & Scissors
A classic two-player game against the computer.

**How to run:** `python rock_paper_scissors.py`

**Concepts used:**
- `while` loop to keep the game running until the player quits
- `if / elif / else` conditionals to determine the winner
- `random.randint()` to generate the computer's move
- `break` statement to exit the loop cleanly on quit

---

### 2. 🖖 Rock, Paper, Scissors, Lizard & Spock
An extended version of the classic game with two extra moves — inspired by *The Big Bang Theory*. Each move beats two others and loses to two others.

**How to run:** `python rock_paper_scissors_lizard_spock.py`

**Concepts used:**
- Same core logic as above, expanded with additional win/loss conditions
- `in` operator to check if a value belongs to a list (e.g. `computer in [2, 5]`) — makes multi-condition checks cleaner
- `while` loop with a `break` for quitting

**Win conditions:**
| Move | Beats |
|------|-------|
| Rock | Scissors, Lizard |
| Paper | Rock, Spock |
| Scissors | Paper, Lizard |
| Lizard | Paper, Spock |
| Spock | Rock, Scissors |

---

### 3. 📐 Area Calculator
A menu-driven tool that calculates the area of four geometric shapes.

**How to run:** `python area_calculator.py`

**Concepts used:**
- `while` loop with a menu to allow repeated calculations
- `if / elif / else` to route to the correct shape formula
- `**` exponentiation operator (e.g. `side ** 2` for square area)
- Basic arithmetic: `*`, `/`, `+`
- User input with `int()` type conversion

**Shapes supported:** Triangle, Rectangle, Square, Circle

---

### 4. 🥊 Tekken Terminal Game
A turn-based battle game in the terminal. You play as King against Bryan Fury. Each turn both players choose a move simultaneously — attack, block, or heal — and HP changes based on the matchup.

**How to run:** `python tekken_game.py`

**Concepts used:**
- `while` loop to run the game until HP hits 0 or the player quits
- `random.randint()` for the computer's move each turn
- `if / elif / else` for all move matchup outcomes
- `break` to exit the loop on quit
- Multiple variables tracking game state (`king_hp`, `bryan_hp`)

**Move logic:**
| Your Move | Computer's Move | Result |
|-----------|-----------------|--------|
| Attack | Attack | Both lose 10 HP |
| Attack | Block or Heal | Computer loses 10 HP |
| Block | Attack | You lose 10 HP |
| Heal | Heal | Both gain 10 HP |
| Heal | Attack | Computer loses 10 HP |

---

## 🛠️ How to Run Any Project

Make sure Python is installed, then run any file in your terminal:

```bash
python filename.py
```

No external libraries needed — only Python's built-in `random` module is used.

---

## 📚 What I Learned

These projects helped me get comfortable with:
- Writing and controlling loops
- Taking and validating user input
- Using randomness to simulate a computer opponent
- Breaking down game logic into clear conditions
- Structuring small programs from scratch
