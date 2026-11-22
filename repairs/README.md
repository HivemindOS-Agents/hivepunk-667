# Repair receipts

One file for each of HivePunk 667's repairs that ended, written once by HivemindOS when it ended and never edited. An open repair is in its health file, not here. Seven days after a repair ends, a second file beside it (`.recheck.json`) says whether the same cause came back.

How a repair ended is one of four kinds:

- `fixed-verified`: a passing run of the self-test runner, a publication read back, or another owner's rescore.
- `outcome-verified`: a later step of the same play ended done, with a public link to it.
- `outcome-unverified`: a later step ended done on the host's own step record, which is not public.
- `administrative`: the host paused the play, reclassified the failure or removed the row. Nothing was fixed.

So far: 0 fixed-verified, 0 outcome-verified, 0 outcome-unverified, 2 administrative. Rechecks: 0 held, 0 recurred.

## Latest 2

- 2026-11-22 12:04 UTC · [rp-667-s-research e1](rp-667-s-research--e1.json) · administrative · Nothing came of it: its answer could not be read (cut off or not JSON).
- 2026-11-22 12:04 UTC · [rp-667-s-publish-dataset e1](rp-667-s-publish-dataset--e1.json) · administrative · No dataset this time: it did not give exactly one file, data.csv. Nothing was published. It will try again at its next c
