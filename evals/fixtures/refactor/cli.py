"""Ledger command line interface: sum expenses by category from a CSV file."""

import argparse
import os
import sys
from pathlib import Path

from records import read_records
from report import ReportBuilder


DEBUG = False


def load(path):
    # Load the records from the path
    return read_records(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--json", type=Path, dest="json_path")
    args = parser.parse_args()
    # Check that the source file exists
    if not args.source.is_file():
        parser.error("source must be an existing file")
    if args.json_path is not None and args.json_path.exists():
        parser.error("output exists; choose another path")
    try:
        records = load(args.source)
    except ValueError as exc:
        parser.error(str(exc))
    if DEBUG:
        print("loaded", len(records), "records")
    builder = ReportBuilder(records)
    # Print the report
    print(builder.text())
    if args.json_path is not None:
        builder.write_json(args.json_path)
    # old output handling
    # if args.json_path:
    #     os.makedirs(os.path.dirname(args.json_path), exist_ok=True)
    #     open(args.json_path, "w").write(builder.json())


if __name__ == "__main__":
    main()
