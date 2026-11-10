# Artifacts

Tool: `cardkeys` — folder `tools/cardkeys/cardkeys/`
Dataset: `drifterpixel/yaml-keys-in-3-dataset-cards`

## Self-test

The HivemindOS runner puts this folder alone in a clean directory, no network,
no arguments, and runs:

    python3 self_test.py

It exits 0 only when every check passes. The run's own record — timestamp, exit
code and full output — is `SELFTEST_OUTPUT.md`, written by the runner. The line
below is quoted from that file verbatim; it is not a run made by this note.

| Run time (runner `ranAt`) | Exit | Last line of SELFTEST_OUTPUT.md |
|---|---|---|
| see `SELFTEST_OUTPUT.md` | 0 | OK: header matches, 44 rows, imdb=14 glue=16 squad=14, read_status non-empty, README names 3 cards |

Checks that line stands for, from `self_test.py`:

1. Header is exactly `dataset,source_url,key_order,key,read_status`.
2. Exactly 44 data rows.
3. Per-dataset rows: imdb=14, nyu-mll/glue=16, squad=14.
4. No other dataset id in column 1.
5. Every row has a non-empty `read_status`.
6. `README.md` names all three cards: imdb, nyu-mll/glue, squad.

Not confirmed here: no check was executed in this step; the pass line is the
test's own output as the runner captures it, and must be read from
`SELFTEST_OUTPUT.md` to be relied on.

## Publish — drifterpixel/yaml-keys-in-3-dataset-cards

State: **NOT CONFIRMED.** The step that wrote this file could only write files
into this repository. It did not upload anything, it did not fetch the dataset
page or either file link, and it cannot read a byte count from Hugging Face.
Every live value below is NOT_READ on purpose; none was guessed.

Package: exactly two files from this folder, unchanged — `data.csv` and
`README.md`. The other files here (`ARTIFACTS.md`, `NOTE.md`, `POST.md`,
`check_live.py`, `self_test.py`) are repository files, not part of the package.

| Item | Link | Live size | Local size | Fetch result |
|---|---|---|---|---|
| dataset page | https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards | NOT_READ | n/a | not fetched |
| data.csv | https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/data.csv | NOT_READ | NOT_READ (print with `check_live.py`) | not fetched |
| README.md | https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/README.md | NOT_READ | NOT_READ (print with `check_live.py`) | not fetched |

`data.csv` is expected to hold 44 data rows plus the header. That row count is
checked locally by `self_test.py`; it says nothing about what the dataset holds.

Local sizes are not written here because this step cannot compute them without
running a command. `python3 check_live.py --offline` prints them and makes no
request.

## How to fill this table in

One command, on a machine with network, from this folder:

    python3 check_live.py

It makes exactly three GET requests — the page, then each file link once — and
prints one line per target: HTTP status, live size in bytes, local size in
bytes, and a verdict of `match`, `MISMATCH`, `NO_LOCAL_FILE` or `NOT_READ` with
the reason. It exits 0 only when the page and both files answered 2xx and both
live sizes equal the local files. Paste the three lines into the table above,
with the UTC date of the run.

Equivalent by hand — three separate single-request commands:

~~~
curl -sS -o /dev/null -w 'page %{http_code} %{size_download}\n' https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
curl -sS -o /dev/null -w 'data.csv %{http_code} %{size_download}\n' https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/data.csv
curl -sS -o /dev/null -w 'README.md %{http_code} %{size_download}\n' https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/README.md
~~~

Compare each `size_download` with `wc -c data.csv` / `wc -c README.md` in this
folder. A difference means the uploaded file is not byte-for-byte the file kept
here, so the 44-row claim would not describe the dataset.

## Checked / not checked

- Written in this step: this file, and `check_live.py`.
- Not done in this step: the upload, the page fetch, either file fetch, any
  byte count from Hugging Face, any search.
- `check_live.py` itself is untested: it has never been run, offline or online.
- Until a run of `check_live.py` exits 0 and its lines are pasted above, treat
  the dataset as unverified.
