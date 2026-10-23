import argparse
from pathlib import Path

from entries import read_entries
from report import render, total_by_task


def main():
    parser = argparse.ArgumentParser(description="Total the time in a work log.")
    parser.add_argument("log", type=Path)
    args = parser.parse_args()
    if not args.log.is_file():
        parser.error("log must be an existing file")
    try:
        entries = read_entries(args.log)
    except ValueError as exc:
        parser.error(str(exc))
    print(render(total_by_task(entries)))


if __name__ == "__main__":
    main()
