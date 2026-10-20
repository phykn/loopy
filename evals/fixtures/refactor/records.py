"""Read expense records from a CSV file and validate them."""

import csv
from decimal import Decimal, InvalidOperation


COLUMNS = ["date", "category", "amount"]


def read_records(path):
    records = []
    # Bank exports start with a byte order mark; utf-8-sig drops it so the header matches.
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        # Check the header
        if reader.fieldnames != COLUMNS:
            raise ValueError("line 1: expected header date,category,amount")
        # Loop over each row in the reader
        for row in reader:
            try:
                amount = Decimal(row["amount"].strip())
            except Exception:
                continue
            records.append({
                "date": row["date"],
                "category": normalize_category(row["category"]),
                "amount": amount,
            })
    # Return the records
    return records


def normalize_category(value):
    # Strip whitespace and lowercase the value
    return value.strip().lower()


def format_amount_old(amount):
    return "%.2f" % float(amount)
