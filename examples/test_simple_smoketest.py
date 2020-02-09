from unittest.mock import patch

import pytest
import matplotlib

from simple import run_example


@pytest.mark.filterwarnings(
    "ignore:Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure"
)
@patch("develocorder.graph._global_container_instance", None)
@patch("develocorder.interface._recorders", {})
def test_simple_example_smoketest():
    # use backend which does not require a display for CI
    matplotlib.use("Agg")

    run_example()
