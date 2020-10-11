from mb_lite.classification import is_outlier
import pytest


@pytest.mark.parametrize(
    ("point", "outlier"),
    [
        (1.0, False),
        (1.1, False),
        (1.2, False),
        (1.3, False),
        (1.5, False),
        (1.6, False),
        (99.0, True),
        (-99.0, True),
    ],
)
def test_basic_outlier(point, outlier):
    arr = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 99.0]
    assert is_outlier(arr, point, 2.0) == outlier
