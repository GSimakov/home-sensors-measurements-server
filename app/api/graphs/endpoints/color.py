from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app import schemas
from app import models
from app import crud
from app.api.data import dependencies as deps
from app.utils.graph_params import GraphParams
from app.utils.graph import graph

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()
crud_repo = crud.color


@router.get("")
async def get_color_graph(
        params: GraphParams = Depends(),
):
    """
    Gets a graph of color measurements
    """
    file_path, file_name = await graph(
        limit=params.limit,
        hardware_id=params.hardware_id,
        current_repo=crud_repo
    )

    return FileResponse(file_path, media_type='application/octet-stream', filename=file_name)
