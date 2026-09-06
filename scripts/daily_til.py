#!/usr/bin/env python3
"""
Picks the next problem from data/problems.json (round-robin) and appends
a dated entry to TIL.md. Updates data/state.json so tomorrow's run picks
the next one in line.

This does NOT fake work — it assigns you today's problem to solve.
Solve it yourself and commit your actual solution/notes under the entry
whenever you get to it; that's the real, honest part of the streak.
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBLEMS_PATH = os.path.join(ROOT, "data", "problems.json")
STATE_PATH = os.path.join(ROOT, "data", "state.json")
TIL_PATH = os.path.join(ROOT, "TIL.md")


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def main():
    problems = load_json(PROBLEMS_PATH)
    state = load_json(STATE_PATH)

    next_index = (state["last_index"] + 1) % len(problems)
    problem = problems[next_index]
    state["last_index"] = next_index
    save_json(STATE_PATH, state)

    today = date.today().isoformat()
    entry = (
        f"\n## {today} — {problem['topic']}\n"
        f"**Problem:** [{problem['title']}]({problem['link']})\n\n"
        f"- [ ] Solved\n"
        f"- Notes:\n\n"
        f"---\n"
    )

    # Create TIL.md with a header if it doesn't exist yet
    if not os.path.exists(TIL_PATH):
        with open(TIL_PATH, "w") as f:
            f.write("# Today I Learned\n\nDaily DSA/backend practice log.\n---\n")

    with open(TIL_PATH, "a") as f:
        f.write(entry)

    print(f"Added entry for {today}: {problem['title']}")


if __name__ == "__main__":
    main()
