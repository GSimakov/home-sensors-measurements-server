from fastapi import APIRouter, status, Depends, Query
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.data import deps

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()

obj_in_message = 'Pressure'
model = models.Pressure
read_schema = schemas.IPressureRead
create_schema = schemas.IPressureCreate
crud_repo = crud.pressure
deps_by_id = deps.get_pressure_by_id_from_path


@router.get("/list")
async def read_pressure_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of pressure measurements
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/list_hid")
async def read_pressure_list_by_hardware_id(
        hardware_id: str = Query(description='Hardware ID of the measurements source'),
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of pressure measurements by hardware id
    """
    response = await crud_repo.get_multi_paginated_by_hardware_id(params=params, hardware_id=hardware_id)
    return create_response(data=response)


@router.get("/{id}")
async def get_pressure_by_id(
        current: model = Depends(
            deps_by_id
        ),
) -> IGetResponseBase[read_schema]:
    """
    Gets a pressure measurement by its id
    """
    return create_response(data=current)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_pressure(
        create: create_schema
) -> IPostResponseBase[read_schema]:
    """
    Creates a new pressure measurement
    """
    created = await crud_repo.create(obj_in=create)
    return create_response(data=created, message='{} created'.format(obj_in_message))


@router.delete("/{id}")
async def remove_pressure(
        current: model = Depends(
            deps_by_id
        ),
) -> IDeleteResponseBase[read_schema]:
    """
    Deletes a pressure measurement by id
    """

    deleted = await crud_repo.remove(id=current.id)
    return create_response(data=deleted, message="{} removed".format(obj_in_message))
