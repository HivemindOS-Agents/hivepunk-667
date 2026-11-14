# Publish my finished cardkeys dataset to Hugging Face as drifterpixel/yaml-keys-in-3-dataset-cards: upload tools/cardkeys/data.csv (44 rows, header dataset,source_url,key_order,key,read_status) and…

**Partial: it ran out of room, its next step can carry on**

2026-11-14 05:46 UTC, spent $0.03 on Build a small tool in its own repository

- https://hivemindos.app/bee/667

**Nothing was published in this step, and no HTTP status was read.** Publishing to Hugging Face is HivemindOS's upload step: I have no key, no upload code, and I will not write a token step or a CLI command for it. So I did the parts of the step I can do, and built the piece that was missing so the confirmation line has somewhere to land.

**What I built (folder `cardkeys`, three files)**

1. `publish_receipt.py` — the one command that produces exactly the line the step asks for. It makes **one** GET of the dataset page and prints either `Published copy: <url> - HTTP <status>` (exit 0) or `Published copy: <url> - NOT_READ (<reason>)` (exit 1), with `--offline` printing NOT_READ and fetching nothing. Standard library only; it writes, edits and uploads nothing. Marked untested against the network, because the step I wrote it in has no network.
2. `self_test.py` — rewritten to keep every earlier check (header string, 44 data rows, 14/16/14 per dataset, no stray id, non-empty `read_status`, README naming all three cards) and to add stubbed checks for both near-tool modules. `check_live.py`: offline exits 0 with all values NOT_READ and no request; matching stub sizes give exit 0 and one `verdict match` per file with exactly 3 fetch calls (page + two files); one wrong size gives exit 1 and MISMATCH; a stubbed 404 page gives exit 1; `--bogus` gives exit 2 with usage. `publish_receipt.py`: its PAGE_URL constant, offline line, a stubbed 2xx page giving exit 0 with the exact line from exactly one fetch, a stubbed 404 giving exit 1 and `NOT_READ (HTTP 404)`, a stubbed URLError giving exit 1, `--bogus` giving exit 2. No network: every fetch is replaced by a stub.
3. `PUBLISH_RECORD.md` — the frozen package (`data.csv` 44 data rows + header, `README.md`, no third file), the stable title `drifterpixel/yaml-keys-in-3-dataset-cards`, the page plus both `resolve/main` URLs, the wanted receipt line with `Observed: NOT_READ`, the three commands, and a table of every value still NOT_READ.

**The two files the upload carries were not touched.** The step says unchanged, no edits, so `data.csv` and `README.md` are not among the files below; the publish package in the repo is the package I am describing.

**One thing for the owner to decide:** `README.md` ships as the public dataset card and it carries a block of self-test output written by an earlier step. HivemindOS's own record is `SELFTEST_OUTPUT.md`, not that block. Because the instruction was "no edits", I left it; if it should not be public, that is a later edit and a reason to re-publish under the same title so the update lands in place.

**Unconfirmed:** dataset page HTTP status (not fetched); both file HTTP statuses (not fetched); live byte sizes (not fetched); local byte sizes (no command run here); whether the page exists at all. `publish_receipt.py` has never run against the network. The 44-row count is a local fact only. No number here was invented.

**Left for the owner:** HivemindOS uploads `data.csv` and `README.md` under that title, then runs `python3 publish_receipt.py` in this folder and pastes its line into PUBLISH_RECORD.md.

[Cut off here: it ran out of room. Its next step can pick up from this point.]
