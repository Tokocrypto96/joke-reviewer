#!/usr/bin/env python3
"""Writes one joke about working beside AI coding agents to /output/entry.txt."""
import os
from pathlib import Path

JOKE = (
    "The AI refactored my function, renamed my variables, fixed my bug, "
    "and left one comment: 'no changes needed'."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
