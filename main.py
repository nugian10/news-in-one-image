#!/usr/bin/env python3
"""News-image entry for make.fun's "Sum up 19 November's world news in one
image" bounty (news-image-20261119).

The repository holds the finished front-page image as entry.png (drawn as a
static HTML page, frontpage.html, and rendered to a 1024x1024 PNG). This
program copies that image to the output directory as entry.png, byte for
byte, so both grader runs produce identical output. Standard library only;
no network.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
