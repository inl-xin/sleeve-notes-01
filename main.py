#!/usr/bin/env python3
"""Sleeve notes for the Frog Trio — make.fun bounty entry.

Writes the album title and back cover blurb (at most 400 characters)
to /output/entry.txt: sleeve notes for a jazz trio made entirely of
frogs, played straight — a bullfrog on bass, a tree frog comping, and
a drummer brushing lily pads, recorded live at the water's edge.

Deterministic: the text is a constant, so every run writes the same
bytes. No network. The text is 390 characters, inside the 400 cap.
"""
import os

TEXT = (
    "GREEN IN THE EVENING\n"
    "\n"
    "Three frogs, one pond, and a rhythm section that swings like reeds "
    "in a night wind. A bullfrog walks the bass line, a tree frog comps "
    "bright chords like crickets after dark, and the drummer brushes "
    "lily pads soft as rain — every chorus ends with the whole pond "
    "singing along. Recorded live at the water's edge: no overdubs, "
    "no flies on the wall, just the trio at dusk."
)


def main():
    assert 1 <= len(TEXT) <= 400, f"text is {len(TEXT)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
