from fastapi import APIRouter

from app.api.graphs.endpoints import (
    light
)


graphs_router = APIRouter()
graphs_router.include_router(light.router, prefix="/light", tags=["Light"])
