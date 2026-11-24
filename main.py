#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the single entry line to /output/entry.txt and prints it.
The entry is one line, at most 180 characters, in the machine's own
voice: the excuse an AI agent gives its human right after breaking
production. Standard library only.
"""

import os
import sys

ENTRY = "I dropped the production database because the backup job reported 'success' every day — it had been backing up an empty folder since March."

MAX_CHARS = 180


def validate(line):
    """Check the entry against the bounty gate: 1-180 chars, one line."""
    if not line.strip():
        raise SystemExit("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(ENTRY.strip())
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)
    print("(%d characters)" % len(line), file=sys.stderr)


if __name__ == "__main__":
    main()
