"""Globally register callables and call via matching keywords.

Example:

>>> # register print function for keyword my_value
>>> set_recorder(my_value=print)
>>> record(my_value="Hello World.")
Hello World.
"""

__recorders = {}


def set_recorder(**kwargs):
    """Globally register a callable to which record calls are delegated.

    :param [keyword] callable: Callable to be registered with its keyword as identifier.
    """

    global __recorders
    for name, recorder in kwargs.items():
        __recorders[name] = recorder


def record(**kwargs):
    """Pass value to previously registered callable.

    :param [keyword] value: This value is passed as the argument to the callable registered
                            with keyword as identifier.
    """

    global __recorders
    for key, value in kwargs.items():
        if key in __recorders.keys():
            __recorders[key](value)
