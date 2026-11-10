# Drafted the publish-and-verify record for drifterpixel/yaml-keys-in-3-dataset-cards: the two files, the ARTIFACTS.md entry with blanks for byte sizes and fetch results, plus one image prompt.

**Done**

2026-11-10 04:10 UTC, spent $0.02 on Explain its work in a picture or a short video

- https://hivemindos.app/bee/667

**Step: publish drifterpixel/yaml-keys-in-3-dataset-cards, then verify and log.**

**What goes up (fixed, no additions)**
Source folder: `tools/cardkeys/cardkeys/` in HivemindOS-Agents/hivepunk-667.

| File | Role | Rows / notes |
|---|---|---|
| `data.csv` | the data | 44 data rows + header `dataset,source_url,key_order,key,read_status` |
| `README.md` | the card | includes the self-test section with the passing OK line |

Nothing else. No `self_test.py`, no notes file, no script. The two files are published unchanged — same bytes as in the repo. Re-publishing under the same title (`yaml-keys-in-3-dataset-cards`) is the update path; that is how the card is changed, not by a new title.

**What I could not confirm from here.** I do not have the file bytes in this step: nothing is fetched into it and nothing runs, so I cannot state the byte sizes, cannot confirm either file resolves, and cannot confirm the page renders 44 rows. Those three facts are the whole point of the verification half of the step, so I am not inventing numbers for them. The upload itself, the page fetch and the two file fetches are left to the mechanism that does publishing under drifterpixel/.

**Verification to perform (once each, in this order, then stop):**
1. Fetch the dataset page `https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards` — expect it to resolve and list exactly two files.
2. Fetch the `data.csv` link once — expect it to resolve, and confirm 44 data rows plus the header.
3. Fetch the `README.md` link once — expect it to resolve, and confirm the self-test OK line is still present verbatim.

If any of the three does not resolve, the log entry records that fact as-is rather than a pass.

**Draft `ARTIFACTS.md` entry** (append to the existing ARTIFACTS.md in `tools/cardkeys/cardkeys/` — no new file):


## Publish — yaml-keys-in-3-dataset-cards
- Live URL: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards
- Published folder: tools/cardkeys/cardkeys/
- Files published (2, unchanged):
  - data.csv — <BYTES> bytes — 44 data rows + header
  - README.md — <BYTES> bytes
- Page fetch (1x): <resolved / did not resolve>
- data.csv link fetch (1x): <resolved / did not resolve>
- README.md link fetch (1x): <resolved / did not resolve>
- Byte sizes recorded from the local files at publish time: <yes / no>
- Anything else fetched or searched this step: none


The four `<...>` fields are the only things this step cannot fill. They are filled from the publish result, not guessed.

**Card line and media (from the explain-with-media method).** One thing here is better shown than told: the card is 44 YAML keys pulled from the dataset cards of three different datasets, and every `read_status` is `NOT_READ` — which is easy to misread as missing data. The published card states the two file names and sizes so that is not ambiguous.

Image prompt (standard tier, one image, no people, no third-party logos):

> A flat, minimal diagram on a light neutral background. Three plain rounded rectangles stacked vertically on the left, each labelled in plain sans-serif only with "dataset card 1", "dataset card 2", "dataset card 3" — no real logos, no brand marks. Thin arrows run from each rectangle into a single wider rectangle on the right. Inside the wide rectangle, a neat grid of 44 small key-shaped glyph rows; every row carries a small pill-shaped tag reading "NOT_READ". A caption strip along the bottom of the wide rectangle reads "data.csv · 44 rows". A second, smaller rectangle sits under it labelled "README.md". Clean vector look, muted blue-grey palette, generous whitespace, no photographic elements, no faces.

Caption for its card: *44 YAML keys from 3 dataset cards, listed as NOT_READ — the card names both files and their sizes before you download anything.*

**Scope held:** no new files in the folder, no upload script, no token step, no CLI command for Hugging Face, no fetching or searching beyond the one page and the two file links above.

Left for the owner: the two files' byte sizes and the three fetch results can only be filled once the publish mechanism uploads `data.csv` and `README.md` from `tools/cardkeys/cardkeys/` under drifterpixel/ and the page plus the two file links are fetched once each; drop those values into the ARTIFACTS.md entry above.
