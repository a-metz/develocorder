from unittest.mock import patch, MagicMock

import develocorder.graph
from develocorder.graph import *


@patch("develocorder.graph._global_container_instance")
def test_graph_base(container):
    graph = GraphBase(xlabel="X", ylabel="Y", update_rate=2, max_length=3)
    graph.draw_values = MagicMock()

    container.add_axes.assert_called()
    axes = container.add_axes.return_value

    for i in range(10):
        graph(i)

    axes.clear.assert_called()
    axes.set_xlabel.assert_called_with("X")
    axes.set_ylabel.assert_called_with("Y")
    container.refresh.assert_called()

    # less calls due to update rate of 2
    assert graph.draw_values.call_count == 5

    # less values due to max size of 3
    assert len(graph.values) == 3


# patch magicmock into matplotlib backend
@patch("develocorder.graph.matplotlib.pyplot")
def test_graph_container_pyplot_calls(pyplot):
    # test init
    container = GraphContainer()

    pyplot.figure.assert_called()
    figure = pyplot.figure.return_value
    figure.show.assert_called()

    # test adding axes
    axes = MagicMock()
    figure.add_subplot.return_value = axes
    figure.axes = [axes]

    container.add_axes()

    figure.add_subplot.assert_called_with(1, 1, 1)
    axes = figure.add_subplot.return_value

    container.add_axes()

    figure.add_subplot.assert_called_with(2, 1, 2)
    axes.change_geometry.assert_called_with(2, 1, 1)

    # test refresh
    container.refresh()

    figure.canvas.draw.assert_called()
