"""Health check endpoint — used by Docker healthcheck and uptime monitors."""
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "watch4u-backend"}
