from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship

from .base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseSAW', 'SAWUpdate', 'StrainAndWeight']


class BaseSAW(BaseMeasurement):
    pass


class SAWUpdate(BaseMeasurementUpdate):
    pass


class StrainAndWeight(BaseEntityModel, BaseSAW, table=True):

    __tablename__ = 'StrainAndWeight'
    __table_args__ = {'extend_existing': True}