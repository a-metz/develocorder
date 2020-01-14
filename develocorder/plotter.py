import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    initialized = False
    plots_count = 0

    def __init__(self, xlabel, ylabel, filter_size=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.filter_size = filter_size
        self.values = []

        Plotter.plots_count += 1
        self.index = self.plots_count

        Plotter.initialize_display()

    @classmethod
    def initialize_display(cls):
        if not Plotter.initialized:
            plt.ioff()
            plt.show()
            Plotter.initialized = True

    def __call__(self, value):
        self.values.append(value)

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
