from fastapi import APIRouter

from app.api.v1.endpoints import (color)

api_router = APIRouter()
api_router.include_router(color.router, prefix="/color", tags=["Color"])
