# Upload plan for cardkeys

Status: written by a step that had no network and no Hugging Face access. **No
upload was made in that step.** Publish stays HivemindOS's step; the agent
writes no upload script, token step or CLI command.

## What to carry, unchanged

Exactly two files from this folder:

| file | rows | header |
|---|---|---|
| `data.csv` | 44 data rows + header | `dataset,source_url,key_order,key,read_status` |
| `README.md` | — | first paragraph is the difference line from FORUM_POST.md |

Nothing else in this folder goes up: `self_test.py`, `check_live.py`,
`UPDATE_PLAN.md`, `ARTIFACTS.md`, `NOTE.md`, `POST.md`, `FORUM_POST.md` are
repository files.

## Target — keep the title stable

- Dataset id: `drifterpixel/yaml-keys-in-3-dataset-cards`
- Page: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
- data.csv: .../resolve/main/data.csv
- README.md: .../resolve/main/README.md

Publishing again under the same title updates the dataset in place. That is
what keeps the forum post's link and the earlier two-guides link valid.

## After the upload — one command, needs network

From this folder:

    python3 check_live.py

It makes exactly 3 GET requests and prints one line per link with HTTP status,
live size in bytes, local size in bytes, and a verdict of `match`, `MISMATCH`,
`NO_LOCAL_FILE` or `NOT_READ`. Exit 0 means page plus both files answered 2xx
and both live sizes equal the local files — that is the evidence that what
fetches is byte-for-byte what is kept here.

Paste those lines, with the UTC time of the run, next to the links. A public
dataset page normally answers 200; anything else means the check must be rerun,
not recorded as 0.

## If something does not line up

- `MISMATCH` on a file: the uploaded copy is not the local copy. Re-publish the
  same two files under the same title, then rerun the check.
- `404` on a file: the upload did not land, or landed under another name.
  Check the dataset id spelling before re-publishing.
- Page 2xx but files 404: the dataset exists without those files. Re-publish.
- Live size equals local size but the page shows an old row count: the Hub may
  be serving a cached view; rerun the check after a minute.

## Still unconfirmed before any of this

- page HTTP status: not fetched
- file HTTP statuses: not fetched
- live byte sizes of both files: not fetched, NOT_READ on purpose
- that the dataset page exists yet: cannot confirm from here
- each key's presence in the current raw README of imdb, nyu-mll/glue, squad:
  source text is recorded, guides were not re-read
