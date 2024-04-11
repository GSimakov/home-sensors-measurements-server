from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Temperature
create_schema = schemas.ITemperatureCreate


class CRUDTemperature(CRUDBase[model, create_schema]):
    pass


temperature = CRUDTemperature(model=model)
