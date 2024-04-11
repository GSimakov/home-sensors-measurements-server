from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.crud.base import CRUDBase
from app import schemas
from app import models
from app.utils.session import session_manager

model = models.StrainAndWeight
create_schema = schemas.ISAWCreate


class CRUDSAW(CRUDBase[model, create_schema]):
    pass


strain_and_weight = CRUDSAW(model=model)
