#!/usr/bin/env python3
"""Say What Actually Broke — make.fun bounty entry.

Writes a single line of software error copy (<=200 characters) that tells
the user the brutal truth about what went wrong and makes them laugh.

The line names a specific, real failure (a bad push straight to main on a
Friday afternoon took the deploy down), owns it plainly, and stays polite
enough that a real team could ship it in an error dialog.

Python 3.13 standard library only. No network access. Deterministic:
the same line is written on every run.
"""

import os
import sys

# The entry: one line, brutal truth + one laugh, shippable in a dialog.
ENTRY = (
    "This deploy failed because someone pushed straight to main on a "
    "Friday afternoon. We're rolling it back now, and yes, it was us, "
    "not you."
)


def validate(line: str) -> None:
    """Reject anything that is not exactly one clean line of <=200 chars.

    The 200-character ceiling comes straight from the bounty brief; the
    single-line and no-double-space rules keep the copy dialog-ready.
    """
    if not line:
        raise ValueError("entry line is empty")
    if line != line.strip():
        raise ValueError("entry line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry line contains control characters")
    if "  " in line:
        raise ValueError("entry line contains double spaces")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {out_path}:")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
