from random import random

from develocorder import LinePlot, set_recorder, record


def run_example():
    set_recorder(my_value=LinePlot())

    for _ in range(10):
        record(my_value=random())


if __name__ == "__main__":
    random.seed(0)
    run_example()
    input("Press Enter to exit...")
