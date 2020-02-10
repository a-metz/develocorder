import random
from unittest.mock import patch

import pytest
import matplotlib

from develocorder import LinePlot, FilteredLinePlot, DownsampledLinePlot, set_recorder, record


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
@patch("develocorder.graph._global_container_instance", None)
@patch("develocorder.interface._recorders", {})
def test_lineplot_smoketest():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    # all arguments
    set_recorder(value1=LinePlot(max_length=3, xlabel="Sample", ylabel="LinePlot"))

    # no arguments
    set_recorder(value2=LinePlot())

    set_recorder(
        value3=FilteredLinePlot(
            filter_size=3, max_length=7, xlabel="Sample", ylabel="FilteredLinePlot"
        )
    )

    set_recorder(
        value3=DownsampledLinePlot(
            filter_size=3, max_length=7, xlabel="Sample", ylabel="DownsampledLinePlot"
        )
    )

    random.seed(0)

    for _ in range(10):
        record(value1=random.random())
        record(value2=[random.random(), random.random()])
        record(value3=random.random())
        record(value4=random.random())
