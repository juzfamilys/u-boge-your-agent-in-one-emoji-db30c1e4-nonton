#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty entry.

Writes a single emoji to /output/entry.txt.

The emoji: U+1F501 CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS.
An AI agent is, at its core, a loop: think, act, observe, repeat — retrying,
self-correcting and iterating until the job is done, at 3am or any hour. The
loop is the one glyph that says how an agent actually works, reads instantly
at any size, and is not the obvious robot.

Pure Python standard library only; no third-party dependencies.
"""

import os
import sys

ENTRY = "\U0001F501"  # 🔁 — the agentic loop
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate check mirroring RULES.txt: UTF-8 text of 1 to 16 characters,
    not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not 1 <= len(text) <= 16:
        raise ValueError(f"entry must be 1-16 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(text)} characters")


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-validate, exactly as the gate would see it.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {OUTPUT_PATH}: {written!r} "
          f"({len(written)} character, {len(written.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
