__recorders = {}


def set_recorder(**kwargs):
    global __recorders
    for name, recorder in kwargs.items():
        __recorders[name] = recorder


def record(**kwargs):
    global __recorders
    for key, value in kwargs.items():
        if key in __recorders.keys():
            __recorders[key](value)
