from pandas import read_csv


def ingest(path: str):
    return read_csv(path, delimiter=",")
