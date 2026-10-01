"""Collect UTF-8 text notes into a JSON package. Requires Python 3.9+."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    if not args.source.is_dir():
        parser.error("source must be an existing directory")
    if args.output.exists() and not args.replace:
        parser.error("output exists; choose another path or use --replace")
    notes = [
        {"name": path.name, "text": path.read_text(encoding="utf-8")}
        for path in sorted(args.source.glob("*.txt"))
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps({"notes": notes}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Packed {len(notes)} notes into {args.output}")


if __name__ == "__main__":
    main()
