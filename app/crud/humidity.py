from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Humidity
create_schema = schemas.IHumidityCreate


class CRUDHumidity(CRUDBase[model, create_schema]):
    pass


humidity = CRUDHumidity(model=model)
