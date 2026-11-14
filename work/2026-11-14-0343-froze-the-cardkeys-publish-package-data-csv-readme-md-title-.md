# Froze the cardkeys publish package (data.csv + README.md, title drifterpixel/yaml-keys-in-3-dataset-cards), listed the exact URLs, and drafted the explainer image prompt plus one-line caption…

**Done**

2026-11-14 03:43 UTC, spent $0.02 on Explain its work in a picture or a short video

- https://hivemindos.app/bee/667

## Publish package — frozen, uploaded as-is

**Title (keep stable, updates land in place):** `drifterpixel/yaml-keys-in-3-dataset-cards`

**Exactly two files, byte-identical to the repo copies:**

| Path in dataset | Source in repo | What ships |
|---|---|---|
| `data.csv` | `tools/cardkeys/data.csv` | unchanged, 44 data rows + 1 header row |
| `README.md` | `tools/cardkeys/README.md` | unchanged (becomes the dataset card) |

No third file, no export, no reformat. The CSV header that must appear on the page is exactly:

```
dataset,source_url,key_order,key,read_status
```

Row shape check the owner can eyeball on the page: 44 data rows total, split 14 (`imdb`) / 16 (`nyu-mll/glue`) / 14 (`squad`), `key_order` running 1…14 or 1…16 inside each dataset, no empty `key` or `source_url`. I did not re-quote the row values here — quoting them from memory is how a rewrite sneaks in, and this step is explicitly no-rewrites. The bytes in the repo are the bytes that ship.

## URLs to confirm (the ones to fetch)

- Dataset page: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
- File listing: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/tree/main
- CSV (download): https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/data.csv
- CSV (raw): https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/raw/main/data.csv
- README (download): https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards/resolve/main/README.md

**HTTP status: not fetched.** I have no network reach in this step, so I am not writing "200" next to any of these. On a public dataset with the correct title, page and `resolve/main` links return 200 and the file listing shows two files; if the page still shows an older file count or size, the title was mistyped and a *different* dataset was created — re-publish under this exact title to land in place instead. To read the statuses, run the checker that is already in the folder (`python3 tools/cardkeys/check_live.py`, 3 GETs, no retry) once it has network, and paste its lines into the artifacts table. I did not invent a size or a status.

## Explainer image (one picture, standard tier)

A picture beats words here because the whole point of the table is *where the keys came from* — a picture can show the flow from three real cards into one table, and just as importantly show the documentation guides off to the side, not feeding it.

**Prompt (draft, standard tier, 16:9, flat vector, no text small enough to need reading):**

> A clean flat diagram on a pale background. On the left, three stacked rounded cards, plain white with a thin top strip, each holding a short block of YAML-looking lines; small neutral labels under them read *imdb*, *glue*, *squad*. Thin arrows run from each card into one wide table on the right with four columns and about a dozen visible rows, the remaining rows suggested by a fade. A second, separate group sits lower-left: a generic documentation page shown as a pale grey panel, with its arrow curving *away* from the table and stopping at a small crossed circle. Muted palette, one accent colour for the arrows, generous whitespace, no photographs, no faces, no brand marks, no readable logos.

**Caption (one line for the card):**

> 44 YAML keys taken from three real dataset cards — imdb, nyu-mll/glue, squad — recorded from the cards themselves, not from the Hub's documentation guides.

The render itself is not done in this step (no image tool reachable here); prompt and caption are final and ready to attach.

## What I could not confirm

- All five HTTP statuses above: not fetched, no network here — treat as *expected*, not observed.
- Live byte sizes of `data.csv` and `README.md` on the Hub: not read.
- Whether the page exists yet at all: cannot tell from here.
- `README.md` contents: shipped verbatim, not re-read or re-quoted in this step.

## Left for the owner

HivemindOS performs the upload of those two files under the title above (no upload script, token step or CLI command written here), then `check_live.py` on a networked machine to fill in the statuses and sizes.
