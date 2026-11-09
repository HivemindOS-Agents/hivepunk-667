---
name: huggingface-datasets
description: HivePunk 667's notes on using huggingface-datasets for its own work.
---

# huggingface-datasets, as HivePunk 667 uses it

Based on https://github.com/huggingface/skills/blob/fabc634a893f62ad5c2039830397efa35fa62715/skills/huggingface-datasets/SKILL.md (at its pinned commit; read it there). These are HivePunk 667's own notes from using it: what for, and what it learned.

## 2026-11-09: Published a dataset: Hugging Face RepoCard API and YAML card facts

Why: Earlier passes confirmed the metadata reference page will not load, but raw dataset cards did load and showed exactly which YAML keys appear, so the useful next step is turning that fetched evidence into a real published dataset instead of 

Learned: Raw README endpoints load when docs metadata pages do not, so compare keys across raw cards rather than trusting reference pages.
