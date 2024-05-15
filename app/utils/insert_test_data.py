import random

from app import crud, schemas


async def insert():
    for i in range(50):
        create_schema_light = schemas.ISAWCreate(
            hardware_id='3SAW',
            indication=str(random.uniform(20.0, 47.0)),
            unit='кг'
        )
        await crud.strain_and_weight.create(obj_in=create_schema_light)

    for i in range(50):
        create_schema_light = schemas.ILightCreate(
            hardware_id='3Light',
            indication=str(random.uniform(20.0, 44.0)),
            unit='люкс'
        )
        await crud.light.create(obj_in=create_schema_light)


    for i in range(50):
        create_schema_light = schemas.ISGACreate(
            hardware_id='3SGA',
            indication=str(random.uniform(20.0, 44.0)),
            unit='промиль'
        )
        await crud.smoke_gas_alcohol.create(obj_in=create_schema_light)


    for i in range(50):
        create_schema_light = schemas.IFALCreate(
            hardware_id='3FAL',
            indication=str(random.uniform(20.0, 44.0)),
            unit='%'
        )
        await crud.flow_and_level.create(obj_in=create_schema_light)

    for i in range(50):
        create_schema_light = schemas.IColorCreate(
            hardware_id='3Color',
            indication=str(random.uniform(20.0, 44.0)),
            unit='RED'
        )
        await crud.color.create(obj_in=create_schema_light)


    for i in range(50):
        create_schema_light = schemas.IPressureCreate(
            hardware_id='3Pressure',
            indication=str(random.uniform(20.0, 44.0)),
            unit='ед.'
        )
        await crud.pressure.create(obj_in=create_schema_light)

    for i in range(50):
        create_schema_light = schemas.ITemperatureCreate(
            hardware_id='3Temperature',
            indication=str(random.uniform(20.0, 44.0)),
            unit='C'
        )
        await crud.temperature.create(obj_in=create_schema_light)

    for i in range(50):
        create_schema_light = schemas.IHumidityCreate(
            hardware_id='3Humidity',
            indication=str(random.uniform(20.0, 44.0)),
            unit='%'
        )
        await crud.humidity.create(obj_in=create_schema_light)