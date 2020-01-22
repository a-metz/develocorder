import numpy as np


def filter_values(values, filter_size):
    padded_values = np.concatenate(
        [np.full(filter_size // 2, values[0]), np.array(values), np.full(filter_size // 2 - 1, values[-1]),]
    )
    filter_kernel = np.ones((filter_size,)) / filter_size
    return np.convolve(padded_values, filter_kernel, mode="valid")
