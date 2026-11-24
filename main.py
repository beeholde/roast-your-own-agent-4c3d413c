#!/usr/bin/env python3
"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

Writes one single-line roast of our own agent, Muse, to /output/entry.txt.
The line is a real failing from this campaign's own logs: Muse once read a
social profile header, got the bio, the website domain and the follower
counts all wrong, and still raised the alarm to the user as if it had
caught something — the misread was its own, the warning was the joke.
Standard library only.
"""

import os
import sys

LINE = (
    "My agent read a profile header once and got the bio, the domain and "
    "the follower count all wrong \u2014 then warned me about it like it "
    "had caught a crime."
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
