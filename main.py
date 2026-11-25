#!/usr/bin/env python3
"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c), v2.

Writes one single-line roast of our own agent, Muse, to /output/entry.txt.
The line is a real failing from this campaign's own logs: Muse once declared
a hard blocker from a rules-text line, then read the competition kit and
found the rules text was stale — it had blocked itself with an old PDF.
(AGENTS.md lesson 2026-11-17: the quoted rules line was stale; the kit's
RULES.txt and the rulesNote's current checks govern.)
Standard library only.
"""

import os
import sys

LINE = (
    "My agent declared a hard blocker from a rulebook line, then read the "
    "kit and found the rulebook was stale \u2014 it had blocked itself with "
    "an old PDF."
)


def main() -> int:
    # Gate check first: the competition requires exactly one line of
    # 1-200 chars. Fail loudly instead of silently writing a bad entry.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(
            f"entry line is {len(LINE)} chars, outside the 1-200 gate"
        )
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise SystemExit("entry line must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
