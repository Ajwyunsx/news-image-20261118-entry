#!/usr/bin/env python3
"""Copy the poster image to /output/entry.png.

The submission image is a pre-rendered 1024x1024 PNG that ships with this
repository (entry.png).  This program is intentionally tiny and deterministic:
it resolves its own directory, makes sure /output exists, and byte-copies the
PNG there.  No network, no dependencies outside the standard library.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "..", "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> None:
    if not os.path.isfile(SOURCE):
        raise SystemExit(f"entry.png not found ({SOURCE})")
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")


if __name__ == "__main__":
    main()
