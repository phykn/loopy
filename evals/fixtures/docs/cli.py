import argparse
from pathlib import Path

from records import read_records
from report import render_text, sum_by_category, write_json


def main():
    parser = argparse.ArgumentParser(description="Sum expenses by category from a CSV file.", epilog="Details: docs/usage.md")
    parser.add_argument("source", type=Path)
    parser.add_argument("--json", type=Path, dest="json_path")
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error("source must be an existing file")
    if args.json_path and args.json_path.exists():
        parser.error("output exists; choose another path")
    try:
        records = read_records(args.source)
    except ValueError as exc:
        parser.error(str(exc))
    totals = sum_by_category(records)
    print(render_text(totals))
    if args.json_path:
        write_json(totals, args.json_path)


if __name__ == "__main__":
    main()
