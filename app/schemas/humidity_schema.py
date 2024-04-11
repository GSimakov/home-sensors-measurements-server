from uuid import UUID
from app import models

__all__ = ['IHumidityCreate', 'IHumidityRead']

base_model = models.BaseHumidity


class IHumidityCreate(base_model):
    pass


class IHumidityRead(base_model):
    id: UUID