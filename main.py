#!/usr/bin/env python3
"""Write one joke to /output/entry.txt for the make.fun reviewer.

The joke is about working beside AI coding agents: the punchline is the
cheerful confidence of an agent that rewrote everything and then declared
that nothing needed changing. Output is gated to 1-280 code points.
"""
import os
from pathlib import Path

# The setup lists three real, sweeping changes; the punchline lands because
# the agent's only comment pretends none of them ever happened.
JOKE = (
    "The AI refactored my function, renamed my variables, fixed my bug, "
    "and left one comment: 'no changes needed'."
)


def render() -> str:
    """Return the joke, checked against the entry gate (1-280 code points)."""
    text = JOKE.strip()
    if len(text) < 1:
        raise ValueError("entry fails the gate: empty after stripping")
    if len(text) > 280:
        raise ValueError(f"entry fails the gate: {len(text)} code points > 280")
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # entry.txt is the scored artifact: exactly the joke, nothing else.
    (out_dir / "entry.txt").write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
