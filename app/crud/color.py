from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.Color
create_schema = schemas.IColorCreate


class CRUDColor(CRUDBase[model, create_schema]):
    pass


color = CRUDColor(model=model)
