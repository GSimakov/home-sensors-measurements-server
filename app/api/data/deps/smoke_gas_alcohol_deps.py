from uuid import UUID
from fastapi import Query, Body, Path
from typing_extensions import Annotated

from app import crud
from app import models
from app.utils.exceptions import IdNotFoundException

__all__ = ['get_sga_by_id_from_path', 'get_sga_by_id_from_query']

model = models.SmokeGasAlcohol
crud_repo = crud.smoke_gas_alcohol
id_param_description = 'The UUID id of the SGA measurement'


async def get(id: UUID) -> model:
    response = await crud_repo.get(id=id)
    if not response:
        raise IdNotFoundException(model=model, id=id)
    return response


async def get_sga_by_id_from_path(
        id: Annotated[UUID, Path(description=id_param_description)]
) -> model:
    return await get(id=id)


async def get_sga_by_id_from_query(
        id: Annotated[UUID, Query(description=id_param_description)]
) -> model:
    return await get(id=id)