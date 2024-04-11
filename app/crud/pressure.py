from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Pressure
create_schema = schemas.IPressureCreate


class CRUDPressure(CRUDBase[model, create_schema]):
    pass


pressure = CRUDPressure(model=model)
