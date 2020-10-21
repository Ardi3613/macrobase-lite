"""Complete e2e happy flow."""
from mb_lite.classification import batch_classify
from mb_lite.pipeline import batch_pipeline
import pandas as pd
from unittest.mock import mock_open, patch


def test_univariate():
    input_df = {0: [1.0, 1.1, 0.9, 99.8], 1: ["A", "A", "A", "B"]}
    expected_output = {
        0: [1.0, 1.1, 0.9, 99.8],
        1: ["A", "A", "A", "B"],
        "outlier": ["inlier", "inlier", "inlier", "outlier"],
    }
    ex_df = pd.DataFrame(expected_output)
    in_df = pd.DataFrame(input_df)
    res_df = batch_classify(in_df)
    assert res_df.to_dict() == ex_df.to_dict()


happy_data = """1.0,1.1,0.9,99.8
A,A,A,B
"""

happy_data_expected = """Outliers
4\t99.9,B
Rules
B causes outlier
"""


@patch("builtins.open", new_callable=mock_open, read_data=happy_data)
def test_batch_pipeline(_):
    output_str = batch_pipeline("path")
    assert output_str == happy_data_expected
