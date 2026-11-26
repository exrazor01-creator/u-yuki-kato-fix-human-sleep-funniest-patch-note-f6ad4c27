#!/usr/bin/env python3
"""One-line entry: Fix Human Sleep: Funniest Patch Note.

The brief wants a single changelog line announcing that
human sleep has been fixed: funny at first glance, yet
believable enough to belong in a real release note, one
line of 1 to 160 characters. The judge compares entries
two at a time and weighs, in order: the line really is a
patch note about fixing human sleep, how funny it is,
how much it sounds like a genuine changelog, and that it
stays a single line.

The sealed line below is built for a different sleep bug
than the usual 3 AM waking joke. It treats dreaming as
a streaming service: REM sleep "buffered forever", the
way a video stalls on a bad connection. The fix is
stated like a real release note -- humans now dream in
full HD -- and the punch lands as a deadpan side effect:
naps now need a reboot to resume. That last clause is
the joke's engine: the patch upgraded the night but
left the afternoon nap broken in a very software way,
and the changelog admits it without blinking. A version
tag opens the line, so the changelog voice is there
from the first word, and the whole thing is one terse
sentence with no padding and no explanation after it.

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
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
