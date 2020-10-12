import random

from numpy import median
from scipy.stats import median_abs_deviation as mad


class AdrMAD:
    def __init__(self, arr=None, k=1000, cut_off=2.0, r=0.5, w=1.0):
        self.cw = 0
        self.w = w
        self.r = r
        self.k = k
        self.reservoir = arr if arr else []
        self.cut_off = cut_off

    def is_outlier(self, point, cut_off=2.0):
        mad_val = mad(self.reservoir)
        med = median(self.reservoir)
        median_deviation = abs(point - med) / abs(med)
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

    def adr_decay(self):
        self.cw *= self.r
