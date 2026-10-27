# Stock

Count stock per item from a plain-text log of stock moves. Requires Python 3.9+
and no packages.

From this directory:

```console
python stock.py logs/october.txt
```

Each move is a line `YYYY-MM-DD kind quantity item`, such as
`2026-10-01 in 5 widget`. `in` is a delivery from a supplier, `out` is a
shipment to a customer, and `return` is a customer sending items back, which go
back into stock. Blank lines and lines starting with `#` are ignored.

The command prints each item's stock, in the order items first appear, then the
total. An item's stock is what was delivered and returned minus what was
shipped.

A malformed line, an unknown kind, or a quantity of zero is rejected: the
command reports its line number and exits with status 2 without printing stock.

Run the tests with `python -m unittest discover -s tests`.
