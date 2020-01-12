__global_instance = None


def set_recorder(recorder=None):
    global __global_instance
    __global_instance = recorder


def record(**kwargs):
    if __global_instance is not None:
        __global_instance(**kwargs)


class Recorder:
    def __init__(self):
        self.records = {}

    def add(self, record, name):
        self.records[name] = record

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.records.keys():
                self.records[key](value)
