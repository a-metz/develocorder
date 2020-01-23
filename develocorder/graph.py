from collections import deque

import matplotlib.pyplot

from .filter import filter_values


class GraphBase:
    def __init__(self, xlabel, ylabel, update_rate=1, max_size=None, container=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.update_rate = update_rate
        self.container = container

        if self.container is None:
            self.container = global_container_instance()
        self.axes = self.container.add_axes()

        self.count = 0
        self.values = deque(maxlen=max_size)

    def __call__(self, value):
        self.count += 1
        self.values.append(value)
        self.indices = range(self.count - len(self.values), self.count)

        if self.count % self.update_rate == 0:
            self.axes.clear()
            self.draw_decorations()
            self.draw_values()
            self.container.refresh()

    def draw_decorations(self):
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)

    def draw_values(self):
        """ to be implemented by concrete type """
        pass


class LinePlot(GraphBase):
    def __init__(self, *args, filter_size=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw_values(self):
        self.axes.plot(self.indices, self.values)

        if self.filter_size is not None:
            self.axes.plot(self.indices, filter_values(self.values, self.filter_size))


class GraphContainer:
    def __init__(self):
        self.figure = matplotlib.pyplot.figure()
        self.figure.show()

        self.num_rows = 0
        self.num_columns = 1
        self.num_axes = 0

    def refresh(self):
        self.figure.canvas.draw()

    def add_axes(self):
        self._increment_counts()
        axes = self.figure.add_subplot(self.num_rows, self.num_columns, self.num_axes)
        self._update_layout()
        return axes

    def _increment_counts(self):
        self.num_axes += 1
        self.num_rows = self.num_axes // self.num_columns

    def _update_layout(self):
        for i, axes in enumerate(self.figure.axes):
            axes.change_geometry(self.num_rows, self.num_columns, i + 1)


_global_container_instance = None


def global_container_instance():
    global _global_container_instance

    if _global_container_instance is None:
        _global_container_instance = GraphContainer()

    return _global_container_instance
