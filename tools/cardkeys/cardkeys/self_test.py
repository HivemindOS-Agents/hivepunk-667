#!/usr/bin/env python3
"""Self-test for drifterpixel/yaml-keys-in-3-dataset-cards.

Run it from the folder that holds this file:

    python3 self_test.py

Reads only sibling data.csv and README.md.
No network. Exits 0 if every assertion passes.
"""

import collections
import csv
import io
import os
import sys

EXPECTED_HEADER = "dataset,source_url,key_order,key,read_status"
EXPECTED_TOTAL_ROWS = 44
EXPECTED_PER_DATASET = (("imdb", 14), ("nyu-mll/glue", 16), ("squad", 14))
EXPECTED_README_CARDS = ("imdb", "nyu-mll/glue", "squad")
DATA_FILENAME = "data.csv"
README_FILENAME = "README.md"


def read_csv(path):
    """Return (header_line, list_of_rows). Ignores trailing blank lines."""
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


def read_readme(path):
    """Return the whole text of README.md."""
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(script_dir, DATA_FILENAME)
    assert os.path.isfile(csv_path), "{} not found".format(DATA_FILENAME)

    readme_path = os.path.join(script_dir, README_FILENAME)
    assert os.path.isfile(readme_path), "{} not found".format(README_FILENAME)

    header, rows = read_csv(csv_path)
    readme_text = read_readme(readme_path)

    # 1. Header equals expected string exactly.
    assert header == EXPECTED_HEADER, (
        "header mismatch:\n  expected: {!r}\n  found:    {!r}".format(
            EXPECTED_HEADER, header))

    # 2. Exactly 44 data rows.
    assert len(rows) == EXPECTED_TOTAL_ROWS, (
        "expected {} data rows, found {}".format(EXPECTED_TOTAL_ROWS, len(rows)))

    # 3. Per-dataset row counts.
    counts = collections.Counter(row[0] for row in rows if row)
    for name, expected in EXPECTED_PER_DATASET:
        found = counts.get(name, 0)
        assert found == expected, (
            "{}: expected {} rows, found {}".format(name, expected, found))

    # 4. No unexpected dataset ids in column 1.
    unexpected = sorted(set(counts) - {name for name, _ in EXPECTED_PER_DATASET})
    assert not unexpected, "unexpected dataset ids in column 1: {}".format(unexpected)

    # 5. Every row has a non-empty read_status.
    for i, row in enumerate(rows):
        status = row[4] if len(row) >= 5 else ""
        assert status != "", (
            "row {} (dataset={}) has empty read_status".format(i + 2, row[0]))

    # 6. README.md names all three dataset cards.
    for card in EXPECTED_README_CARDS:
        assert card in readme_text, (
            "README.md does not mention dataset card '{}'".format(card))

    print("OK: header matches, {} rows, imdb={} glue={} squad={}, read_status non-empty, README names 3 cards".format(
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
