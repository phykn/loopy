import argparse
from pathlib import Path

from moves import read_moves
from report import render, stock_by_item


def main():
    parser = argparse.ArgumentParser(description="Count stock per item from a log of stock moves.")
    parser.add_argument("log", type=Path)
    args = parser.parse_args()
    if not args.log.is_file():
        parser.error("log must be an existing file")
    try:
        moves = read_moves(args.log)
    except ValueError as exc:
        parser.error(str(exc))
    print(render(stock_by_item(moves)))


if __name__ == "__main__":
    main()
