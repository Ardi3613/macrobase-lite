import random

from numpy import median
import pandas as pd
from scipy.stats import median_abs_deviation as mad


class AdrMAD:
    def __init__(self, arr=None, k=1000, cut_off=2.0, r=0.99, w=1.0, tuple_decay=True):
        self.w = w
        self.r = r
        self.k = k
        self.reservoir = arr if arr else []
        self.cw = len(self.reservoir) * self.w
        self.cut_off = cut_off
        self.tuple_decay = tuple_decay

    def get_outliers(self):
        return [self.is_outlier(x, batch=True) for x in self.reservoir]

    def is_outlier(self, point, cut_off=2.0, batch=False):
        mad_val = mad(self.reservoir)
        med = median(self.reservoir)
        median_deviation = abs(point - med) / abs(med)
        if not batch:
            self.adr_update(point)
        return median_deviation > (cut_off * mad_val)

    def adr_update(self, x):
        self.cw += self.w
        prob = self.k / self.cw
        r_len = len(self.reservoir)
        if r_len < self.k:
            self.reservoir.append(x)
        elif random.random() < prob:
            ind = random.randint(0, r_len - 1)
            self.reservoir.pop(ind)
        if self.tuple_decay:
            self.adr_decay()

    def adr_decay(self):
        self.cw *= self.r


def _outlier_str(x):
    return "outlier" if x else "inlier"


def filter_non_numeric(df):
    """Filter non-categorical columns away."""
    non_cat = [ind for ind, dtype in enumerate(df.dtypes) if dtype != "object"]
    return df[non_cat]


def batch_classify(df_in):
    df = filter_non_numeric(df_in)
    if len(df.columns) != 1:
        raise ValueError("batch_classify works only with univariate data")
    series_ind = df.columns[0]
    series = df[series_ind]
    adr = AdrMAD(series.to_list())
    outliers = adr.get_outliers()
    outliers = [_outlier_str(x) for x in outliers]
    return df_in.assign(outlier=outliers)
