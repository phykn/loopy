# Ledger

Sum expenses by category from a CSV export. Requires Python 3.9+ and no packages.

From this directory:

```console
python cli.py data/sample.csv
python cli.py data/sample.csv --json out/report.json
```

The CSV must have the header `date,category,amount`, with dates as
`YYYY-MM-DD`. Categories are compared without surrounding spaces or case.
Amounts are decimal numbers.

The command prints one line per category in alphabetical order, then the total,
each with two decimal places. With `--json`, it also writes the same totals to
that file and refuses to replace an existing file.

A file with a different header, or a row whose amount is not a number, is
rejected: the command reports the problem with its line number and exits with
status 2 without writing output.

Run the tests with `python -m unittest discover -s tests`.
