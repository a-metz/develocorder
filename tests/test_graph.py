from unittest.mock import patch, MagicMock

import develocorder.graph
from develocorder.graph import *


# @patch("develocorder.graph._global_container_instance")
# def test_graph_base(container):
#     graph = GraphBase(xlabel="X", ylabel="Y", max_length=3)
#     graph.draw_values = MagicMock()

#     container.register_graph.assert_called()

#     for i in range(10):
#         graph(i)

#     axes.clear.assert_called()
#     axes.set_xlabel.assert_called_with("X")
#     axes.set_ylabel.assert_called_with("Y")
#     self.figure.canvas.draw
#     container.refresh.assert_called()

#     # less calls due to update rate of 2
#     assert graph.draw_values.call_count == 5

#     # less values due to max size of 3
#     assert len(graph.values) == 3


# patch magicmock into matplotlib backend
@patch("develocorder.graph.matplotlib.pyplot")
@patch("develocorder.graph._global_container_instance", None)
def test_pyplot_calls_on_container_creation(pyplot):
    container = global_container_instance()

    pyplot.figure.assert_called()
    figure = pyplot.figure.return_value
    figure.show.assert_called()


# patch magicmock into matplotlib backend
@patch("develocorder.graph.matplotlib.pyplot")
@patch("develocorder.graph._global_container_instance", None)
def test_pyplot_calls_on_graph_creation(pyplot):
    container = global_container_instance()
    figure = container.figure

    graph = GraphBase()

    figure.add_subplot.assert_called_with(1, 1, 1)
    axes = figure.add_subplot.return_value

    graph = GraphBase()

    figure.add_subplot.assert_called_with(2, 1, 2)
    # check that gemetry of first axis gets changed
    axes.change_geometry.assert_called_with(2, 1, 1)


# patch magicmock into matplotlib backend
@patch("develocorder.graph.matplotlib.pyplot")
@patch("develocorder.graph._global_container_instance", None)
def test_pyplot_calls_on_graph_call(pyplot):
    container = global_container_instance()
    figure = container.figure
    graph = GraphBase(xlabel="X", ylabel="Y")
    axes = figure.add_subplot.return_value

    graph(42)

    axes.clear.assert_called()
    axes.set_xlabel.assert_called_with("X")
    axes.set_ylabel.assert_called_with("Y")
    figure.canvas.draw.assert_called()
