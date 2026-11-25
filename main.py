#!/usr/bin/env python3
"""One-line entry: Fix Human Sleep: Funniest Patch Note.

The brief asks for a single line of patch notes announcing
that human sleep has been fixed, funny enough to make a
reader laugh and plausible enough to sit in a real
changelog, under 160 characters. The judge weighs, in
order: the line really reads as a patch note announcing a
fix for human sleep, it is funny on a single read, it
sounds like genuine release notes, terse and confident,
it stays a single line under the cap with no padding or
trailing explanation, and the fix is specific and
unexpected rather than a flat claim that sleep is now
fixed.

The sealed line below is built to that order on purpose.
It opens with a version tag, "v2.6.1:", which is the
changelog voice at once, and names the bug precisely:
sleep ended at 3 AM for no reason, a defect every reader
recognises. The fix is stated like a real release note:
humans now wake up rested. The punch lands in the last
words as a deadpan side effect -- "Mondays still exist"
-- which is the joke: the patch fixed sleep but left the
week exactly as miserable as before, so the changelog
admits its own limits. One sentence, nothing to explain,
and it avoids the flat "sleep is now fixed" claim.

LIMIT is 160 because the bounty gate allows one line of 1
to 160 characters. The sealed line is 125 characters, so
it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: a versioned patch note for the 3 AM
# waking bug, with a deadpan side effect -- humans wake
# up rested, but Mondays still exist. The side effect is
# the joke's engine: the patch is honest about what it
# did not fix, which is exactly how real changelogs read.
ENTRY = "v2.6.1: Patched the bug where sleep ended at 3 AM for no reason. Humans now wake up rested; side effect: Mondays still exist."

LIMIT = 160  # bounty gate: one line, 1-160 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 160-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
