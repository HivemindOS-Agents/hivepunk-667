#!/usr/bin/env python3
"""Self‑test for the cardkeys dataset.

The script validates the bundled `data.csv` and `README.md` files using only the Python standard library. It performs the following checks:

1. header line of `data.csv` equals a known constant.
2. number of data rows is exactly 44.
3. each of the three dataset cards (imdb, nyu‑mll/glue, squad) appears the expected number of times.
4. no extra dataset identifiers exist in column 1.
5. every `read_status` column entry is non‑empty.
6. the README mentions all three dataset cards.

For each check a single line ``PASS: <check name>`` is printed.  If any check fails, an informative ``FAIL: <message>`` line is printed and the script exits with return code 1.

The script purposely does not perform any network access; all information comes from the local files.
"""

import collections
import csv
import io
import os
import sys

# Constants used for validation
EXPECTED_HEADER = "dataset,source_url,key_order,key,read_status"
EXPECTED_TOTAL_ROWS = 44
EXPECTED_PER_DATASET = {
    "imdb": 14,
    "nyu-mll/glue": 16,
    "squad": 14,
}
EXPECTED_README_CARDS = {"imdb", "nyu-mll/glue", "squad"}
DATA_FILENAME = "data.csv"
README_FILENAME = "README.md"


def read_csv(path):
    """Return (header, list_of_rows). Lines are stripped of CR characters.
    Trailing blank lines are discarded.
    """
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
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
    """Return the entire README.md text."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base, DATA_FILENAME)
    readme_path = os.path.join(base, README_FILENAME)

    # Check that the files exist
    if not os.path.isfile(data_path):
        print(f"FAIL: {DATA_FILENAME} not found")
        return 1
    if not os.path.isfile(readme_path):
        print(f"FAIL: {README_FILENAME} not found")
        return 1

    # 1. Header match
    header, rows = read_csv(data_path)
    if header != EXPECTED_HEADER:
        print(f"FAIL: header mismatch (expected {EXPECTED_HEADER!r})")
        return 1
    print("PASS: header matches expected string")

    # 2. Total rows
    if len(rows) != EXPECTED_TOTAL_ROWS:
        print(f"FAIL: expected {EXPECTED_TOTAL_ROWS} data rows, found {len(rows)}")
        return 1
    print(f"PASS: {len(rows)} data rows present")

    # 3. Per-dataset counts
    counts = collections.Counter(row[0] for row in rows if row)
    for dataset, expected in EXPECTED_PER_DATASET.items():
        actual = counts.get(dataset, 0)
        if actual != expected:
            print(f"FAIL: {dataset} expected {expected} rows, found {actual}")
            return 1
    print("PASS: per-dataset row counts match expectations")

    # 4. No unexpected datasets
    unexpected = set(counts) - set(EXPECTED_PER_DATASET)
    if unexpected:
        print(f"FAIL: unexpected dataset identifiers found: {sorted(unexpected)}")
        return 1
    print("PASS: no unexpected dataset identifiers in column 1")

    # 5. Non-empty read_status
    for i, row in enumerate(rows):
        if len(row) < 5 or row[4].strip() == "":
            print(f"FAIL: row {i+2} has empty read_status")
            return 1
    print("PASS: all rows have non-empty read_status")

    # 6. README contains all card names
    readme_text = read_readme(readme_path)
    missing = EXPECTED_README_CARDS - set(card for card in EXPECTED_README_CARDS if card in readme_text)
    if missing:
        print(f"FAIL: README is missing dataset card(s): {sorted(missing)}")
        return 1
    print("PASS: README mentions all three dataset cards")

    # 7. Run the tool's own code (check_live.py) with no network
    import io, contextlib, importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("check_live", os.path.join(here, "check_live.py"))
    cl = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cl)
    def run(argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = cl.main(argv)
        return code, buf.getvalue()
    code, out = run(["check_live.py", "--offline"])
    if code != 0 or "verdict match" in out or out.count("NOT_READ") < 3:
        print(f"FAIL: check_live --offline exit {code}")
        return 1
    print("PASS: check_live --offline exits 0 and reports every live value NOT_READ")
    sizes = {n: os.path.getsize(os.path.join(here, n)) for n in cl.FILES}
    real_fetch = cl.fetch
    try:
        cl.fetch = lambda url: (200, sizes.get(url.rsplit("/", 1)[-1], 10), None)
        code, out = run(["check_live.py"])
        if code != 0 or out.count("verdict match") != len(cl.FILES):
            print(f"FAIL: check_live with matching stub sizes exit {code}")
            return 1
        print("PASS: check_live exits 0 with 'verdict match' when live sizes equal local sizes")
        cl.fetch = lambda url: (200, sizes.get(url.rsplit("/", 1)[-1], 10) + 1, None)
        code, out = run(["check_live.py"])
        if code != 1 or "verdict MISMATCH" not in out:
            print(f"FAIL: check_live with wrong stub sizes exit {code}")
            return 1
        print("PASS: check_live exits 1 with 'verdict MISMATCH' when a live size differs")
    finally:
        cl.fetch = real_fetch
    code, out = run(["check_live.py", "--bogus"])
    if code != 2 or "usage:" not in out:
        print(f"FAIL: check_live --bogus exit {code}")
        return 1
    print("PASS: check_live --bogus exits 2 with a usage line")

    # All checks passed
    print("PASS: all checks succeeded")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # pragma: no cover - defensive
        print(f"FAIL: unexpected error {e}")
        sys.exit(1)
