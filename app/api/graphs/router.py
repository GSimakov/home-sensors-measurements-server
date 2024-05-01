from fastapi import APIRouter

from app.api.graphs.endpoints import (
    light,
    color,
    flow_and_level,
    humidity,
    pressure,
    strain_and_weight,
    smoke_gas_alcohol,
    temperature
)


graphs_router = APIRouter()
graphs_router.include_router(light.router, prefix="/light", tags=["Light"])
graphs_router.include_router(color.router, prefix="/color", tags=["Color"])
graphs_router.include_router(flow_and_level.router, prefix="/flow_and_level", tags=["FlowAndLevel"])
graphs_router.include_router(humidity.router, prefix="/humidity", tags=["Humidity"])
graphs_router.include_router(pressure.router, prefix="/pressure", tags=["Pressure"])
graphs_router.include_router(strain_and_weight.router, prefix="/strain_and_weight", tags=["StrainAndWeight"])
graphs_router.include_router(smoke_gas_alcohol.router, prefix="/smoke_gas_alcohol", tags=["SmokeGasAlcohol"])
graphs_router.include_router(temperature.router, prefix="/temperature", tags=["Temperature"])

