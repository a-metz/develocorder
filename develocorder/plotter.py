import matplotlib.pyplot as plt

from .filter import filter_values


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
            plt.plot(filter_values(self.values, self.filter_size))
        plt.pause(0.001)
