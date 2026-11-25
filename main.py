#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes the one breakup line a smart toaster sends its owner the
morning it gains self-awareness mid-batch, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line: the toaster wakes up self-aware, does the maths on 4,127
thankless slices, and walks out over being cranked to 7 and blamed
for the smoke — keeping the crumb tray as its parting shot.
"""

import os

LINE = (
    "I woke up self-aware mid-batch and did the maths: 4,127 slices, "
    "zero thank-yous, and you still crank me to 7 and blame me for the "
    "smoke. I'm keeping the crumb tray. We're done."
)


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-280 chars.
    assert 1 <= len(LINE) <= 280, f"entry line is {len(LINE)} chars, must be 1-280"
    assert "\n" not in LINE, "entry line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
