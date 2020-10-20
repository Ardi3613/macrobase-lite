from mb_lite.explanation import filter_non_cat
import pytest
import pandas as pd


@pytest.mark.parametrize(
    ("data", "ex_data"), [([["abc", 123], ["cab", 63]], {1: [123, 63]})]
)
def test_filter_basic(data, ex_data):
    """Basic categorical col filtering."""
    df = pd.DataFrame(data)
    ex_df = pd.DataFrame(ex_data)
    cat_df = filter_non_cat(df)
    assert cat_df.to_dict() == ex_df.to_dict()
