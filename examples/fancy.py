import time

import numpy as np

from develocorder import (
    LinePlot,
    Heatmap,
    DownsampledLinePlot,
    set_recorder,
    record,
    set_update_period,
    set_num_columns,
)


def run_example():
    # filter values (window filter kernel)
    set_recorder(filtered=LinePlot(filter_size=64))

    # maximum history length
    set_recorder(detail=LinePlot(max_length=50))

    # downsampled values (record mean of every filter_size values)
    set_recorder(downsampled=DownsampledLinePlot(filter_size=5))

    # show heatmap for recording 1d-array values
    set_recorder(array=Heatmap())

    # axis labels
    set_recorder(labeled=LinePlot(xlabel="Episode", ylabel="Score"))

    # minimum update period (limit update rate for better performance)
    set_update_period(0.5)  # [seconds]

    # set number of columns
    set_num_columns(2)

    # generate example values
    for episode in range(50):
        for step in range(20):
            i = episode * 20 + step
            loss = example_loss(i)
            record(filtered=loss, downsampled=loss, detail=loss)
            record(array=example_values(i))
            time.sleep(0.01)

        record(labeled=example_score(episode))


def example_loss(i):
    return 10 / (pow(i / 10, 0.5) + 1) * (1 + 0.3 * np.random.standard_normal())


def example_score(i):
    return i * (1 + 0.1 * np.random.standard_normal())


def example_values(i):
    return np.array([1, 0.3, 0.2, 0.1, 0.3]) * i * 0.001 * (1 + 0.1 * np.random.standard_normal(5))


if __name__ == "__main__":
    np.random.seed(0)
    run_example()
    input("Press Enter to exit...")
