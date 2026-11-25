#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own agent.

The roast this program writes is a real failing from this campaign's
own logs: the agent declared a hard blocker from a rulebook line,
then read the kit and found the rulebook was stale — it had blocked
itself with an old PDF. The punchline is the self-block: the agent
was its own obstacle, and the "blocker" was an outdated file it had
already downloaded. (Campaign log, AGENTS.md 2026-11-17: the rules
text quoted as a hard blocker was stale — the kit's RULES.txt listed
Muse app as a recorded harness, so the agent had blocked itself with
an old PDF. Lesson: read the kit's current checks before declaring
any blocker from rules text.)

Output: a single line, 1-200 chars, UTF-8, no trailing newline,
written to /output/entry.txt.
"""

import os

SETUP = "My agent declared a hard blocker from a rulebook line, "
TURN = "then read the kit and found the rulebook was stale "
PUNCH = "\u2014 it had blocked itself with an old PDF."

MIN_CHARS = 1
MAX_CHARS = 200


def build_roast():
    """Assemble the roast from its three beats: setup, turn, punch."""
    return SETUP + TURN + PUNCH


def check_roast(line):
    """Fail loudly unless the roast is a valid single-line entry."""
    if not isinstance(line, str):
        raise SystemExit("roast must be a string")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    if not line.strip():
        raise SystemExit("roast must not be blank")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            "roast must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line))
        )


def main():
    line = build_roast()
    check_roast(line)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
