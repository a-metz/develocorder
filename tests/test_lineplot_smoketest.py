import pytest
import matplotlib

from develocorder import LinePlot, set_recorder, record


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
def test_lineplot_smoketest():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    # all arguments
    set_recorder(value1=LinePlot(xlabel="Sample", ylabel="Value 1", filter_size=2, update_rate=2, max_length=3))

    # no arguments
    set_recorder(value2=LinePlot())

    record(value1=1)
    record(value2=42)
    record(value1=3)
    record(value2=43)
    record(value1=6)
    record(value1=9)
    record(value1=-1)
    record(value3=0)
