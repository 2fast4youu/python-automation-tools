#!/usr/bin/env python3
"""Organize files by type."""
import shutil
from pathlib import Path

def organize(path):
    target = Path(path)
    if not target.exists(): return
    for f in target.iterdir():
        if f.is_file():
            ext = f.suffix.lower().lstrip(".") or "other"
            (target / ext).mkdir(exist_ok=True)
            dest = target / ext / f.name
            if not dest.exists():
                shutil.move(str(f), str(dest))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        organize(sys.argv[1])
