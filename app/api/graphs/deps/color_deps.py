from fastapi import Query

from app import crud
from app import models
from app.utils.exceptions import ResultIsEmptyException

__all__ = ['get_color_multi_by_hardware_id_from_query']

model = models.Color
crud_repo = crud.color
HID_param_description = 'Hardware ID of the measurements source'
limit_param_description = 'Number of measurements from last record'


async def get_color_multi_by_hardware_id_from_query(
        hardware_id: str = Query(description=HID_param_description),
        limit: int = Query(default=50, description=limit_param_description)
) -> list:
    response = await crud_repo.get_multi_by_hardware_id(hardware_id=hardware_id, limit=limit)
    if not response:
        raise ResultIsEmptyException(model=model, param='hardware_id', param_value=hardware_id)
    return response
