from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseLight', 'Light']


class BaseLight(BaseMeasurement):
    pass


class Light(BaseEntityModel, BaseLight, table=True):

    __tablename__ = 'Light'
    __table_args__ = {'extend_existing': True}