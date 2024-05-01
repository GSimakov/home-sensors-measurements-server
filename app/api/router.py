from fastapi import APIRouter

from app.api.v1.endpoints import (
    color,
    flow_and_level,
    humidity,
    light,
    pressure,
    smoke_gas_alcohol,
    strain_and_weight,
    temperature
)

api_router = APIRouter()
api_router.include_router(color.router, prefix="/color", tags=["Color"])
api_router.include_router(flow_and_level.router, prefix="/flow_and_level", tags=["FlowAndLevel"])
api_router.include_router(humidity.router, prefix="/humidity", tags=["Humidity"])
api_router.include_router(light.router, prefix="/light", tags=["Light"])
api_router.include_router(pressure.router, prefix="/pressure", tags=["Pressure"])
api_router.include_router(smoke_gas_alcohol.router, prefix="/smoke_gas_alcohol", tags=["SmokeGasAlcohol"])
api_router.include_router(strain_and_weight.router, prefix="/strain_and_weight", tags=["StrainAndWeight"])
api_router.include_router(temperature.router, prefix="/temperature", tags=["Temperature"])

