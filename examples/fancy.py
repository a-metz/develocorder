import time

import numpy as np

from develocorder import LinePlot, Heatmap, set_recorder, record, set_update_period, set_num_columns


def run_example():
    # axis labels
    set_recorder(score=LinePlot(xlabel="Episode", ylabel="Score"))

    # filter values (window filter kernel)
    set_recorder(loss=LinePlot(filter_size=64))

    # maximum history length
    set_recorder(loss_detail=LinePlot(max_length=50))

    # show heatmap for recording 1d-array values
    set_recorder(array_values=Heatmap(max_length=1000))

    # minimum update period (limit update rate for better performance)
    set_update_period(0.5)

    # set number of columns
    set_num_columns(2)

    # generate example values
    for episode in range(50):
        for step in range(20):
            i = episode * 20 + step
            loss = example_loss(i)
            record(loss=loss)
            record(loss_detail=loss)
            action_values = example_values(i)
            record(action_values=action_values)
            record(action_values_detail=action_values)
            record(state_values=example_values(i))
            time.sleep(0.01)

        record(score=example_score(episode))


def example_loss(i):
    return 10 / (pow(i / 10, 0.5) + 1) * (1 + 0.3 * np.random.standard_normal())


def example_score(i):
    return i * (1 + 0.1 * np.random.standard_normal())


def example_values(i):
    return np.array([1, 0.3, 0.2, 0.1, 0.3]) * i * 0.001 * (1 + 0.1 * np.random.standard_normal(5))


if __name__ == "__main__":
    run_example()
    input("Press Enter to exit...")
