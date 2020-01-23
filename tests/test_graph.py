from unittest.mock import patch, MagicMock

import develocorder.graph
from develocorder.graph import *

# patch magicmock into matplotlib backend
@patch("develocorder.graph.matplotlib.pyplot")
def test_graph_container(pyplot):
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
    axes.change_geometry.assert_called_with(1, 1, 1)

    container.add_axes()

    figure.add_subplot.assert_called_with(2, 1, 2)
    axes.change_geometry.assert_called_with(2, 1, 1)

    # test refresh
    container.refresh()

    figure.canvas.draw.assert_called()
