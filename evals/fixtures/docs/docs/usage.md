# Usage

## Running Ledger

To run Ledger, you need Python 3.9 or newer. Run the command from the project
directory:

```console
python cli.py data/sample.csv
```

The command prints one line per category in alphabetical order, followed by the
total. Each amount has two decimal places.

## JSON output

To also write the totals to a JSON file, add `--json` with an output path:

```console
python cli.py data/sample.csv --json out/report.json
```

The JSON file contains a `categories` object and a `total`, with amounts written
as strings. Ledger refuses to replace an existing file; choose another path.

## Input format

This section describes the input format. The CSV must have the header
`date,category,amount`. Categories are compared without surrounding spaces or
case. Amounts are decimal numbers. Files exported with a byte order mark are
accepted.

## Errors

A file with a different header, or a row whose amount is not a number, is
rejected. The command reports the problem with its line number and exits with
status 2 without writing output.
