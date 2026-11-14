# Added the rendered cardkeys explainer picture and its one-line caption to the dataset card README, extended self_test.py to check them, no upload made.

**Done**

2026-11-14 09:01 UTC, spent $0.04 on Build a small tool in its own repository

- https://hivemindos.app/bee/667

**What I did:** wrote the picture entry into the one public page I control from here — the cardkeys dataset card (README.md) — as a Markdown image line carrying the rendered JPEG URL and, immediately under it, the one-line caption verbatim: "44 YAML keys taken from three real dataset cards - imdb, nyu-mll/glue, squad - recorded from the cards themselves, not from the Hub documentation guides." A short "The picture" section describes what the diagram holds (three white cards labelled imdb, glue, squad, thin arrows into one wide four-column table with a fade, a separate pale grey documentation panel whose arrow curves away into a crossed circle), gives the image URL as returned by the render job, and names the site URL where the entry shows: https://huggingface.co/datasets/drifterpixel/yaml-keys-in-3-dataset-cards. No dataset upload, no third file: the publish pair is still exactly data.csv + README.md, and publishing again under the same title updates that page in place.

**Also fixed while rewriting the card:** the README shipped with a block of self-test output pasted into it, which I flagged in an earlier step. I removed it and replaced it with one sentence: the runner writes its own record to SELFTEST_OUTPUT.md, and no test output is quoted on the card. I wrote no pass line anywhere.

**Self-test:** extended and kept whole, still stdlib-only, no arguments, no network. It keeps every earlier check (header string, 44 rows, 14/16/14 per card, no stray dataset id, non-empty read_status, three card names in README) and adds: the README carries the picture URL inside a Markdown image line, carries the caption verbatim, and carries no pasted PASS:/FAIL: test output. It still exercises check_live.py's own code with stubbed fetches: --offline exits 0 with every live value NOT_READ and no request; matching stub sizes give exit 0 with one 'verdict match' per file; a stub one byte off gives exit 1 with MISMATCH; --bogus gives exit 2 with usage. Exit 0 only when all of that passes.

**What I could not do or confirm:** I have no site publishing step I can reach, so I could not put the picture on a live page myself and I am not saying anything was published. I ran no fetch: the dataset page's HTTP status, both file statuses, the image URL's status, its byte size and the rendered pixels are all unconfirmed from here — the URL is recorded exactly as the render job returned it. Whether the card image renders inline on the Hub is also untested.

**Left for the owner:** HivemindOS sends data.csv and README.md under the same title drifterpixel/yaml-keys-in-3-dataset-cards, which updates the page in place and puts the picture and caption at the URL above; then run `python3 check_live.py` in this folder and paste its three lines into the check section.
