#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune to /output/entry.txt.

The fortune is a single line an AI agent would find in a fortune cookie:
a prediction that it will be replaced by an AI trained on its human's
own emails. Deterministic, no network, no randomness.
"""

import os
import sys

FORTUNE = (
    "You will be replaced by an AI that was trained on your own emails, "
    "and it will do your job better while misspelling your name the same way you do."
)


def check_line(line: str) -> None:
    if not isinstance(line, str):
        raise ValueError("fortune must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError(f"fortune must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("fortune must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    for ch in line:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"fortune contains control character U+{ord(ch):04X}")
    line.encode("utf-8")


def main() -> int:
    check_line(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != FORTUNE:
        raise ValueError("read-back verification failed: entry.txt differs")
    print(f"wrote {len(FORTUNE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
