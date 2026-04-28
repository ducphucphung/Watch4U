# frontend/

**Phase 2 placeholder.** The Streamlit prototype in `streamlit_app/` is the active UI for now.

When we're ready to build the production web app, this folder will hold a Next.js project (similar stack to `~/Documents/fpt-llm/frontend`):

- Next.js 16 + React 19, TypeScript
- pnpm workspace, Tailwind, Radix UI primitives
- Zustand for state
- Talks to the **same** FastAPI backend — `app/services/` does not change

Until then, leave this folder empty save for this README.
