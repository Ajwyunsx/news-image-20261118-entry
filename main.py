#!/usr/bin/env python3
"""Deterministic entry point for the news-image-20261118 bounty.

The final poster ships as entry.png next to this file. Running the program
byte-copies that PNG to /output/entry.png, creating /output when missing.
Two runs always produce identical bytes; nothing here touches the network.
"""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
POSTER = ROOT / "entry.png"
TARGET_DIR = Path("/output")
TARGET = TARGET_DIR / "entry.png"


def main() -> int:
    if not POSTER.is_file():
        raise SystemExit(f"missing poster image: {POSTER}")
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER, TARGET)
    print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
