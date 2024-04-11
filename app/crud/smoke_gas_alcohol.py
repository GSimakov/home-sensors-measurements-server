from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.SmokeGasAlcohol
create_schema = schemas.ISGACreate


class CRUDSGA(CRUDBase[model, create_schema]):
    pass


smoke_gas_alcohol = CRUDSGA(model=model)
