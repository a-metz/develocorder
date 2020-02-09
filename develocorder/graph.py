import time
from collections import deque
import math

import matplotlib.pyplot


class GraphBase:
    """
    Base class for a graph in a container. Needs to be subclassed to implement actual drawing.
    """

    def __init__(self, xlabel=None, ylabel=None, max_length=None, container=None):
        """Init to be called via subclass.

        :param xlabel str: label for x axis
        :param ylabel str: label for y axis
        :param update_rate int: The divisor for updating the plot window.
                                Only update every update_rate calls to graph(value).
        :param max_length int: Maximum length of buffer for values. Older values are discarded.
        :param container GraphContainer or None: Instance of container.
                                                 If None then the global instance will be used.
        """

        self.xlabel = xlabel
        self.ylabel = ylabel
        if container is None:
            container = global_container_instance()
        self.container = container

        self.container.register_graph(callback=self.update)

        self.count = 0
        self.last_update = 0
        self.values = deque(maxlen=max_length)
        self.indices = range(0)

    def __call__(self, value):
        self.count += 1
        self.values.append(value)
        self.indices = range(self.count - len(self.values), self.count)
        self.container.update()

    def update(self, axes):
        if self.last_update >= self.count:
            updated = False
            return updated

        axes.clear()
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        self.draw_values(axes, self.indices, self.values)

        self.last_update = self.count
        updated = True
        return updated

    def draw_values(self, axes, indices, values):
        """Actual drawing on axes. To be implemented by concrete type.

        :param axes Matplotlib.axes.Axes: Axes object to draw on
        :param indices py:range: range of indices (one per value)
        :param values deque[any]: recorded values
        """

        pass


class GraphContainer:
    """Container for GraphBase which is shown as Matplotlib figure."""

    def __init__(self, title="Develocorder"):
        self.figure = matplotlib.pyplot.figure(title)
        self.figure.show()

        self.num_rows = 0
        self.num_columns = 1
        self.num_axes = 0

        self.graphs = []
        self.update_period = 0.0
        self.last_update = 0.0

    def update(self):
        # skip updating if not enough time has passed
        if time.time() < self.last_update + self.update_period:
            return

        updated = [callback(axes) for axes, callback in self.graphs]
        if any(updated):
            self.figure.canvas.draw()
            # a bit of a hack to give the gui thread time to update, the value can be arbitrarily small
            matplotlib.pyplot.pause(1e-9)

        self.last_update = time.time()

    def register_graph(self, callback):
        # update layout of previously added graphs
        self.num_axes += 1
        self._update_layout()

        axes = self.figure.add_subplot(self.num_rows, self.num_columns, self.num_axes)
        self.graphs.append((axes, callback))

    def _update_layout(self):
        self.num_rows = int(math.ceil(self.num_axes / self.num_columns))

        for i, (axes, _) in enumerate(self.graphs):
            axes.change_geometry(self.num_rows, self.num_columns, i + 1)

        # make some space for labels
        self.figure.tight_layout(h_pad=1.5, w_pad=1.5)

    def set_update_period(self, update_period):
        self.update_period = update_period

    def set_num_columns(self, num_columns):
        self.num_columns = num_columns
        self._update_layout()


_global_container_instance = None


def global_container_instance():
    global _global_container_instance

    if _global_container_instance is None:
        _global_container_instance = GraphContainer()

    return _global_container_instance


def set_update_period(update_period):
    """ Set global update period in seconds.

    Graphs will only be redrawn after specified time has passed.
    """

    global_container_instance().set_update_period(update_period)


def set_num_columns(num_columns):
    """ Set number of columns in graph container."""

    global_container_instance().set_num_columns(num_columns)
