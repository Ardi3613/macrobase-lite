from efficient_apriori import apriori
from mb_lite.present import present
from pandas import DataFrame


def test_present():
    _, rules = apriori([["a", "outlier"], ["c", "outlier"]])
    df_outliers = {0: [1.2, 1.4], 1: ["a", "b"]}
    df_outliers = DataFrame(df_outliers)
    human_str = present(df_outliers, rules)
    expected_str = """Outliers
     0  1
0  1.2  a
1  1.4  b
Causes
{a} -> {outlier} (conf: 1.000, supp: 0.500, lift: 1.000, conv: 0.000)
{c} -> {outlier} (conf: 1.000, supp: 0.500, lift: 1.000, conv: 0.000)"""
    assert human_str == expected_str
