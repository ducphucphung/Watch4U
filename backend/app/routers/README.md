# routers/

HTTP-facing layer. Each file owns one feature's endpoints and **delegates all logic to `services/`** — routers should be thin.

Pattern per feature:

```python
# app/routers/triage.py
from fastapi import APIRouter
from app.models.triage import TriageRequest, TriageResponse
from app.services.triage import classify

router = APIRouter(tags=["triage"])

@router.post("/classify", response_model=TriageResponse)
async def classify_endpoint(req: TriageRequest) -> TriageResponse:
    return classify(req)
```

Suggested routers (create as the work lands):

- `health.py` ✅ already created
- `fall_detection.py` (Darrel)
- `wifi_detection.py` (Ryan)
- `triage.py` (Jayce)
- `rag.py` (Ryan)
