# Watch4U

**Context-Aware AI Fall Detection with Multilingual Staged Escalation for CALD Seniors**

41004 — Group 43A

## Project Structure

```
Watch4U/
├── backend/          FastAPI service — domain logic (Ryan, Muhamad)
├── streamlit_app/    Prototype UI — multi-page demo for each component
├── data/             Synthetic patient profiles + preprocessing (Affan)
└── frontend/         Future Next.js web app (placeholder)
```

## Quickstart

```bash
# Spin up backend + Streamlit prototype
make up

# Or start them individually
make backend       # FastAPI on http://localhost:8000
make streamlit     # Streamlit on http://localhost:8501

# Stop everything
make down
```

## Team & Component Ownership

| Component             | Owner(s)        | Path                                   |
|-----------------------|-----------------|----------------------------------------|
| RAG workflow          | Ryan            | `backend/app/services/rag/`            |
| Triage logic          | Jayce           | `backend/app/services/triage/`         |
| Fall detection (CV)   | Darrel          | `backend/app/services/fall_detection/` |
| Wi-Fi detection       | Ryan            | `backend/app/services/wifi_detection/` |
| Backend setup         | Ryan, Muhamad   | `backend/`                             |
| Synthetic data + prep | Affan           | `data/`                                |

## Roadmap

- **Phase 1 (now):** Streamlit prototype + FastAPI backend
- **Phase 2 (later):** Replace Streamlit with Next.js web app in `frontend/`
- The backend (`backend/app/services/`) stays unchanged across phases.

## Documents

- A1 — Plan and Proposal: `41004 A1.docx`
- A2 — Mid-Project Update: `41004 A2.docx`
