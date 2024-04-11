import datetime
from uuid import UUID
from app import models

__all__ = ['IColorCreate', 'IColorRead']

base_model = models.BaseColor


class IColorCreate(base_model):
    pass


class IColorRead(base_model):
    id: UUID
    created_at: datetime.datetime
