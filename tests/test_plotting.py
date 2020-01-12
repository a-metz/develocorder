import pytest
import matplotlib

from develocorder import ValuePlotter, set_plotter, plot


class DummyPlotter:
    def __call__(self, value):
        self.value = value


def test_interface():
    dummy_plotter = DummyPlotter()

    set_plotter(dummy_plotter)
    plot(42)

    assert dummy_plotter.value == 42


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
def test_smoketest_value_plotter():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    value_plotter = ValuePlotter()
    value_plotter.add_plot(name="value1", xlabel="t", filter_size=32)
    value_plotter.add_plot(name="value2", xlabel="t")
    set_plotter(value_plotter)

    plot(value1=1)
    plot(value2=42)
    plot(value1=3)
    plot(value2=43)
    plot(value1=6)
    plot(value1=9)
    plot(value1=-1)
    plot(value3=0)
