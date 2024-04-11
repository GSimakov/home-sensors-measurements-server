from uuid import UUID
from app import models

__all__ = ['ISGACreate', 'ISGARead']

base_model = models.BaseSGA


class ISGACreate(base_model):
    pass


class ISGARead(base_model):
    id: UUID