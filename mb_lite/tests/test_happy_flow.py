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


happy_data = """{"num_col":{"0":99.8,"1":1.0,"2":1.1,"3":1.2,"4":1.11,"5":1.12,"6":1.22,"7":1.3,"8":109.0},"cat_col":{"0":"B","1":"A","2":"A","3":"A","4":"A","5":"A","6":"A","7":"A","8":"B"}}"""

happy_data_expected = """Outliers
   num_col cat_col
0     99.8       B
8    109.0       B
Causes
{A} -> {inlier} (conf: 1.000, supp: 0.778, lift: 1.286, conv: 222222222.222)"""


@patch("mb_lite.ingest.read_csv")
def test_batch_pipeline(read_csv):
    read_csv.return_value = pd.read_json(happy_data)
    output_str = batch_pipeline("path")
    assert output_str == happy_data_expected
