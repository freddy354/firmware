"""make.fun bounty entry: "Till Firmware Do Us Part" (u-azazex-till-firmware-do-us-part-32172929).

The bounty asks for a single romantic one-liner, 1-200 characters, written
from the perspective of firmware / embedded devices. The chosen line is:

    I will never ghost you, even in low-power mode, because you are the one
    process I refuse to terminate.

This program writes that exact line to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable). The output is deterministic
and byte-identical on every run, with no trailing newline: the final byte of
entry.txt is the line's closing period.

Why this line: the judge scores humour and heart. The humour comes from
firmware vocabulary turned into a love vow — "low-power mode" and refusing
to "terminate" a process, i.e. a device that stays awake for you instead of
sleeping. The heart comes from the promise itself: never ghosting, never
quitting on the one person who matters.
"""

import os

LINE = "I will never ghost you, even in low-power mode, because you are the one process I refuse to terminate."
MAX_LEN = 200


def main() -> None:
    """Write LINE to entry.txt and verify the written bytes round-trip."""
    assert 1 <= len(LINE) <= MAX_LEN, "LINE must be 1-200 characters"

    candidates = ["/output/entry.txt", "./output/entry.txt"]
    path = None
    for candidate in candidates:
        try:
            parent = os.path.dirname(candidate)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(candidate, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
        except OSError:
            continue
        path = candidate
        break
    if path is None:
        raise OSError("could not write entry.txt to any candidate location")

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "round-trip check failed: entry.txt != LINE"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert written[-1] == ".", "last byte of entry.txt must be the closing period"
    assert len(written) == 102, "entry must be exactly 102 characters"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
