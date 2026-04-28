"""Thin HTTP client for the FastAPI backend.

All Streamlit pages MUST go through this module — never hard-code the backend URL
or build requests inline. That way Phase 2 (Next.js) only has to mirror this contract.
"""
import os

import httpx

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
TIMEOUT = httpx.Timeout(30.0, connect=5.0)


def health() -> dict:
    """Backend liveness probe."""
    with httpx.Client(base_url=BACKEND_URL, timeout=TIMEOUT) as client:
        r = client.get("/health")
        r.raise_for_status()
        return r.json()


def get(path: str, **params) -> dict:
    with httpx.Client(base_url=BACKEND_URL, timeout=TIMEOUT) as client:
        r = client.get(path, params=params)
        r.raise_for_status()
        return r.json()


def post(path: str, json: dict | None = None) -> dict:
    with httpx.Client(base_url=BACKEND_URL, timeout=TIMEOUT) as client:
        r = client.post(path, json=json or {})
        r.raise_for_status()
        return r.json()
