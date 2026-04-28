# Backend — FastAPI

Owners: **Ryan, Muhamad**

The backend hosts all domain logic for Watch4U. The Streamlit prototype (and future Next.js app) call this service over HTTP — UI shells can be swapped without touching anything in `app/services/`.

## Run

```bash
# From repo root
make backend

# Or directly
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000/docs for the auto-generated Swagger UI.

## Layout

```
backend/
├── main.py                FastAPI app entrypoint
├── requirements.txt
├── Dockerfile
└── app/
    ├── core/              Settings, config, shared constants
    ├── models/            Pydantic schemas (request/response DTOs)
    ├── routers/           HTTP endpoints, one router per feature
    └── services/          Domain logic — one folder per teammate's component
        ├── fall_detection/    (Darrel) CV pipeline
        ├── wifi_detection/    (Ryan)   Wi-Fi CSI sensing
        ├── triage/            (Jayce)  Clinical severity / Cat 1–5 logic
        └── rag/                (Ryan)   Multilingual RAG workflow
```

## Adding a new endpoint

1. Define the request/response schema in `app/models/`
2. Add the business logic in `app/services/<your_component>/`
3. Wire it up to a router in `app/routers/`
4. Include the router in `main.py`
5. Add a test in `tests/`
