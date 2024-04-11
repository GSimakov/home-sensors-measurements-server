from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from .base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseHumidity', 'HumidityUpdate', 'Humidity']


class BaseHumidity(BaseMeasurement):
    pass


class HumidityUpdate(BaseMeasurementUpdate):
    pass


class Humidity(BaseEntityModel, BaseHumidity, table=True):

    __tablename__ = 'Humidity'
    __table_args__ = {'extend_existing': True}