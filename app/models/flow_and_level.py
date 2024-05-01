from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseFAL', 'FlowAndLevel']


class BaseFAL(BaseMeasurement):
    pass


class FlowAndLevel(BaseEntityModel, BaseFAL, table=True):

    __tablename__ = 'FlowAndLevel'
    __table_args__ = {'extend_existing': True}