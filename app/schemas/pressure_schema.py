from uuid import UUID
from app import models
import datetime

__all__ = ['IPressureCreate', 'IPressureRead']

base_model = models.BasePressure


class IPressureCreate(base_model):
    pass


class IPressureRead(base_model):
    id: UUID
    created_at: datetime.datetime
