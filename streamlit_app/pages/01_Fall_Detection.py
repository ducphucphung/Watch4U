"""Fall Detection demo (Darrel)."""
import streamlit as st

st.title("Fall Detection")
st.caption("Owner: Darrel · backend/app/services/fall_detection/")

st.info("Skeleton page. Wire up to `/api/fall-detection/...` when the service ships.")

st.markdown(
    """
    ### Planned demo

    - Upload a clip (or pick a sample from FallVision)
    - Backend returns `{label, confidence, long_lie}`
    - Show timeline of detected events with thumbnails
    """
)
