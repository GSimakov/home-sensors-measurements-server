from uuid import UUID
from fastapi import Query, Body, Path
from typing_extensions import Annotated

from app import crud
from app import models
from app.utils.exceptions import IdNotFoundException

__all__ = ['get_light_multi_by_hardware_id_from_query']

model = models.Light
crud_repo = crud.light
HID_param_description = 'Hardware ID of the measurements source'
limit_param_description = 'Number of measurements from last record"'


async def get_light_multi_by_hardware_id_from_query(
        hardware_id: str = Query(description=HID_param_description),
        limit: int = Query(default=50, description=limit_param_description)
) -> list:
    return await crud_repo.get_multi_by_hardware_id(hardware_id=hardware_id, limit=limit)
