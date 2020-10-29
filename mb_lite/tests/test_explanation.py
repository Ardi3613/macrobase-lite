from mb_lite.explanation import filter_non_cat, explain, filter_on_attrs, risk_ratio
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


def test_filter_attrs():
    df = pd.DataFrame(
        {"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3], "D": [1, 2, 3], "X": [7, 7, 7]}
    )
    filt = {"A": 2, "B": 2, "X": 7}
    res = filter_on_attrs(df, filt)
    exp = pd.DataFrame({"A": [2], "B": [2], "C": [2], "D": [2], "X": [7]})
    assert all(exp.values[0] == res.values[0])


def test_risk_ratio():
    df = pd.DataFrame(
        {
            "A": [0, 1, 2, 3, 4],
            "B": [0, 1, 2, 3, 4],
            "C": [0, 1, 2, 3, 4],
            "D": [0, 1, 2, 3, 4],
            "X": [7, 7, 7, 8, 9],
            "outlier": ["inlier", "inlier", "inlier", "outlier", "outlier"],
        }
    )
    attrs = {"X": 8}
    assert risk_ratio(attrs, df) == pytest.approx(4.0)
