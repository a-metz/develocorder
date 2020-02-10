import time
from itertools import count

import numpy as np

from develocorder import (
    LinePlot,
    Heatmap,
    FilteredLinePlot,
    DownsampledLinePlot,
    set_recorder,
    record,
    set_update_period,
    set_num_columns,
)


def run_example():
    # axis labels
    set_recorder(labeled=LinePlot(xlabel="Step", ylabel="Score"))

    # additional filtered values (window filter)
    set_recorder(filtered=FilteredLinePlot(filter_size=50, xlabel="(Filtered)"))

    # maximum history length
    set_recorder(detail=LinePlot(max_length=50, xlabel="(Detail)"))

    # downsampled values (record mean of every filter_size values)
    set_recorder(downsampled=DownsampledLinePlot(filter_size=5, xlabel="(Downsampled)"))

    # multiple curves for recording 1d-array values
    set_recorder(multiple=FilteredLinePlot(filter_size=50, xlabel="(Multiple)"))

    # heatmap for recording 1d-array values
    set_recorder(heatmap=Heatmap(xlabel="(Heatmap)"))

    # minimum update period (limit update rate for better performance)
    set_update_period(0.5)  # [seconds]

    # set number of columns
    set_num_columns(2)

    # example value generators
    score_gen = score_values()
    loss_gen = loss_values()
    multiple = array_values(3)
    heatmap = array_values(8)

    for _ in range(50):
        record(labeled=next(score_gen))
        for _ in range(20):
            loss = next(loss_gen)
            record(filtered=loss, downsampled=loss, detail=loss)
            record(multiple=next(multiple), heatmap=next(heatmap))
            time.sleep(0.01)


def loss_values(random=np.random.RandomState(0)):
    for i in count():
        yield 10 / (pow(i / 10, 0.5) + 1) * (1 + 0.3 * random.standard_normal())


def score_values(random=np.random.RandomState(0)):
    for i in count():
        yield i * (1 + 0.1 * random.standard_normal())


def array_values(dimensions, random=np.random.RandomState(17)):
    factor = random.random(dimensions) * 0.001
    for i in count():
        yield factor * i * (1 + 0.1 * random.standard_normal(dimensions))


if __name__ == "__main__":
    run_example()
    input("Press Enter to exit...")
