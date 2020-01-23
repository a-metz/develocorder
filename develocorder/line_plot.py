from .filter import filter_values
from .graph import GraphBase


class LinePlot(GraphBase):
    def __init__(self, *args, filter_size=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw_values(self, axes, indices, values):
        axes.plot(indices, values)

        if self.filter_size is not None:
            axes.plot(indices, filter_values(values, self.filter_size))
