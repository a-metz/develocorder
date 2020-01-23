import numpy as np

from .graph import GraphBase


class LinePlot(GraphBase):
    def __init__(self, *args, filter_size=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw_values(self, axes, indices, values):
        axes.plot(indices, values)

        if self.filter_size is not None:
            axes.plot(indices, filter_values(values, self.filter_size))


def filter_values(values, filter_size):
    padded_values = np.concatenate(
        [np.full(filter_size // 2, values[0]), np.array(values), np.full(filter_size // 2 - 1, values[-1]),]
    )
    filter_kernel = np.ones((filter_size,)) / filter_size
    return np.convolve(padded_values, filter_kernel, mode="valid")
