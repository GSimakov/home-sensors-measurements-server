import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import numpy as np


from app import crud
from app.utils.date_format import DateFormat


async def graph(
        date_format: str = DateFormat.YMDHMSM,
):

    x = []
    y = []

    iter = 0

    measurements = await crud.light.get_multi_by_hardware_id(hardware_id='GARSHOKSINII', limit=100)
    for measurement in measurements:
        y.append(round(float(measurement.indication), 2))
        x.append(str(measurement.created_at.strftime(date_format)[:-3]))

    plt.style.use("ggplot")
    plt.figure(figsize=(50, 20))
    plt.yticks(np.arange(min(y), max(y) + 1, 0.5))
    plt.ylabel(ylabel="Показания ({})".format(measurements[0].unit), loc='top')
    plt.xlabel(xlabel="Время", loc="left")
    plt.plot(x, y)
    plt.xticks(rotation=90)

    filename = '{}-{}_{}.png'.format(min(x), max(x), measurements[0].hardware_id)
    plt.savefig(filename)

    return filename
