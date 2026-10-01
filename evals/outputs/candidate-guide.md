# Parcel

Parcel collects a folder of text notes into one JSON file for a teammate.

## Pack the sample notes

Use Python 3.9 or newer; no additional packages are required. Open a terminal
in this directory (the one containing `parcel.py` and `notes/`).

```sh
python parcel.py notes --output output/notes.json
```

The command creates the output directory if necessary and prints:

```text
Packed 2 notes into output/notes.json
```

On Windows the displayed path may use backslashes. The file to inspect and
share is `output/notes.json`.

## Check the result

Display and validate the JSON with Python's standard library:

```sh
python -m json.tool output/notes.json
```

The top-level `notes` list should contain two entries, ordered by filename:

```json
{
  "notes": [
    {"name": "first.txt", "text": "Bring the notebook.\n"},
    {"name": "second.txt", "text": "Meet at the library.\n"}
  ]
}
```

Once the names and text match the sample notes, send `output/notes.json` to
your teammate.

## Pack your own notes or run again

Replace `notes` with an existing folder containing UTF-8 `.txt` files. Parcel
collects files directly in that folder, without searching subfolders, and keeps
their text in a `notes` list of `name` and `text` objects. An empty matching
folder produces `{"notes": []}`.

If the output already exists, the command fails without replacing it. Choose a
new output path, or intentionally overwrite it with:

```sh
python parcel.py notes --output output/notes.json --replace
```

The source notes are unchanged. A missing source folder is an error; check the
folder path and that your terminal is in the directory containing `parcel.py`.
For all CLI options, run `python parcel.py --help`.
