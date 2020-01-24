import numpy as np

from .graph import GraphBase


class LinePlot(GraphBase):
    """
    Lineplot for recording scalar values with optional filtering.
    """

    def __init__(self, *args, filter_size=None, **kwargs):
        """
        :param filter_size int: size of filter kernel (window)
        """

        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw_values(self, axes, indices, values):
        axes.plot(indices, values)

        if self.filter_size is not None:
            axes.plot(indices, filter_values(values, self.filter_size))

        # additionally plot point when there is only one value, as the line is not visible then
        if len(values) == 1:
            axes.scatter(indices, values)


def filter_values(values, filter_size):
    padded_values = np.concatenate(
        [np.full(filter_size // 2, values[0]), np.array(values), np.full(filter_size // 2 - 1, values[-1]),]
    )
    filter_kernel = np.ones((filter_size,)) / filter_size
    return np.convolve(padded_values, filter_kernel, mode="valid")
