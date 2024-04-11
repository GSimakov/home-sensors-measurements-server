from uuid import UUID
import datetime
from app import models

__all__ = ['ILightCreate', 'ILightRead']

base_model = models.BaseLight


class ILightCreate(base_model):
    pass


class ILightRead(base_model):
    id: UUID
    created_at: datetime.datetime
