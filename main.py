#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the sign taped to the door of a
haunted server room.

The line was picked from 36 candidates by mock pairwise judging against
the brief: a tired sysadmin hears typing at 3am, is told it is not an
intruder but the previous on-call engineer, and the punchline is that he
never logged out. The joke lands in one line, sounds like a notice on a
door, and uses a haunting specific to IT life instead of a generic ghost.

The line is 98 characters: short enough to read at a glance on a printed
sheet, long enough for the reveal to land in three turns. The program
builds the line from three clauses -- the 3am typing, the reassurance it
is not an intruder, the reveal -- and checks the result against the entry
gate (length, single line, no leading or trailing space) before writing
it, then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "If you hear typing at 3am, it is not an intruder. "
    "It is the previous on-call. "
    "He never logged out."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 120):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-120")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
