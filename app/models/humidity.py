from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseHumidity', 'Humidity']


class BaseHumidity(BaseMeasurement):
    pass


class Humidity(BaseEntityModel, BaseHumidity, table=True):

    __tablename__ = 'Humidity'
    __table_args__ = {'extend_existing': True}