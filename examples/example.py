import numpy as np

from develocorder import LinePlot, Heatmap, set_recorder, record


def setup():
    set_recorder(loss=LinePlot(xlabel="Step", ylabel="Loss", filter_size=32, update_rate=10, max_size=500))
    set_recorder(score=LinePlot(xlabel="Episode", ylabel="Score"))
    set_recorder(action_values=Heatmap(xlabel="Step", ylabel="Action Values", update_rate=10, max_size=200))


def run():
    for episode in range(10):
        for step in range(100):
            record(loss=example_loss(episode, step))
            record(action_values=example_action_values(episode, step))

        record(score=example_score(episode))


def example_loss(episode, step):
    i = episode * 100 + step + 1
    return 10 / pow(i, 0.2) * (1 + 0.3 * np.random.standard_normal())


def example_score(episode):
    return episode * (1 + 0.3 * np.random.standard_normal())


def example_action_values(episode, step):
    i = episode * 100 + step + 1
    return (0.01 * i) + pow(i, 0.2) * (1 + np.array([1, 0.3, 0, 0.1, 0.3]) * np.random.standard_normal(5))


if __name__ == "__main__":
    setup()
    run()
    input("Press Enter to exit...")
