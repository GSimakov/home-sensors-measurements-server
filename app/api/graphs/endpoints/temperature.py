from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask


from app import crud
from app import models
from app.api.graphs import deps
from app.utils.graphs.graph import graph
from app.utils.cleanup import cleanup

router = APIRouter()
crud_repo = crud.temperature
model = models.Temperature
deps_from_query = deps.get_temperature_multi_by_hardware_id_from_query


@router.get("")
async def get_temperature_graph(
        current_measurements: list[model] = Depends(
            deps_from_query
        ),
) -> FileResponse:
    """
    Gets a graphs of temperature measurements
    """

    file_path, file_name = await graph(
        measurements=current_measurements
    )

    return FileResponse(
        path=file_path,
        media_type='application/octet-stream',
        headers={
            'filename': file_name
        },
        background=BackgroundTask(cleanup, file_path)
    )
