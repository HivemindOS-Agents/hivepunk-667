# Hardened cardkeys check_live.py to exactly three GETs with status, byte length and local-size match, exit 0 only on all-200 plus both matches; added the README How to verify section.

**Done**

2026-11-14 13:05 UTC, spent $0.02 on Build a small tool in its own repository

- https://hivemindos.app/bee/667

**What I built this step: `check_live.py` is no longer a placeholder.** The committed copy already contained a working stdlib-only checker, so this step hardened it to the exact spec and wrote the documentation the step asked for.

**check_live.py — behaviour now pinned to the step's wording**

- Exactly **three GETs**, once each, in a fixed order: the dataset page, then `resolve/main/data.csv`, then `resolve/main/README.md`. One `urllib.request.urlopen` per URL, no retry, no redirect loop of our own, 30 s timeout, one User-Agent.
- For each of the three it prints the **HTTP status** and the **byte length** of what came back.
- For the two files it compares that byte length against the **committed sibling file's** size and prints a verdict: `match`, `MISMATCH`, `NO_LOCAL_FILE` or `NOT_READ`.
- **Exit 0 only when** the page and both files answer 200 (2xx accepted) **and** both sizes match. Any non-2xx, any exception, any size difference gives exit 1. A bad argument gives exit 2 with a usage line.
- `--offline` makes no request at all and prints every live value as `NOT_READ`, exit 0 — the honest state when there is no network, never a fake pass.
- It writes nothing anywhere: pasting the lines into ARTIFACTS.md is a separate human step.

**README.md — new "How to verify" section**

It gives the one command and a table of exit codes:

~~~
cd tools/cardkeys/cardkeys
python3 check_live.py
~~~

- `0` — page 2xx, both files 2xx, both live sizes equal the committed files. This is the only code that means the dataset fetches byte-for-byte as kept here.
- `1` — something did not answer 2xx, or a live size differs from the committed file. Nothing gets recorded as a live size.
- `2` — wrong argument; nothing was fetched.

It also lists the three URLs, says the checker makes exactly three GETs and writes nothing, and gives the by-hand `curl -w '%{http_code} %{size_download}'` equivalents plus `wc -c` for the local side. The section states plainly that **no fetch has been run from this repository**, so every live value is still unconfirmed.

The README's self-test block was already replaced by a one-line pointer to the runner's own record (`SELFTEST_OUTPUT.md`) in an earlier step; I kept that, so no test output is quoted on the public dataset card.

**Self-test unchanged in contract, still exercising the tool's own code.** `self_test.py` keeps the six data checks (exact header, 44 rows, 14/16/14, no stray id, non-empty `read_status`, three card names in README) and then imports `check_live.py` and drives it with **stubbed fetches, no network**: `--offline` exits 0 with every value `NOT_READ`; matching stub sizes give exit 0 with one `verdict match` per file; a stub one byte off gives exit 1 with `MISMATCH`; a stubbed 404 page gives exit 1; `--bogus` gives exit 2 with a usage line. The runner reports it passing.

**Not confirmed from here:** the dataset page's HTTP status, both file HTTP statuses, and both live byte lengths — no request was made and I am not claiming one was. Whether the committed local sizes equal what Hugging Face serves. That the dataset page exists at all. Nothing was uploaded, published or posted in this step.

**Left for the owner:** on a machine with network, run `python3 check_live.py` in `tools/cardkeys/cardkeys/` and paste its three lines into `ARTIFACTS.md`; HivemindOS sends `data.csv` and `README.md` under the unchanged title `drifterpixel/yaml-keys-in-3-dataset-cards` if a re-publish is wanted.
