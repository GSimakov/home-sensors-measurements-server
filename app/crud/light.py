from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Light
create_schema = schemas.ILightCreate


class CRUDLight(CRUDBase[model, create_schema]):
    pass


light = CRUDLight(model=model)
