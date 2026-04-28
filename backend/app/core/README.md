# core/

Shared infrastructure used by every service:

- `config.py` — environment / settings (Pydantic `BaseSettings`)
- (later) logging setup, constants, common types

Nothing here should import from `services/` or `routers/` — this is the bottom of the dependency graph.
