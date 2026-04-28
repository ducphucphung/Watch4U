# Streamlit Prototype

The demo UI for Phase 1 — one page per backend component so each teammate has a place to show their work without stepping on anyone else.

## Run

```bash
# From repo root
make streamlit

# Or directly
cd streamlit_app
cp .env.example .env
pip install -r requirements.txt
streamlit run Home.py
```

Open http://localhost:8501.

## Layout

```
streamlit_app/
├── Home.py                 Landing page — project overview, links to demos
├── pages/
│   ├── 01_Fall_Detection.py     (Darrel)
│   ├── 02_Wifi_Detection.py     (Ryan)
│   ├── 03_Triage.py             (Jayce)
│   ├── 04_RAG_Chat.py           (Ryan)
│   └── 05_Patient_Profiles.py   (Affan)
├── components/             Shared Streamlit widgets
└── lib/
    └── api_client.py       Thin wrapper around the FastAPI backend
```

## Streamlit conventions

- Files in `pages/` auto-appear in the sidebar.
- The `NN_` numeric prefix controls order; underscores become spaces.
- All HTTP calls to the backend must go through `lib/api_client.py` — never hard-code URLs in pages.

## Roadmap

Phase 2 replaces this folder with `frontend/` (Next.js). The backend stays unchanged.
