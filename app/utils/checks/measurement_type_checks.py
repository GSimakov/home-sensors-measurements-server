from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['measurements_type_name_is_taken', 'measurements_type_is_exist']

crud_repo = crud.measurement_type
model = models.MeasurementType


async def measurements_type_name_is_taken(name: str) -> None:
    obj = await crud_repo.get_by_name(name=name)
    if obj:
        raise NameExistException(model=model, name=name)


async def measurements_type_is_exist(id: UUID) -> None:
    obj = await crud_repo.get(id=id)
    if not obj:
        raise IdNotFoundException(model=model, id=id)
