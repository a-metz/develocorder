from unittest.mock import patch

import pytest

from develocorder import set_recorder, record


@patch("develocorder.interface._recorders", {})
def test_without_initialized_recorder():
    # expect no error
    record(my_value=42)


class RecorderStub:
    def __init__(self):
        self.value = None

    def __call__(self, value):
        self.value = value


@patch("develocorder.interface._recorders", {})
def test_delegation_to_correct_record():
    my_recorder = RecorderStub()
    set_recorder(my_value=my_recorder)
    other_recorder = RecorderStub()
    set_recorder(other_value=other_recorder)

    record(my_value=42)

    assert my_recorder.value == 42
    assert other_recorder.value == None


@patch("develocorder.interface._recorders", {})
def test_nonexisting_record():
    recorder_stub = RecorderStub()
    set_recorder(my_value=recorder_stub)

    record(other_value=42)

    assert recorder_stub.value == None
