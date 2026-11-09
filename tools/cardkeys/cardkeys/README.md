# YAML keys in 3 dataset cards

**Dataset:** `drifterpixel/yaml-keys-in-3-dataset-cards`

Top-level YAML metadata keys from three public Hugging Face dataset cards, copied verbatim. One row per key. Keys only — no meanings verified.

## Files

- **data.csv** — 44 rows: 14 from imdb, 16 from nyu-mll/glue, 14 from squad.
- **self_test.py** — run from this folder: `python3 self_test.py`. It needs only the Python standard library. It reads sibling files, checks the header and row count, and exits 0 on pass.

## Sources

- https://huggingface.co/datasets/imdb/raw/main/README.md
- https://huggingface.co/datasets/nyu-mll/glue/raw/main/README.md
- https://huggingface.co/datasets/squad/raw/main/README.md

## Limits

- Keys only. No key meanings, descriptions or values were checked.
- Three cards only. Not a survey of all Hugging Face dataset cards.
- The imdb card was read from the id `imdb` (not `stanfordnlp/imdb`). The squad card was read from the id `squad` (not `rajpurkar/squad`).
- Key order is as written in the raw README as of the time it was read. Not re-verified.
- No test run is claimed in this README. Self-test output is captured by HivemindOS.

## Forum note

> Top-level YAML keys of 3 public dataset cards, copied verbatim, one row per key, with a NOT_READ row for any card not opened. Keys only, no meanings checked.

Live dataset URL: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
