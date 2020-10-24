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


happy_data = """99.8,B
1.0,A
1.1,A
1.2,A
1.11,A
1.12,A
1.22,A
1.3,A
109,B
"""

happy_data_expected = """"""


@patch("mb_lite.ingest.read_csv", new_callable=mock_open, read_data=happy_data)
def test_batch_pipeline(_):
    output_str = batch_pipeline("path")
    assert output_str == happy_data_expected
