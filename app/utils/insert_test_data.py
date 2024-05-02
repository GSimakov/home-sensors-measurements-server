import random

from app import crud, schemas


async def insert():
    for i in range(50):
        create_schema_light = schemas.ILightCreate(
            hardware_id='3',
            indication=str(random.uniform(20.0, 44.0)),
            unit='люкс'
        )
        await crud.light.create(obj_in=create_schema_light)
