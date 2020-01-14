import pytest
import matplotlib

from develocorder import Logger, set_recorder, record


def test_logger_smoketest():
    set_recorder(value1=Logger(name="Value 1"))
    set_recorder(value2=Logger(name="Value 2", format_string="{name}, {index}, {value}"))

    record(value1=1)
    record(value1=6)
    record(value1=-1)
    record(value2=0)
