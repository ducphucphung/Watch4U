# fall_detection/

Owner: **Darrel**

Spatio-temporal fall classification from video.

## Scope

- Input: video frames (file upload, RTSP stream, or pre-clipped events)
- Output: `{event_id, label, confidence, started_at, ended_at, "long_lie": bool}`
- Datasets: **FallVision** (audited in A2 — 11,732 clips), **OmniFall** for cross-dataset eval

## Suggested files

- `model.py` — model loader (YOLO / pose-based / 3D CNN — TBD)
- `pipeline.py` — frame ingest → preprocess → infer → post-process
- `long_lie.py` — sustained-pose / no-rise detector (post-fall confirmation)
- `schemas.py` — local DTOs (or put public ones in `app/models/fall.py`)

## Notes

- Keep model weights out of git — load from `data/` or a model registry.
- Privacy: never persist raw video by default; store events + thumbnails only.
