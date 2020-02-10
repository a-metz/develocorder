import time

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
    set_recorder(labeled=LinePlot(xlabel="Episode", ylabel="Score"))

    # additional filtered values (window filter)
    set_recorder(filtered=FilteredLinePlot(filter_size=50, xlabel="Filtered"))

    # maximum history length
    set_recorder(detail=LinePlot(max_length=50, xlabel="Detail"))

    # downsampled values (record mean of every filter_size values)
    set_recorder(downsampled=DownsampledLinePlot(filter_size=5, xlabel="Downsampled"))

    # multiple curves for recording 1d-array values
    set_recorder(multiple=FilteredLinePlot(filter_size=50, xlabel="Multiple"))

    # heatmap for recording 1d-array values
    set_recorder(heatmap=Heatmap(xlabel="Heatmap"))

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
            values = example_values(i)
            record(multiple=values[:3], heatmap=values)
            time.sleep(0.01)

        record(labeled=example_score(episode))


def example_loss(i):
    return 10 / (pow(i / 10, 0.5) + 1) * (1 + 0.3 * np.random.standard_normal())


def example_score(i):
    return i * (1 + 0.1 * np.random.standard_normal())


def example_values(i):
    return np.array([1, 0.5, 0.2, 0.1, 0.3]) * i * 0.001 * (1 + 0.1 * np.random.standard_normal(5))


if __name__ == "__main__":
    np.random.seed(0)
    run_example()
    input("Press Enter to exit...")
