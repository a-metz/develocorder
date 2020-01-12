__global_instance = None


def set_plotter(plotter):
    global __global_instance
    __global_instance = plotter


def plot(*args, **kwargs):
    if __global_instance is not None:
        __global_instance(*args, **kwargs)
