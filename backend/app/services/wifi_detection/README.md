# wifi_detection/

Owner: **Ryan**

Wi-Fi Channel State Information (CSI) sensing for privacy-sensitive zones (bathrooms, bedrooms) where cameras are unacceptable.

## Scope

- Input: CSI samples streamed from ESP32 / commodity APs
- Output: motion / fall verdict with confidence — same envelope as `fall_detection`
- Hardware: ESP32-based CSI capture (per A2 — kit ordered)

## Suggested files

- `csi_ingest.py` — read live or recorded CSI streams
- `features.py` — denoise, extract amplitude/phase features
- `classifier.py` — model that maps features → motion/fall
- `schemas.py` — local DTOs

## Notes

- A2 risk: hardware delays. Keep a recorded-stream replay path so the rest of the pipeline can be developed without live hardware.
