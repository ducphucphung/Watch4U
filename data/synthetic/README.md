# synthetic/

Generators that produce synthetic CALD-senior patient profiles for testing the triage pipeline without any real PHI.

## Suggested files

- `generate_profiles.py` — the main generator (CLI: `python generate_profiles.py --n 500 --out profiles.json`)
- `distributions.py` — age / comorbidity / medication priors (document sources!)
- `samples/` — a small committed sample (~10 profiles) so the prototype runs without regenerating

## Schema

Each profile contains:

- `id`, `age`, `sex`, `language` (en / vi / mixed)
- `medical_history[]`, `medications[]`
- `functional_status` (mobility, cognition)
- `fall_history[]`
- `emergency_contacts[]`
- `risk_level`: `"low" | "moderate" | "high"`

Document **every** prior used by the generator — A2 calls out synthetic bias as a key risk.
