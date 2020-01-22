from collections import deque

import numpy as np


class Logger:
    def __init__(self, name):
        self.name = name

    def __call__(self, value):
        print("{}: {}".format(self.name, value))


class WindowFilterLogger:
    def __init__(self, name, filter_size):
        self.name = name
        self.values = deque(maxlen=filter_size)

    def __call__(self, value):
        self.values.append(value)

        if len(self.values) == self.values.maxlen:
            print("{}: {}".format(self.name, np.mean(self.values)))
