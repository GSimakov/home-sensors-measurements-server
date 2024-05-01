from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud
from app.api.data import deps as deps

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()

obj_in_message = 'Flow And Level'
model = models.FlawAndLevel
read_schema = schemas.IFALRead
create_schema = schemas.IFALCreate
crud_repo = crud.flaw_and_level
deps_from_path = deps.get_fal_by_id_from_path


@router.get("/list")
async def read_fav_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of flow and level measurements
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)


@router.get("/{id}")
async def get_fav_by_id(
        current: model = Depends(
            deps_from_path
        ),
) -> IGetResponseBase[read_schema]:
    """
    Gets a flow and level measurement by its id
    """
    return create_response(data=current)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_fav(
        create: create_schema
) -> IPostResponseBase[read_schema]:
    """
    Creates a new flow and level measurement
    """
    created = await crud_repo.create(obj_in=create)
    return create_response(data=created, message='{} created'.format(obj_in_message))


@router.delete("/{id}")
async def remove_fav(
        current: model = Depends(
            deps_from_path
        ),
) -> IDeleteResponseBase[read_schema]:
    """
    Deletes a flow and level measurement by id
    """

    deleted = await crud_repo.remove(id=current.id)
    return create_response(data=deleted, message="{} removed".format(obj_in_message))
