from collections import deque

import numpy as np


class Logger:
    """Print recorded values."""

    def __init__(self, name):
        """
        :param name str: identifier for printed value
        """

        self.name = name

    def __call__(self, value):
        print("{}: {}".format(self.name, value))


class WindowFilterLogger:
    """Filter and print recorded values."""

    def __init__(self, name, filter_size):
        """
        :param name str: identifier for printed value
        :param filter_size: number of historic samples which are averaged.
                            No output until filter_size number of values have been recorded.
        """
        self.name = name
        self.values = deque(maxlen=filter_size)

    def __call__(self, value):
        self.values.append(value)

        if len(self.values) == self.values.maxlen:
            print("{}: {}".format(self.name, np.mean(self.values)))
