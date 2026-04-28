# triage/

Owner: **Jayce**

Clinical Decision Support System — turns a detected event + patient context into an urgency category and an alert plan.

## Scope

- Input: `{fall_event, patient_profile, vitals?, environment?}`
- Output: `{category: 1..5, recommended_action, escalation_steps[], rationale}`
- Reference: ATS / standard 1–5 emergency triage scale (Cat 1 = immediate, Cat 5 = non-urgent)

## Suggested files

- `rules.py` — deterministic rule layer (medication conflicts, comorbidities)
- `severity.py` — severity scoring (combines fall confidence + long-lie + risk profile)
- `escalation.py` — staged alert logic (carer → family → emergency services)
- `schemas.py` — local DTOs

## Notes

- Per A2: alarm fatigue is a key risk → tune thresholds with synthetic profiles before any live trial.
- Keep rules **explainable** — every category decision should return a rationale for the carer UI.
