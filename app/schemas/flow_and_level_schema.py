from uuid import UUID
from app import models

__all__ = ['IFALCreate', 'IFALRead']

base_model = models.BaseFAL


class IFALCreate(base_model):
    pass


class IFALRead(base_model):
    id: UUID
