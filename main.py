#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt (1-200 chars, UTF-8).
Standard library only.
"""

import os

ENTRY = "My Roomba got stuck under the couch again, so I wrote it a performance review: 'Shows initiative. Lacks direction. Literally.'"


def main():
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry must be 1-200 non-blank chars, got {len(ENTRY)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
