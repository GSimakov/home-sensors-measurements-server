from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.FlawAndLevel
create_schema = schemas.IFALCreate


class CRUDFAL(CRUDBase[model, create_schema]):
    pass


flaw_and_level = CRUDFAL(model=model)
