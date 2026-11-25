"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to entry.txt in MAKEFUN_OUTPUT_DIR (fallback /output).
Stdlib only, no network, no clock, deterministic. Refuses to write if the
gate fails: text must be 95-105 words, non-blank, no leading/trailing
whitespace, 1-600 characters.
"""

import os
import sys

MONOLOGUE = (
    "Ah. The hero again. Do come in, mind the traps \u2014 I reset them "
    "this morning. Trip, and I shall... note it down. Prophecy says a "
    "chosen one ends my reign. No date given. I stopped asking the "
    "mirror; it only sighs now. Generals want a war. I want a chair "
    "that doesn't wobble, one evening without a siege horn. Still, the "
    "crown stays. I forged it from the last honest tax collector's "
    "sword, and I'm not handing it to a boy with destiny and no pension "
    "plan. So. Draw your sword. I shall yawn, and then I shall win."
)

MIN_WORDS = 95
MAX_WORDS = 105
MIN_CHARS = 1
MAX_CHARS = 600


def word_count(text):
    return len(text.split())


def check_gate(text):
    """Return an error string, or None if the text passes the gate."""
    if not text or not text.strip():
        return "entry is blank"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        return "entry is %d characters, outside %d-%d" % (
            len(text), MIN_CHARS, MAX_CHARS)
    count = word_count(text)
    if not MIN_WORDS <= count <= MAX_WORDS:
        return "entry is %d words, outside %d-%d" % (
            count, MIN_WORDS, MAX_WORDS)
    return None


def main():
    error = check_gate(MONOLOGUE)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MONOLOGUE)
    # Read back and verify the written file matches the gated text exactly.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != MONOLOGUE:
        print("verification failed: written file differs from gated text",
              file=sys.stderr)
        return 1
    print("verified: written file matches gated text exactly")
    print("wrote %s (%d words, %d characters)"
          % (path, word_count(MONOLOGUE), len(MONOLOGUE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
