"""Triage demo (Jayce)."""
import streamlit as st

st.title("Triage")
st.caption("Owner: Jayce · backend/app/services/triage/")

st.info("Skeleton page. Wire up to `/api/triage/classify` when the service ships.")

st.markdown(
    """
    ### Planned demo

    - Pick a synthetic patient profile + simulated fall event
    - Backend returns `{category: 1..5, recommended_action, escalation_steps, rationale}`
    - Show the staged-escalation timeline (carer → family → emergency services)
    """
)
