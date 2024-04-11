from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship


__all__ = ['BaseMeasurement', 'BaseMeasurementUpdate']


class BaseMeasurement(SQLModel):
    DAS_id: UUID | None
    indication: str


class BaseMeasurementUpdate(BaseMeasurement):
    DAS_id: UUID | None = None
    indication: str | None = None
