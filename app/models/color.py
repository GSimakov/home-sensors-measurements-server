from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from .base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseColor', 'ColorUpdate', 'Color']


class BaseColor(BaseMeasurement):
    pass


class ColorUpdate(BaseMeasurementUpdate):
    pass


class Color(BaseEntityModel, BaseColor, table=True):

    __tablename__ = 'Color'
    __table_args__ = {'extend_existing': True}