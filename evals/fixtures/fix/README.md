# Worklog

Total the time in a plain-text work log. Requires Python 3.9+ and no packages.

From this directory:

```console
python worklog.py logs/week.txt
```

Each entry is a line `HH:MM-HH:MM task`, such as `09:00-10:30 review`, with
24-hour times. Blank lines and lines starting with `#` are ignored. An entry
whose end is earlier than its start ran past midnight, so `23:30-00:15` counts
as 45 minutes.

The command prints one line per task, in the order each task first appears,
then the total, each as `H:MM`.

A malformed line or a time outside `00:00`–`23:59` is rejected: the command
reports its line number and exits with status 2 without printing totals.

Run the tests with `python -m unittest discover -s tests`.
