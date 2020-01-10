import numpy as np
import matplotlib.pyplot as plt


class ValueLogger(object):
    def __init__(self, show_plot=True):
        self.plotter = {}
        if show_plot:
            ValuePlotter.show_plot()

    def add_plot(self, name, xlabel, filter_size=None):
        self.plotter[name] = ValuePlotter(xlabel=xlabel, ylabel=name, filter_size=filter_size)

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.plotter.keys():
                self.plotter[key].add(value)
                self.plotter[key].plot()


class ValuePlotter(object):
    plots_count = 0

    def __init__(self, xlabel, ylabel, filter_size=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.filter_size = filter_size
        ValuePlotter.plots_count += 1
        self.index = self.plots_count
        self.values = []

    @classmethod
    def show_plot(cls):
        plt.ion()
        plt.show()

    def add(self, value):
        self.values.append(value)

    def plot(self):
        plt.subplot(self.plots_count, 1, self.index)
        plt.cla()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.values)
        if self.filter_size is not None:
            plt.plot(self._filter_values(self.values))
        plt.pause(0.001)

    def _filter_values(self, values):
        padded_values = np.concatenate(
            [
                np.full(self.filter_size // 2, values[0]),
                np.array(values),
                np.full(self.filter_size // 2 - 1, values[-1]),
            ]
        )
        filter_kernel = np.ones((self.filter_size,)) / self.filter_size
        return np.convolve(padded_values, filter_kernel, mode="valid")
