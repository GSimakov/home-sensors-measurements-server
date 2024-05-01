from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask

from app import crud
from app.utils.graphs.graph_params import GraphParams
from app.utils.graphs import graph
from app.utils.cleanup import cleanup

router = APIRouter()
crud_repo = crud.light


@router.get("")
async def get_light_graph(
        params: GraphParams = Depends(),
) -> FileResponse:
    """
    Gets a graphs of light measurements
    """
    file_path, file_name = await graph(
        limit=params.limit,
        hardware_id=params.hardware_id,
        current_repo=crud_repo
    )

    return FileResponse(
        path=file_path,
        media_type='application/octet-stream',
        filename=file_name,
        background=BackgroundTask(cleanup, file_path)
    )
