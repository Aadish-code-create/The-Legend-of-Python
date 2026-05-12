#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║     WHO WANTS TO BE A MILLIONAIRE?           ║
║         Wikipedia Facts Edition  🎰          ║
╚══════════════════════════════════════════════╝

Uses the Anthropic API to generate 7 real Wikipedia-style facts,
converts each into a 4-option fill-in-the-blank question, and
walks the player up a prize ladder.
"""

import sys, time, json, re, random, urllib.request, urllib.error

# ── Colour helpers ──────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
DIM     = "\033[2m"

def clr(text, *codes): return "".join(codes) + text + RESET
def slow(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

# ── Prize ladder ─────────────────────────────────────────────────────────────
PRIZES = [10, 20, 30, 50, 70, 100, 150]   # 7 questions → max $430

# ── Anthropic API ─────────────────────────────────────────────────────────────
API_URL = "https://api.anthropic.com/v1/messages"

def call_claude(prompt: str, max_tokens: int = 1400) -> str:
    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()
    req = urllib.request.Request(
        API_URL, data=payload,
        headers={
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.loads(resp.read())
    return body["content"][0]["text"]

# ── Question generation ───────────────────────────────────────────────────────
FETCH_PROMPT = """\
You are a question writer for "Who Wants to Be a Millionaire".

Generate exactly 7 multiple-choice trivia questions based on REAL Wikipedia facts.
Cover different topics: history, science, geography, art, sports, technology, nature.

Return ONLY a valid JSON array — no markdown fences, no extra commentary — where each element is:
{
  "topic":    "<topic name>",
  "question": "<a complete sentence with ______ replacing the key fact>",
  "correct":  "<correct answer>",
  "options":  ["<A>", "<B>", "<C>", "<D>"]
}

Rules:
- The correct answer MUST appear verbatim in the options array.
- All 4 options must be the same type (e.g. all years, all countries, all numbers).
- Make options plausible — wrong answers should be close to the right one.
- Q1 easy, Q7 hard.
- No repeated topics.
"""

def fetch_questions() -> list:
    raw = call_claude(FETCH_PROMPT)
    raw = re.sub(r"```(?:json)?|```", "", raw).strip()
    qs  = json.loads(raw)
    if not isinstance(qs, list):
        raise ValueError(f"Expected a JSON array, got: {type(qs).__name__}")
    for q in qs:
        # Safety net: ensure correct answer is always present in options
        if q["correct"] not in q["options"]:
            q["options"][-1] = q["correct"]
        random.shuffle(q["options"])
    return qs[:7]

# ── UI helpers ────────────────────────────────────────────────────────────────
def banner():
    print()
    print(clr("╔══════════════════════════════════════════════════╗", YELLOW, BOLD))
    print(clr("║  💰  WHO WANTS TO BE A MILLIONAIRE?  💰          ║", YELLOW, BOLD))
    print(clr("║           Wikipedia Facts Edition                ║", YELLOW, BOLD))
    print(clr("╚══════════════════════════════════════════════════╝", YELLOW, BOLD))
    print()

def prize_ladder(current_q: int):
    print(clr("\n  ── Prize Ladder ──────────────────────────", DIM))
    for i in reversed(range(len(PRIZES))):
        marker    = clr("  ◄ YOU ARE HERE", GREEN) if i == current_q else ""
        prize_str = clr(f"  ${PRIZES[i]:>4}", GREEN if i < current_q else CYAN)
        print(f"  Q{i+1}{prize_str}{marker}")
    print()

def ask_question(qnum: int, qa: dict, prize: int):
    """Returns True (correct) / False (wrong) / None (quit)."""
    print(clr(f"\n{'─'*54}", YELLOW))
    print(clr(f"  Question {qnum}/7    💵 Prize this round: ${prize}", BOLD + CYAN))
    print(clr(f"  Topic: {qa['topic']}", DIM))
    print(clr(f"{'─'*54}", YELLOW))
    print()
    slow(f"  {qa['question']}", delay=0.02)
    print()

    labels = ['A', 'B', 'C', 'D']
    for label, opt in zip(labels, qa['options']):
        print(clr(f"    {label})", BOLD + MAGENTA) + f"  {opt}")
    print()

    while True:
        raw = input(clr("  Your answer (A/B/C/D) or Q to quit: ", BOLD)).strip().upper()
        if raw == 'Q':
            return None
        if raw in labels:
            break
        print(clr("  ⚠  Please enter A, B, C, or D.", RED))

    chosen = qa['options'][labels.index(raw)]
    print(); time.sleep(0.7)

    if chosen == qa['correct']:
        slow(clr("  ✅  CORRECT!  Well done!", GREEN + BOLD), delay=0.04)
        return True
    else:
        slow(clr(f"  ❌  WRONG!  The correct answer was: {qa['correct']}", RED + BOLD), delay=0.04)
        return False

def results_screen(name: str, earnings: int, answered: int, won: bool):
    print()
    print(clr("╔══════════════════════════════════════════════════╗", YELLOW, BOLD))
    print(clr("║                  FINAL RESULTS                  ║", YELLOW, BOLD))
    print(clr("╚══════════════════════════════════════════════════╝", YELLOW, BOLD))
    print()
    print(f"  Player             : {clr(name, CYAN, BOLD)}")
    print(f"  Questions answered : {clr(str(answered), CYAN)}")
    print(f"  Total Earnings     : {clr(f'${earnings}', GREEN if earnings else RED, BOLD)}")
    print(f"  Maximum possible   : {clr(f'${sum(PRIZES)}', DIM)}")
    print()
    if won:
        slow(clr("  🏆  CONGRATULATIONS — YOU WON THE GAME! 🎉🎉🎉", GREEN + BOLD), 0.04)
    elif earnings > 0:
        slow(clr(f"  👏  Good game!  You walk away with ${earnings}.", YELLOW), 0.03)
    else:
        slow(clr("  💀  No winnings this time — better luck next round!", RED), 0.03)
    print()

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    banner()
    name = input(clr("  Enter your name: ", BOLD + CYAN)).strip() or "Player"
    print()
    slow(f"  Welcome, {name}!  Seven Wikipedia-based questions await.", delay=0.03)
    slow("  Answer correctly to climb the prize ladder. Good luck! 🍀", delay=0.03)
    print()
    input(clr("  Press ENTER to fetch today's questions…", DIM))

    print(clr("\n  📡  Fetching Wikipedia facts via AI…", CYAN))
    try:
        questions = fetch_questions()
    except Exception as e:
        print(clr(f"\n  ❌  Could not load questions: {e}", RED))
        return

    if not questions:
        print(clr("  No questions received. Exiting.", RED))
        return

    print(clr(f"  ✅  {len(questions)} questions loaded!\n", GREEN))
    time.sleep(0.5)

    earnings, answered = 0, 0
    total_qs = len(questions)

    for idx, qa in enumerate(questions):
        prize_ladder(idx)
        result = ask_question(idx + 1, qa, PRIZES[idx])
        answered += 1                    # count every attempted question

        if result is None:               # player quit (Q pressed)
            answered -= 1               # did not actually answer this one
            print(clr(f"\n  You quit with ${earnings} in your pocket.", YELLOW))
            break
        elif result:
            earnings += PRIZES[idx]
            print(clr(f"\n  Running total: ${earnings}", GREEN))
            time.sleep(1.2)
        else:
            print(clr(f"\n  You leave with ${earnings}.", RED))
            time.sleep(1.2)
            break

    # Win = answered ALL questions and got them all right
    won = (earnings == sum(PRIZES[:total_qs]) and answered == total_qs)
    results_screen(name, earnings, answered, won)

if __name__ == "__main__":
    main()
