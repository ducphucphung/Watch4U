"""RAG Chat demo (Ryan)."""
import streamlit as st

st.title("RAG Chat")
st.caption("Owner: Ryan · backend/app/services/rag/")

st.info("Skeleton page. Wire up to `/api/rag/...` when the service ships.")

st.markdown(
    """
    ### Planned demo

    - Chat box that accepts EN or VI input
    - Backend retrieves from ViMQ / VietMed-NER / ViMedical Disease + EN refs
    - Render response with **citations**, language auto-detected
    """
)
