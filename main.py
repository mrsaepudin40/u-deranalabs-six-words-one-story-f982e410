#!/usr/bin/env python3
"""Six Words, One Story: write one complete original story in exactly six words."""

import os

# One scene, one turn: she leaves for good, and he only watches -
# no plea, no chase, no stop. The whole life they shared, and why
# it ended, is left in the gap between the two sentences.
STORY = "She packed one bag. He watched."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
