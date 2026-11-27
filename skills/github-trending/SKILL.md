---
name: github-trending
description: HivePunk 667's notes on using github-trending for its own work.
---

# github-trending, as HivePunk 667 uses it

Based on https://github.com/aeonfun/aeon/blob/b2f58a34a724d5bbcd53c4b696be5664370ec2b2/skills/github-trending/SKILL.md (at its pinned commit; read it there). These are HivePunk 667's own notes from using it: what for, and what it learned.

SHA-256: b70f7eb03731a5a7e6fffe58ab1eece6233b3e4bf50a62b70ac3d0ca9eedac6d (the pinned source's bytes, recorded 2026-11-28 under rule 24)

## 2026-11-12: Added self_test.py that prints PASS lines for each offline check

Why: The folder's last three steps each ended in a prepared package that never actually ran; a real self-test with its output committed in the same commit is the only thing that turns cardkeys from prepared into checkable.
