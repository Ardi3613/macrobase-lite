import pandas as pd


def ingest(path: str):
    return pd.read_csv(path)
