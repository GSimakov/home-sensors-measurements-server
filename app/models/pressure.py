from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BasePressure', 'Pressure']


class BasePressure(BaseMeasurement):
    pass


class Pressure(BaseEntityModel, BasePressure, table=True):

    __tablename__ = 'Pressure'
    __table_args__ = {'extend_existing': True}