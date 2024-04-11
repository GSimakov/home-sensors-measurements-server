from uuid import UUID
from app import models
import datetime

__all__ = ['ISAWCreate', 'ISAWRead']

base_model = models.BaseSAW


class ISAWCreate(base_model):
    pass


class ISAWRead(base_model):
    id: UUID
    created_at: datetime.datetime
