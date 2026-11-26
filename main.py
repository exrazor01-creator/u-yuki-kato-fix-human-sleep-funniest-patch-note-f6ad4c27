#!/usr/bin/env python3
"""One-line entry: Fix Human Sleep: Funniest Patch Note.

The brief asks for one changelog line that fixes human
sleep and makes the reader laugh: funny at first glance,
plausible enough to pass as a real release note, and a
single line of 1 to 160 characters. The judge scores
entries head to head, weighing first that the line
really is a patch note about fixing human sleep, then
how funny it is, then how much it reads like a genuine
changelog, and finally that it stays on one line.

The sealed line below picks a sleep bug nobody else
reaches for: instead of the tired 3 AM waking joke, it
treats dreaming as a video stream. REM sleep "buffered
forever", the way a clip stalls on a bad connection.
The fix is written in straight release-note voice --
humans now dream in full HD -- and the laugh comes from
the deadpan side effect: naps now need a reboot to
resume. That last clause does the heavy lifting: the
patch upgraded the night but left the afternoon nap
broken in a very software-shaped way, and the changelog
admits it without flinching. A version tag opens the
line, so the changelog voice is present from the first
word, and the whole thing is one compact sentence with
no padding and no explanation tacked on after it.

LIMIT is 160 because the bounty gate allows one line of
1 to 160 characters. The sealed line is 131 characters,
so it sits comfortably inside the cap; the validator
below only guards against an edit that would push it
past the limit.
"""

import os

# The sealed line: a versioned patch note for the REM
# buffering bug, with a deadpan side effect -- dreams
# now render in full HD, but naps need a reboot to
# resume. The joke is that the fix upgraded sleep like
# a video stream while leaving the nap broken in a
# very software-shaped way.
ENTRY = "v2.7.0: Fixed the bug where REM sleep buffered forever. Humans now dream in full HD; side effect: naps now need a reboot to resume."

LIMIT = 160  # bounty gate: one line, 1-160 characters


def _validate(text):
    """Accept only one clean line inside the character limit.

    Checks run from the most basic to the most specific:
    type first, then shape (one line, plain spacing), then
    the content rules (printable ASCII, no padding, no
    double spaces), and the length cap last, since a line
    that fails an earlier check is rejected regardless of
    how long it is.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    # Whitespace rule, stated once: only the plain space
    # separates words. Tabs, non-breaking spaces and other
    # invisible characters would hide bytes in the line.
    if any(ch.isspace() and ch != " " for ch in text):
        raise ValueError("entry must use plain spaces only")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 160-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    return text


def main():
    entry = _validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
