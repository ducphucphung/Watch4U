# services/

All domain logic lives here. Each subfolder is owned by one (or two) teammates and is independent — no cross-imports between sibling services. If two services need to talk, they do it through clean function calls or shared models in `app/models/`.

| Folder              | Owner(s)        | What it does                                     |
|---------------------|-----------------|--------------------------------------------------|
| `fall_detection/`   | Darrel          | CV pipeline — classify fall events from video    |
| `wifi_detection/`   | Ryan            | Wi-Fi CSI sensing for privacy zones (bathrooms)  |
| `triage/`           | Jayce           | Clinical severity → Category 1–5, alert staging  |
| `rag/`              | Ryan            | Multilingual RAG (EN ↔ VI) over medical corpora  |

## Why this layout

The Streamlit prototype today and the Next.js app tomorrow both call the same HTTP routers, which call these services. **None of this code changes when the UI swaps.**
