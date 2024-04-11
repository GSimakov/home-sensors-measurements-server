from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from .base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseSGA', 'SGAUpdate', 'SmokeGasAlcohol']


class BaseSGA(BaseMeasurement):
    pass


class SGAUpdate(BaseMeasurementUpdate):
    pass


class SmokeGasAlcohol(BaseEntityModel, BaseSGA, table=True):

    __tablename__ = 'SmokeGasAlcohol'
    __table_args__ = {'extend_existing': True}