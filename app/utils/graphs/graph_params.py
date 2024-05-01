from pydantic import BaseModel
from fastapi import Query


class GraphParams(BaseModel):
    hardware_id: str = Query(default=None, description="Hardware ID")
    limit: int = Query(50, description="Number of measurements from last record")




