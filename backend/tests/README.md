# tests/

Pytest suite for the backend. Mirror the `app/` structure:

```
tests/
├── conftest.py
├── test_health.py
├── services/
│   ├── test_fall_detection.py
│   ├── test_wifi_detection.py
│   ├── test_triage.py
│   └── test_rag.py
└── routers/
    └── ...
```

## Run

```bash
cd backend
pytest                       # all tests
pytest tests/services/       # one folder
pytest -k triage             # one keyword
```

Aim for **80%+ coverage** on every service before integrating it.
