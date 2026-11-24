"""One Letter: Coffee or Tea.

The whole entry is a single letter: A stands for coffee, B stands
for tea. This program takes its side and writes that one letter,
and nothing else, to entry.txt in the output directory.
"""

import os

# The answer: B, for tea. Tea is the truer cup here -- the one that
# slows the morning down instead of shouting at it, and the one
# worth choosing when only a single letter is allowed to speak.
LETTER = "B"

DEFAULT_OUTPUT_DIR = "/output"


def output_dir():
    """Return the directory the entry file belongs in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)


def write_entry(directory):
    """Write the single letter to entry.txt inside directory.

    The file holds the letter and nothing else: no word, no
    explanation, no punctuation, not even a trailing newline, so
    the entry is exactly one character long.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    return path


def main():
    # Guard the gate: the entry must be exactly one character,
    # either A (coffee) or B (tea), and never blank.
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        raise ValueError("entry must be exactly one letter: A or B")
    write_entry(output_dir())


if __name__ == "__main__":
    main()
