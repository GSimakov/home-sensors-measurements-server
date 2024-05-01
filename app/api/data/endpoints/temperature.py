from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.data import dependencies as deps

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()

obj_in_message = 'Temperature'
model = models.Temperature
read_schema = schemas.ITemperatureRead
create_schema = schemas.ITemperatureCreate
crud_repo = crud.temperature
deps_from_path = deps.get_temperature_by_id_from_path


@router.get("/list")
async def read_temperature_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of temperature measurements
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_temperature_by_id(
        current: model = Depends(
            deps_from_path
        ),
) -> IGetResponseBase[read_schema]:
    """
    Gets a temperature measurement by its id
    """
    return create_response(data=current)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_temperature(
        create: create_schema
) -> IPostResponseBase[read_schema]:
    """
    Creates a new temperature measurement
    """
    created = await crud_repo.create(obj_in=create)
    return create_response(data=created, message='{} created'.format(obj_in_message))


@router.delete("/{id}")
async def remove_temperature(
        current: model = Depends(
            deps_from_path
        ),
) -> IDeleteResponseBase[read_schema]:
    """
    Deletes a temperature measurement by id
    """

    deleted = await crud_repo.remove(id=current.id)
    return create_response(data=deleted, message="{} removed".format(obj_in_message))