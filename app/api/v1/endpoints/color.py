from fastapi import APIRouter, status, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()

obj_in_message = 'Color'

model = models.Color
read_schema = schemas.IColorRead
create_schema = schemas.IColorCreate

crud_repo = crud.color

@router.get("/list")
async def read_color_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of color measurements
    """
    response = await crud_repo.get_multi_paginated(params=params)
    return create_response(data=response)


# @router.get("/{id}")
# async def get_color_by_id(
#         current: model = Depends(
#             deps_from_path
#         ),
# ) -> IGetResponseBase[read_schema]:
#     """
#     Gets a board by its id
#     """
#     return create_response(data=current)
#
#
# @router.put("/{id}")
# async def update_board_by_id(
#         update: update_schema,
#         current: model = Depends(
#             deps_from_path
#         ),
# ) -> IPutResponseBase[read_schema]:
#     """
#     Updates a board by id
#     """
#
#     updated = await crud.sensor.update(obj_current=current, obj_new=update)
#     return create_response(data=updated, message='{} updated'.format(obj_in_message))
#
#
# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_board(
#         create: create_schema
# ) -> IPostResponseBase[read_schema]:
#     """
#     Creates a new board
#     """
#     created = await crud_repo.create(obj_in=create)
#     return create_response(data=created, message='{} created'.format(obj_in_message))
#
#
# @router.delete("/{id}")
# async def remove_board(
#         current: model = Depends(
#             deps_from_path
#         ),
# ) -> IDeleteResponseBase[read_schema]:
#     """
#     Deletes a board by id
#     """
#
#     deleted = await crud_repo.remove(id=current.id)
#     return create_response(data=deleted, message="{} removed".format(obj_in_message))