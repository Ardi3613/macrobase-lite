"""Pipelines bind ingest, transform, classify, explain and present together."""
from mb_lite.ingest import ingest
from mb_lite.transform import transform
from mb_lite.classification import batch_classify
from mb_lite.explanation import explain
from mb_lite.present import present


def batch_pipeline(data_path):
    df = ingest(data_path)
    df = transform(df)
    df = batch_classify(df)
    explanation = explain(df)
    outliers = df[df["outlier"] == "outlier"]
    outliers = outliers.drop("outlier", 1)
    return present(outliers, explanation)


def streaming_pipeline():
    pass
