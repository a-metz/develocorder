from unittest.mock import patch

import pytest
import matplotlib

from develocorder import Heatmap, set_recorder, record


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
@patch("develocorder.graph._global_container_instance", None)
@patch("develocorder.interface._recorders", {})
def test_heatmap_smoketest():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    # all arguments
    set_recorder(value1=Heatmap(xlabel="Sample", ylabel="Values 1", max_length=3))

    # no arguments
    set_recorder(value2=Heatmap())

    record(value1=[1, 9])
    record(value2=[42, 43, 44])
    record(value1=[3, 6])
    record(value2=[43, 44, 45])
    record(value1=[6, 3])
    record(value1=[9, 1])
    record(value1=[-1, 0])
