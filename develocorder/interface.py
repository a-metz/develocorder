_global_logger = None


def set_logger(logger):
    global _global_logger
    _global_logger = logger


def log(*args, **kwargs):
    if _global_logger is not None:
        _global_logger(*args, **kwargs)
