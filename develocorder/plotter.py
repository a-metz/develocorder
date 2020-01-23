from collections import deque

import matplotlib.pyplot as plt

from .filter import filter_values


class GraphBase:
    def __init__(self, xlabel, ylabel, update_rate=1, max_size=None, window=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.update_rate = update_rate
        self.window = window

        if self.window is None:
            self.window = Window.global_instance()
        self.axes = self.window.add_axes()

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
            self.window.refresh()

    def draw_decorations(self):
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)

    def draw_values(self):
        """ to be implemented by concrete type """
        pass


class Plotter(GraphBase):
    def __init__(self, *args, filter_size=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw_values(self):
        self.axes.plot(self.indices, self.values)

        if self.filter_size is not None:
            self.axes.plot(self.indices, filter_values(self.values, self.filter_size))


class Window:
    _global_instance = None

    def __init__(self):
        self.figure = plt.figure(constrained_layout=True)
        self.figure.show()

        self.num_rows = 0
        self.num_columns = 1
        self.num_axes = 0

    @classmethod
    def global_instance(cls):
        if cls._global_instance is None:
            cls._global_instance = cls()

        return cls._global_instance

    def refresh(self):
        self.figure.canvas.draw()

    def add_axes(self):
        self.increment_counts()
        axes = self.figure.add_subplot(self.num_rows, self.num_columns, self.num_axes)
        self.update_layout()
        return axes

    def increment_counts(self):
        self.num_axes += 1
        self.num_rows = self.num_axes // self.num_columns

    def update_layout(self):
        for i, axes in enumerate(self.figure.axes):
            axes.change_geometry(self.num_rows, self.num_columns, i + 1)
