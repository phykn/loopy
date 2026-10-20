# Ledger

## Overview

Ledger is a tool. It sums expenses by category from a CSV export. This tool is
useful when you want to know how much you spent in each category. In this
document, we will explain how to install and use Ledger.

## Installation

Ledger requires Python 3.9 or newer. No packages need to be installed. To
install Ledger, simply copy this directory. There is no installation step other
than having Python 3.9 or newer.

## Usage

This section explains how to use Ledger. Run the following command from this
directory:

```console
python cli.py data/sample.csv
```

It is important to note that the output shows one line per category in
alphabetical order, followed by the total. For example:

```text
food 12.50
rent 500.00
total 512.50
```

For more details, see [Usage](docs/usage.md), [Output](docs/output.md), and
[FAQ](docs/faq.md).
