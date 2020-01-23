import numpy as np

from .graph import GraphBase


class Heatmap(GraphBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.colorbar = None

    def draw_values(self, axes, indices, values):
        pixel_width = 0.5

        left = indices[0] - pixel_width
        right = indices[-1] - pixel_width
        if right == left:
            right = left + 1

        top = pixel_width
        bottom = len(values[0]) + pixel_width

        mappable = axes.imshow(
            np.stack(values).T, interpolation="nearest", aspect="auto", extent=[left, right, top, bottom],
        )

        if self.colorbar is not None:
            self.colorbar.remove()
        self.colorbar = self.container.figure.colorbar(mappable, ax=self.axes)
