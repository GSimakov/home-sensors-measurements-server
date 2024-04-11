from app.utils.base_measurement_model import *
from app.utils.base_model import BaseEntityModel

__all__ = ['BaseSGA', 'SmokeGasAlcohol']


class BaseSGA(BaseMeasurement):
    pass


class SmokeGasAlcohol(BaseEntityModel, BaseSGA, table=True):

    __tablename__ = 'SmokeGasAlcohol'
    __table_args__ = {'extend_existing': True}