# preprocessing/

Cleaning and feature-extraction scripts for the public datasets used in Watch4U.

## Suggested files (one per dataset)

- `fallvision.py` — clip filtering, label normalisation (per A2 audit of 11,732 videos)
- `omnifall.py` — cross-dataset alignment with FallVision
- `vimq.py`, `vietmed_ner.py`, `vimedical_disease.py` — VI medical corpora cleanup for RAG

Each script should:

1. Read from `data/raw/<dataset>/`
2. Write to `data/processed/<dataset>/`
3. Log a `manifest.json` describing what it produced (counts, schema, version)

Inputs in `data/raw/` and outputs in `data/processed/` are **git-ignored** — only the scripts themselves are committed.
