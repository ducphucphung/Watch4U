# data/

Owner: **Affan**

Synthetic patient profiles + preprocessing scripts. All public datasets (FallVision, OmniFall, ViMQ, etc.) live under git-ignored subfolders — only **code and small generated samples** belong in version control.

## Layout

```
data/
├── synthetic/        Synthetic patient profile generators + sample outputs
├── preprocessing/    Cleaning / feature-extraction scripts for each dataset
├── raw/              (git-ignored) Original downloads
└── processed/        (git-ignored) Derived / preprocessed artifacts
```

## Synthetic patient schema (per A2)

- Demographics, medical history, medications
- Functional status, fall history, emergency contacts
- Risk level: low / moderate / high

## Notes

- Per A2 risk: synthetic-bias must be tracked. Document generator assumptions in `synthetic/README.md`.
- This folder is mounted into both the backend and Streamlit containers at `/data`.
