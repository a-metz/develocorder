import pytest

import matplotlib
from develocorder import ValueLogger, set_logger, log


class DummyLogger:
    def __call__(self, value):
        self.value = value


def test_set_logger_and_log():
    dummy_logger = DummyLogger()
    set_logger(dummy_logger)
    log(42)

    assert dummy_logger.value == 42


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
def test_smoketest_value_plotter():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    # hide view for non blocking on CI
    value_logger = ValueLogger(show_plot=False)

    value_logger.add_plot(name="value1", xlabel="t", filter_size=32)
    value_logger.add_plot(name="value2", xlabel="t", filter_size=64)
    set_logger(value_logger)

    log(value1=1)
    log(value2=42)
    log(value1=3)
    log(value2=43)
    log(value1=6)
    log(value1=9)
    log(value1=-1)
    log(value3=0)
