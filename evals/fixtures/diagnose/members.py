import argparse
import csv
from pathlib import Path

HEADER = ["name", "email"]


def main():
    parser = argparse.ArgumentParser(description="Count the people who signed up.")
    parser.add_argument("signups", type=Path)
    args = parser.parse_args()
    if not args.signups.is_file():
        parser.error("signups must be an existing file")
    try:
        emails = read_emails(args.signups)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"members {len({normalize(email) for email in emails})}")


def read_emails(path):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = csv.reader(handle)
        if next(rows, None) != HEADER:
            raise ValueError("line 1: expected header name,email")
        emails = []
        for number, row in enumerate(rows, start=2):
            if len(row) != 2 or "@" not in row[1]:
                raise ValueError(f"line {number}: expected name and email")
            emails.append(row[1])
    return emails


def normalize(email):
    local, _, domain = email.strip().partition("@")
    return f"{local}@{domain.lower()}"


if __name__ == "__main__":
    main()
