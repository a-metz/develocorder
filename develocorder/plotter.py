import matplotlib.pyplot as plt

from .filter import filter_values


class GraphBase:
    def __init__(self, xlabel, ylabel, update_rate=1, window=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.update_rate = update_rate

        if window is None:
            window = Window.global_instance()
        self.axes = window.add_axes()

        self.values = []

    def __call__(self, value):
        self.values.append(value)

        if len(self.values) % self.update_rate == 0:
            self.axes.clear()
            self.axes.set_xlabel(self.xlabel)
            self.axes.set_ylabel(self.ylabel)
            self.draw()
            Window.refresh()

    def draw(self):
        """ to be implemented by specialisations """
        pass


class Plotter(GraphBase):
    def __init__(self, *args, filter_size=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_size = filter_size

    def draw(self):
        self.axes.plot(self.values)

        if self.filter_size is not None:
            self.axes.plot(filter_values(self.values, self.filter_size))


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

    @classmethod
    def refresh(cls):
        plt.pause(0.0001)

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
