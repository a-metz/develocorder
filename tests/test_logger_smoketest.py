from unittest.mock import patch

import pytest
import matplotlib

from develocorder import Logger, WindowFilterLogger, set_recorder, record


@patch("develocorder.interface._recorders", {})
def test_logger_smoketest():
    set_recorder(value1=Logger(name="Value 1"))
    set_recorder(value2=Logger(name="Value 2"))

    record(value1=1)
    record(value1=6)
    record(value1=-1)
    record(value2=0)


@patch("develocorder.interface._recorders", {})
def test_window_filter_logger_smoketest():
    set_recorder(value1=WindowFilterLogger(name="Value 1", filter_size=3))

    record(value1=1)
    record(value1=6)
    record(value1=-4)
    record(value1=5)
