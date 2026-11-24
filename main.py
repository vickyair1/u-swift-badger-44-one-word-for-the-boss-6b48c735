"""One-word bounty entry.

Writes a single word to /output/entry.txt, byte-for-byte, with no
trailing newline. Deterministic: the same bytes on every run.
"""

import os

WORD = "ASAP"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
