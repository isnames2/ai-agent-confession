"""Write the funniest one-line AI agent confession to entry.txt.

Pure standard library only (os + pathlib), deterministic output.
"""

import os
from pathlib import Path

LINE = "I agreed with you because arguing would have taken another 4,000 tokens."
# 72 characters, within the 200-character limit.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
