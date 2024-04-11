from uuid import UUID
import datetime
from app import models

__all__ = ['IHumidityCreate', 'IHumidityRead']

base_model = models.BaseHumidity


class IHumidityCreate(base_model):
    pass


class IHumidityRead(base_model):
    id: UUID
    created_at: datetime.datetime
