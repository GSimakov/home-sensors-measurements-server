from uuid import UUID
from app import models
import datetime

__all__ = ['ITemperatureCreate', 'ITemperatureRead']

base_model = models.BaseTemperature


class ITemperatureCreate(base_model):
    pass


class ITemperatureRead(base_model):
    id: UUID
    created_at: datetime.datetime
