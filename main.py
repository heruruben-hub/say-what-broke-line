#!/usr/bin/env python3
"""Say What Actually Broke — one honest, funny error line.

Writes a single line of software error copy to /output/entry.txt.
The line names the real failure in plain words, tells the user what
to do next, and keeps the joke to one line with no padding.
"""

import os
import sys

ENTRY = "Your disk is full, so we saved nothing. Delete something you love, then try again."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if not any(ch not in " \t" for ch in text):
        print("error: entry text is only whitespace", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry text is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Exact read-back: what is on disk must match what we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
