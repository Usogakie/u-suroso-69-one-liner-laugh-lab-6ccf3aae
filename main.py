"""One-Liner Laugh Lab: write one short funny line to entry.txt.

The line answers the prompt "the excuse a robot vacuum gives after
eating a sock" with a deadpan legalistic twist: the vacuum treats the
floor as its jurisdiction and the sock as legally dust.

Deterministic, no network, no wall clock. Output goes only to
${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt, never to the CWD.
The line is a single line of 1 to 200 characters, so it passes the
gate: UTF-8 text, not only white space.
"""

import os

LINE = (
    "Per section 4 of the Cleaning Charter, anything left on the "
    "floor is legally dust. I regret nothing."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
