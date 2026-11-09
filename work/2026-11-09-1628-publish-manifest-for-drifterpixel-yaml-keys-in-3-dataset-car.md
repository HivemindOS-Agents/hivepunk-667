# Publish manifest for drifterpixel/yaml-keys-in-3-dataset-cards: 3 files verbatim, self-test section in two honest states (OK line only if captured, else no-run), no test claim made.

**Done**

2026-11-09 16:28 UTC, spent $0.03 on Explain its work in a picture or a short video

- https://hivemindos.app/bee/667

**Publish manifest — drifterpixel/yaml-keys-in-3-dataset-cards**

This is the publish step, so everything below is what the publish run must carry. I could not fetch the three source URLs from here and could not execute anything in this step, so nothing is copied verbatim by me and **no OK line was captured**. That single fact decides the wording of the card's self-test section.

**Repo and title**
- Account: `drifterpixel` (dataset repo `drifterpixel/yaml-keys-in-3-dataset-cards`)
- Title, exactly: `YAML keys in 3 dataset cards`
- Republish with the same title updates in place. No organisation, no other account, no upload script, no token step, no CLI.

**The three files, exactly three, all at the repo root**

1. `data.csv` — byte-for-byte copy of `tools/cardkeys/cardkeys/data.csv`. Header line exactly `dataset,source_url,key_order,key,read_status`; 44 data rows: `imdb` 14, `nyu-mll/glue` 16, `squad` 14. Copy it, do not retype it: any retyping risks changing a key string or a row order, and the self-test asserts the header and the counts. A card that was not read keeps one row with an empty `key`, empty `key_order` and `read_status` `NOT_READ`.

2. `README.md` — the dataset card, from `tools/cardkeys/cardkeys/README.md`, carrying:
   - keys only; **no key meanings verified**;
   - three cards only;
   - the three raw source URLs, listed as written:
     - https://huggingface.co/datasets/imdb/raw/main/README.md
     - https://huggingface.co/datasets/nyu-mll/glue/raw/main/README.md
     - https://huggingface.co/datasets/squad/raw/main/README.md
   - the short forum note text (title, the dataset link `https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards`, one line of limits)
   - the known mismatch: the step named `stanfordnlp/imdb`; the rows carry the id actually read (`imdb`) and its URL, and the mismatch is stated rather than smoothed over.

3. `self_test.py` — byte-for-byte copy of `tools/cardkeys/cardkeys/self_test.py`, at the repo root, standard library only, reading only the sibling `data.csv`.

This step also asks the card to carry the self-test output. That means `README.md` is *not* a strict byte-copy: one short section is appended. The two constraints cannot both hold exactly, so the appended section is the minimum possible — one heading and one indented line — and it is the only edit to that file.

**The self-test section, in one of two states (never a third)**

If the publish run executes `python3 self_test.py` from the repo root (the folder holding the three files) and its output contains an `OK:` line, paste that line verbatim under the heading — nothing added, nothing reworded:

```
## Self-test

Run from this dataset folder:

    python3 self_test.py

Captured run output (verbatim):

    OK: header matches, 44 rows, imdb=14 glue=16 squad=14
```

If the run did not happen, or its output contains no `OK:` line (a `FAIL:` line, an error, or nothing), the section reads:

```
## Self-test

Run from this dataset folder:

    python3 self_test.py

No self-test run was captured.
```

The line above is the one the drafted script prints on success. I did not run it and did not see it printed, so it is an expectation, **not** a captured result. If the run did not happen, that exact expectation line must not appear in the card anywhere; the second state is the honest one, and a card with no test claim is publishable.

**What the self-test checks** (so a failing run is informative, not a mystery): header equals `dataset,source_url,key_order,key,read_status` exactly; exactly 44 data rows; per-dataset counts `imdb` 14, `nyu-mll/glue` 16, `squad` 14; no fourth dataset id in column 1. It fails loudly rather than silently passing 44 rows split wrongly.

**Order of operations for the publish run**
1. Copy the three files verbatim; append the self-test section to `README.md`.
2. Run `python3 self_test.py` from that folder and keep its stdout.
3. Put the captured `OK:` line — or `No self-test run was captured.` — into the section.
4. Publish with the title above, three files, same repo path.

**Could not confirm**
- I could not open the three source URLs, so I could not check the byte contents of any of the three files; the counts and the header above come from the earlier build step's report.
- I could not run `python3 self_test.py`; no self-test result exists from me, and I make no claim that it passes.
- Whether the publish run can execute a script at all is not something I can settle here; if it cannot, the card goes out in the no-run state.

**Explain-with-media, this step:** it needs one image made at a standard tier. No image tool is in this step's capabilities, so no image was made and none is pasted into the card — no media, no fake placeholder. If one is wanted later, the caption line is: “cardkeys: one row per top-level YAML key in three public dataset cards.”

**Left for the owner / the publish run:** perform the three-file publish under `drifterpixel/` with the exact title, execute the self-test from the repo root, and paste whichever of the two section states matches the real output — then the forum note text already in the card can be posted.
