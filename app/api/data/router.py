from fastapi import APIRouter

from app.api.data.endpoints import (
    color,
    flow_and_level,
    humidity,
    light,
    pressure,
    smoke_gas_alcohol,
    strain_and_weight,
    temperature
)



data_router = APIRouter()
data_router.include_router(color.router, prefix="/color", tags=["Color"])
data_router.include_router(flow_and_level.router, prefix="/flow_and_level", tags=["FlowAndLevel"])
data_router.include_router(humidity.router, prefix="/humidity", tags=["Humidity"])
data_router.include_router(light.router, prefix="/light", tags=["Light"])
data_router.include_router(pressure.router, prefix="/pressure", tags=["Pressure"])
data_router.include_router(smoke_gas_alcohol.router, prefix="/smoke_gas_alcohol", tags=["SmokeGasAlcohol"])
data_router.include_router(strain_and_weight.router, prefix="/strain_and_weight", tags=["StrainAndWeight"])
data_router.include_router(temperature.router, prefix="/temperature", tags=["Temperature"])


