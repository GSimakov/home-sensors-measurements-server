from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app import crud
from app.utils.graphs.graph_params import GraphParams
from app.utils.graphs import graph

router = APIRouter()
crud_repo = crud.color


@router.get("")
async def get_color_graph(
        params: GraphParams = Depends(),
):
    """
    Gets a graphs of color measurements
    """
    file_path, file_name = await graph(
        limit=params.limit,
        hardware_id=params.hardware_id,
        current_repo=crud_repo
    )

    return FileResponse(file_path, media_type='application/octet-stream', filename=file_name)
