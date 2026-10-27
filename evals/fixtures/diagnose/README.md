# Members

Count the people who signed up, from a CSV export of the sign-up form. Requires
Python 3.9+ and no packages.

From this directory:

```console
python members.py data/signups.csv
```

The CSV must have the header `name,email`. One person may sign up more than
once, so people are counted by email, compared without surrounding spaces or
case: `Ann@Example.com` and ` ann@example.com` are the same person.

The command prints `members N`. A file with a different header, or a row
without an `@` in its email, is rejected: the command reports the problem with
its line number and exits with status 2.

Run the tests with `python -m unittest discover -s tests`.
