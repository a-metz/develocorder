from collections import deque

import numpy as np

from .graph import GraphBase


class LinePlot(GraphBase):
    """
    Lineplot for recording scalar values.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_values(self, axes, indices, values):
        axes.plot(indices, values)

        # additionally plot point when there is only one value, as the line is not visible then
        if len(values) == 1:
            value = values[0]
            index = indices[0]

            # in case of multidimensional value
            if hasattr(value, "__len__"):
                for scalar in value:
                    axes.scatter(index, scalar)
            else:
                axes.scatter(index, value)


class FilteredLinePlot(LinePlot):
    """
    Lineplot for recording scalar values with additional window filtered plot.
    """

    def __init__(self, filter_size, *args, **kwargs):
        """
        :param filter_size int: size of filter kernel (window)
        """

        super().__init__(*args, **kwargs)
        self.filter_buffer = deque(maxlen=filter_size)

    def __call__(self, value):
        self.filter_buffer.append(value)
        filtered = np.mean(self.filter_buffer, axis=0)
        # flatten in case of multidimensional value
        value_with_filtered = np.dstack([value, filtered]).flatten()

        super().__call__(value_with_filtered)


class DownsampledLinePlot(LinePlot):
    """
    Lineplot for recording scalar values. Recorded values are the mean of every filter_size
    recorded values.
    """

    def __init__(self, filter_size, *args, **kwargs):
        """
        :param filter_size int: size of filter kernel (window)
        """

        super().__init__(*args, **kwargs)
        self.filter_size = filter_size
        self.filter_buffer = []

    def __call__(self, value):
        self.filter_buffer.append(value)

        if len(self.filter_buffer) == self.filter_size:
            filtered_value = np.mean(self.filter_buffer, axis=0)
            self.filter_buffer.clear()

            super().__call__(filtered_value)

    def draw_values(self, axes, indices, values):
        downsampled_indices = range(
            indices.start * self.filter_size, indices.stop * self.filter_size, self.filter_size
        )
        super().draw_values(axes, downsampled_indices, values)
