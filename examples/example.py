import numpy as np

from develocorder import Plotter, set_recorder, record


def setup():
    set_recorder(loss=Plotter(xlabel="Step", ylabel="Loss", filter_size=32, update_rate=10))
    set_recorder(score=Plotter(xlabel="Episode", ylabel="Score"))


def run():
    for episode in range(10):
        for step in range(100):
            record(loss=example_loss(episode, step))

        record(score=example_score(episode))


def example_loss(episode, step):
    i = episode * 100 + step + 1
    return 10 / pow(i, 0.2) * (1 + 0.3 * np.random.standard_normal())


def example_score(episode):
    return episode * (1 + 0.3 * np.random.standard_normal())


if __name__ == "__main__":
    setup()
    run()
    input("Press Enter to exit...")
