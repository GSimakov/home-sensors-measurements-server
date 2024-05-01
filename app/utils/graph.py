import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import numpy as np
from app.crud.base import CRUDBase


from app import crud
from app.utils.date_format import DateFormat


async def graph(
        limit: int,
        hardware_id: str,
        current_repo: CRUDBase,
        date_format: str = DateFormat.YMDHMSM,

):

    x = []
    y = []
    graph = plt #todo optimization

    iter = 0

    measurements = await current_repo.get_multi_by_hardware_id(hardware_id=hardware_id, limit=limit)
    for measurement in measurements:
        y.append(round(float(measurement.indication), 2))
        x.append(str(measurement.created_at.strftime(date_format)[:-3]))

    graph.style.use("ggplot")
    graph.figure(figsize=(50, 20))
    graph.yticks(np.arange(min(y), max(y) + 1, 0.5))
    graph.ylabel(ylabel="Показания ({})".format(measurements[0].unit), loc='top')
    graph.xlabel(xlabel="Время", loc="left")
    graph.plot(x, y)
    graph.xticks(rotation=90)

    file_name = '{}-{}_{}.png'.format(min(x), max(x), measurements[0].hardware_id)
    file_path = './pictures/' + file_name
    graph.savefig(file_path)
    return file_path, file_name
