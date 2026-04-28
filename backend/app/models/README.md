# models/

Pydantic schemas that describe the **shape of data crossing the API boundary** — request bodies, response payloads, shared DTOs.

Keep these dumb: no business logic, no DB access. Domain logic lives in `services/`.

Suggested files (create as needed):

- `fall.py` — fall event payloads (frame metadata, detection result, confidence)
- `triage.py` — patient state, severity category (Cat 1–5), recommended action
- `rag.py` — chat request/response, retrieved chunks, citations
- `wifi.py` — CSI signal sample, detection verdict
- `patient.py` — synthetic patient profile (mirrors `data/synthetic/`)
