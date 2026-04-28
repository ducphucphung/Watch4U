"""Watch4U — Streamlit landing page.

Phase 1 prototype. Each demo lives under `pages/` and is auto-listed in the sidebar.
"""
import streamlit as st

st.set_page_config(page_title="Watch4U", page_icon="🩺", layout="wide")

st.title("Watch4U")
st.subheader("Context-Aware AI Fall Detection with Multilingual Staged Escalation")
st.caption("41004 — Group 43A")

st.markdown(
    """
    Use the sidebar to open each component demo:

    1. **Fall Detection** — video-based fall classification (Darrel)
    2. **Wi-Fi Detection** — CSI-based motion sensing for privacy zones (Ryan)
    3. **Triage** — Category 1–5 clinical severity + alert staging (Jayce)
    4. **RAG Chat** — multilingual EN/VI medical Q&A (Ryan)
    5. **Patient Profiles** — synthetic EHR data + preprocessing (Affan)

    All pages call the FastAPI backend at `BACKEND_URL` via `lib/api_client.py`.
    """
)

with st.expander("Project status"):
    st.markdown(
        """
        - **Phase 1 (now):** This Streamlit prototype + FastAPI backend
        - **Phase 2 (later):** Next.js web app replaces this prototype; backend unchanged
        """
    )
