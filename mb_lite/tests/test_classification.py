from mb_lite.classification import AdrMAD
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
    adr = AdrMAD(arr)
    assert adr.is_outlier(point, cut_off=2.0) == outlier


def test_basic_adr():
    adr = AdrMAD(k=2)
    adr.adr_update(1)
    assert adr.reservoir == [1]
    adr.adr_update(2)
    assert adr.reservoir == [1, 2]
