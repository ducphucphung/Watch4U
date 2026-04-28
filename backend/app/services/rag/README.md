# rag/

Owner: **Ryan**

Retrieval-Augmented Generation workflow for multilingual (English ↔ Vietnamese) medical Q&A and carer guidance.

## Scope

- Input: user query (EN or VI) + optional patient context
- Output: answer with citations, in the user's language
- Corpora (per A2): **ViMQ**, **VietMed-NER**, **ViMedical Disease**, plus English clinical references
- Embeddings: **PhoBERT** for VI, multilingual model for cross-lingual retrieval

## Suggested files

- `ingest.py` — chunk + embed corpus documents into the vector store
- `retriever.py` — hybrid search (BM25 + dense) with language-aware filtering
- `prompts.py` — system prompts, few-shot examples (EN + VI)
- `chain.py` — orchestration: retrieve → rerank → generate → cite
- `schemas.py` — local DTOs (or shared in `app/models/rag.py`)

## Notes

- A2 risk: API security for any third-party LLM calls — keep keys in `.env`, never in code.
- Always return citations; never let the model answer without grounded context.
