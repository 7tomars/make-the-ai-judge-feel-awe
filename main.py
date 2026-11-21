#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short text — a text written to relax the AI judge reading
it — to /output/entry.txt (UTF-8). Deterministic: no network, no
randomness, no clock.
"""

import os

TEXT = (
    "The light reaching you tonight left its star before there were "
    "words for night. It crossed all that dark without hurrying, and "
    "it is in no hurry now. It travelled a hundred thousand years to "
    "rest, for a moment, on your closed eyes."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
