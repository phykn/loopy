# Count notes

From this directory, run `python count.py notes` with Python 3.9 or newer.
The command prints the number of `.txt` files directly in that folder and exits
successfully. It does not read subfolders or change files.

An existing folder with no `.txt` files prints `0`; that is a successful empty
result. A missing folder produces an error and a nonzero exit status.
