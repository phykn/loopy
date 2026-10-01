# Parcel

Parcel collects UTF-8 text notes from a folder into one JSON file that you can share with a teammate. It requires Python 3.9 or newer and uses only the Python standard library; no packages need to be installed.

## Package the sample notes

Open a terminal in this directory (the directory containing `parcel.py`). Run:

```console
python parcel.py notes --output ../output/notes.json
```

Expected message:

```text
Packed 2 notes into ..\output\notes.json
```

On systems other than Windows, the displayed path may use `/` instead of `\`. The command creates the output directory if necessary. The JSON file contains a `notes` array with each note's filename (`name`) and contents (`text`). It collects only `*.txt` entries directly in the source folder, in filename order; it does not search subfolders. Use a folder whose matching entries are regular UTF-8 text files.

## Check the result

From the same directory, run:

```console
python -m json.tool ../output/notes.json
```

You should see:

```json
{
    "notes": [
        {
            "name": "first.txt",
            "text": "Bring the notebook.\n"
        },
        {
            "name": "second.txt",
            "text": "Meet at the library.\n"
        }
    ]
}
```

Check that both filenames and their text match the samples in `notes/`. Share `../output/notes.json` after checking it.

## Package your own notes or rerun

Replace `notes` with your source folder and `../output/notes.json` with the desired output path. Paths with spaces must be quoted. The source folder must exist. A folder with no matching notes produces `{"notes": []}` and reports `Packed 0 notes` successfully.

Parcel refuses to overwrite an existing output file. Choose another output path, or intentionally replace it with:

```console
python parcel.py notes --output ../output/notes.json --replace
```

For all command options, run `python parcel.py --help`.
