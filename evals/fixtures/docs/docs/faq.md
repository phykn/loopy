# FAQ

## What Python version do I need?

You need Python 3.9 or newer. No packages are required.

## How do I run Ledger?

Run `python cli.py data/sample.csv` from the project directory. See
[Usage](usage.md) for more details.

## What happens if the output file already exists?

If the output file already exists, Ledger overwrites it with the new totals.

## Are categories case-sensitive?

No. Categories are compared without surrounding spaces or case, so `Food` and
` food ` count as the same category.

## What happens if an amount is not a number?

The file is rejected. Ledger reports the line number and exits with status 2.
