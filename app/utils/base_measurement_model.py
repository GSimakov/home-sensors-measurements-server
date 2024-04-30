from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship


__all__ = ['BaseMeasurement']


class BaseMeasurement(SQLModel):
    hardware_id: str
    indication: str
    unit: str

