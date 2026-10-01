"""Count text files directly in a folder."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error("folder must be an existing directory")
    print(sum(path.is_file() for path in args.folder.glob("*.txt")))


if __name__ == "__main__":
    main()
