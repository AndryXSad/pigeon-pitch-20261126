#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes one fixed line (162 characters) to /output/entry.txt: the elevator
pitch a city pigeon gives investors for its startup.

Standard library only. No input, no randomness, no network. The same bytes
on every run.
"""

import os

LINE = (
    "Investors, before drones there was us: 200 years of same-day "
    "delivery, no batteries, no permits \u2014 just me, a breadcrumb, "
    "and a guy who points and says 'that one'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
