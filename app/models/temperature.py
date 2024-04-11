from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseTemperature', 'TemperatureUpdate', 'Temperature']


class BaseTemperature(BaseMeasurement):
    pass


class TemperatureUpdate(BaseMeasurementUpdate):
    pass


class Temperature(BaseEntityModel, BaseTemperature, table=True):

    __tablename__ = 'Temperature'
    __table_args__ = {'extend_existing': True}
