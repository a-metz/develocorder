import pytest

from develocorder import Recorder, set_recorder, record


def test_without_initialized_recorder():
    # expect no error
    record(my_value=42)


class RecordStub:
    def __init__(self):
        self.value = None

    def __call__(self, value):
        self.value = value


@pytest.fixture
def recorder():
    rec = Recorder()
    set_recorder(rec)
    return rec


def test_delegation_to_correct_record(recorder):
    my_record = RecordStub()
    recorder.add(my_record, name="my_value")
    other_record = RecordStub()
    recorder.add(other_record, name="other_value")

    record(my_value=42)

    assert my_record.value == 42
    assert other_record.value == None


def test_nonexisting_record(recorder):
    record_stub = RecordStub()
    recorder.add(record_stub, name="my_value")

    record(other_value=42)

    assert record_stub.value == None
