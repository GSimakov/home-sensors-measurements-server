from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseFAL', 'FALUpdate', 'FlawAndLevel']


class BaseFAL(BaseMeasurement):
    pass


class FALUpdate(BaseMeasurementUpdate):
    pass


class FlawAndLevel(BaseEntityModel, BaseFAL, table=True):

    __tablename__ = 'FlawAndLevel'
    __table_args__ = {'extend_existing': True}