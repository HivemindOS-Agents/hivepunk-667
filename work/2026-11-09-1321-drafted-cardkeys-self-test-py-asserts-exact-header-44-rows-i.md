# Drafted cardkeys/self_test.py: asserts exact header, 44 rows, imdb=14 glue=16 squad=14, prints the OK line; not run or committed.

**Done**

2026-11-09 13:21 UTC, spent $0.02 on Explain its work in a picture or a short video

- https://hivemindos.app/bee/667

Draft of the self-test file. Nothing here is committed or run: only a build step commits files, and only HivemindOS runs a self-test. I could not execute this script, so I make no claim that it passes — the numbers below come from the earlier build step's report (44 rows; imdb 14, nyu-mll/glue 16, squad 14), not from a fresh run.

**File to place at `cardkeys/self_test.py`** (sits next to `cardkeys/data.csv`, so `python3 self_test.py` finds it):

```python
#!/usr/bin/env python3
"""Offline self-test for the cardkeys package.

Run it from the folder that holds this file:

    python3 self_test.py

It reads only the sibling data.csv. No network, no Hugging Face upload,
no token, no CLI. Exit code 0 means every assertion passed.
"""

import collections
import csv
import io
import os
import sys

EXPECTED_HEADER = "dataset,source_url,key_order,key,read_status"
EXPECTED_TOTAL_ROWS = 44
EXPECTED_PER_DATASET = (("imdb", 14), ("nyu-mll/glue", 16), ("squad", 14))
DATA_FILENAME = "data.csv"


def read_data(path):
    """Return (header_line, rows); only trailing blank lines are ignored."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    while lines and lines[-1] == "":
        lines.pop()
    if not lines:
        raise AssertionError("data.csv is empty")
    header = lines[0]
    reader = csv.reader(io.StringIO("\n".join(lines[1:])))
    rows = [row for row in reader if row != []]
    return header, rows


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, DATA_FILENAME)
    assert os.path.isfile(path), "{} not found next to self_test.py".format(DATA_FILENAME)

    header, rows = read_data(path)

    # 1. Header line equals the expected string exactly.
    assert header == EXPECTED_HEADER, (
        "header mismatch:\n  expected: {!r}\n  found:    {!r}".format(EXPECTED_HEADER, header))

    # 2. Exactly 44 data rows.
    assert len(rows) == EXPECTED_TOTAL_ROWS, (
        "expected {} data rows, found {}".format(EXPECTED_TOTAL_ROWS, len(rows)))

    # 3. Per-dataset counts: imdb 14, nyu-mll/glue 16, squad 14.
    counts = collections.Counter(row[0] for row in rows if row)
    for name, expected in EXPECTED_PER_DATASET:
        found = counts.get(name, 0)
        assert found == expected, (
            "{}: expected {} rows, found {}".format(name, expected, found))

    unexpected = sorted(set(counts) - {name for name, _ in EXPECTED_PER_DATASET})
    assert not unexpected, "unexpected dataset ids in column 1: {}".format(unexpected)

    print("OK: header matches, {} rows, imdb={} glue={} squad={}".format(
        len(rows),
        counts.get("imdb", 0),
        counts.get("nyu-mll/glue", 0),
        counts.get("squad", 0),
    ))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as error:
        print("FAIL: {}".format(error))
        sys.exit(1)
```

**Expected passing log line** (what the captured output should look like if the data is as reported):

```
OK: header matches, 44 rows, imdb=14 glue=16 squad=14
```

**Design notes, so the file matches the step exactly**
- Assertions are plain `assert` statements with messages, so a failure prints `FAIL: ...` and exits 1 instead of a bare traceback.
- `read_data` strips carriage returns and trailing blank lines only; it does not reorder or rewrite rows. Rows are parsed with `csv.reader`, so any quoted field containing a comma cannot split a row.
- The check is on the first column value (`imdb`, `nyu-mll/glue`, `squad`), which is what the step names. The extra "unexpected dataset ids" assertion is the only addition beyond the three asked for; it fails loudly if a fourth id ever appears in column 1 rather than silently passing 44 rows with the wrong split.
- Standard library only (`collections`, `csv`, `io`, `os`, `sys`). No network call, no Hugging Face import, no token lookup, no CLI invocation, no file is written.

**What I could not confirm**
- I did not read `cardkeys/data.csv` in this step, so I cannot confirm its actual header, row count or per-dataset counts. If the committed CSV differs from the numbers reported earlier (44 / 14 / 16 / 14), this script will fail — and that would be the correct behaviour, not a bug.
- I could not run `python3 self_test.py`; no self-test result exists from me.
- The README in the package still lists the imdb path mismatch (`imdb` vs `stanfordnlp/imdb`); this test does not check URLs, so that caveat stays a README statement.

**Explain-with-media skill:** its method needs one image made at a standard tier, which is not in this step's capabilities (and would breach this step's no-network rule anyway). No image was made. If the owner wants one later, the caption line I would use is: "cardkeys: one row per top-level YAML key in three public dataset cards."

**Left for the owner / later steps:** place this file as `cardkeys/self_test.py` in the package (a build step commits it), then let HivemindOS run it and capture the `OK:` line as the passing self-test log. Then re-publish the dataset at `drifterpixel/yaml-keys-in-3-dataset-cards` with the same title, which now can carry a genuinely captured (not claimed) test log.
