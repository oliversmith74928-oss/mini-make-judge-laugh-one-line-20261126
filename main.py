#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — make.fun entry.

Writes a single funny line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only. Deterministic: identical bytes on every run.
Writes only to $MAKEFUN_OUTPUT_DIR (default /output), never to the repo dir.
"""
import os

ENTRY = (
    "I asked my GPS for the meaning of life and it said, "
    "'Recalculating,' which is the most honest answer anyone's ever given me."
)
# Single line, 124 characters: setup (GPS + meaning of life) then the
# punchline lands at the end with no explanation afterwards.


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
