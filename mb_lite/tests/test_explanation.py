from mb_lite.explanation import filter_non_cat, explain
import pytest
import pandas as pd


@pytest.mark.parametrize(
    ("data", "ex_data"),
    [
        ([["abc", 123], ["cab", 63]], {0: ["abc", "cab"]}),
        ([["abc", "z"], ["cab", "a"]], {1: ["z", "a"], 0: ["abc", "cab"]}),
    ],
)
def test_filter_basic(data, ex_data):
    """Basic categorical col filtering."""
    df = pd.DataFrame(data)
    ex_df = pd.DataFrame(ex_data)
    cat_df = filter_non_cat(df)
    assert cat_df.to_dict() == ex_df.to_dict()


def test_explain():
    """Basic smoke test for explain."""
    transactions = [
        ("eggs", "bacon", "soup"),
        ("eggs", "bacon", "apple"),
        ("soup", "bacon", "banana"),
    ]
    df = pd.DataFrame(transactions)
    explanation = explain(df)
    assert explanation[0].lhs == ("eggs",)
    assert explanation[0].rhs == ("bacon",)
    assert explanation[1].lhs == ("bacon",)
    assert explanation[1].rhs == ("eggs",)
    assert explanation[2].lhs == ("soup",)
    assert explanation[2].rhs == ("bacon",)
    assert explanation[3].lhs == ("bacon",)
    assert explanation[3].rhs == ("soup",)
