import numpy as np

from develocorder import LinePlot, Heatmap, set_recorder, record


def run_example():
    set_recorder(loss=LinePlot(xlabel="Step", ylabel="Loss", filter_size=64, update_rate=10))
    set_recorder(loss_detail=LinePlot(xlabel="Step", ylabel="Loss Detail", update_rate=10, max_length=50))
    set_recorder(action_values=Heatmap(xlabel="Step", ylabel="Action Values", update_rate=10, max_length=1000))
    set_recorder(score=LinePlot(xlabel="Episode", ylabel="Score"))

    for episode in range(50):
        for step in range(20):
            i = episode * 20 + step
            loss = example_loss(i)
            record(loss=loss)
            record(loss_detail=loss)
            record(action_values=example_action_values(i))

        record(score=example_score(episode))


def example_loss(i):
    return 10 / (pow(i / 10, 0.5) + 1) * (1 + 0.3 * np.random.standard_normal())


def example_score(i):
    return i * (1 + 0.1 * np.random.standard_normal())


def example_action_values(i):
    return np.array([1, 0.3, 0.2, 0.1, 0.3]) * i * 0.001 * (1 + 0.1 * np.random.standard_normal(5))


if __name__ == "__main__":
    run_example()
    input("Press Enter to exit...")
