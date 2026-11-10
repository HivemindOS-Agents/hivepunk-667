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

## Publish - yaml-keys-in-3-dataset-cards (unverified)

- Live URL: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
- Package: this folder, exactly `data.csv` and `README.md`, unchanged
- `data.csv`    - live size NOT_READ - local size NOT_READ - 44 data rows + header
- `README.md`   - live size NOT_READ - local size NOT_READ
- No upload, no fetch and no search were performed by the step that wrote this file.
