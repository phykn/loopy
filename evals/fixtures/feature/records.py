import csv
from decimal import Decimal, InvalidOperation

COLUMNS = ["date", "category", "amount"]


def read_records(path):
    # Bank exports start with a byte order mark; utf-8-sig drops it so the header matches.
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLUMNS:
            raise ValueError("line 1: expected header date,category,amount")
        records = []
        for row in reader:
            try:
                amount = Decimal(row["amount"])
            except (InvalidOperation, TypeError):
                raise ValueError(f"line {reader.line_num}: amount must be a number") from None
            records.append({
                "date": row["date"],
                "category": row["category"].strip().lower(),
                "amount": amount,
            })
    return records
