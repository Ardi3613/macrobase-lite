from scipy.stats import median_abs_deviation as mad
from numpy import median
import random


def is_outlier(arr, point, cut_off=2.0):
    mad_val = mad(arr)
    med = median(arr)
    median_deviation = abs(point - med) / abs(med)
    return median_deviation > (cut_off * mad_val)


def adr_update(reservoir, x, cw, w, k):
    cw += w
    prob = k/cw
    r_len = len(reservoir)
    if r_len < k:
        reservoir.append(x)
    elif random.random() < prob:
        ind = random.randint(0 , r_len-1)
        reservoir.pop(ind)
    return cw

def adr_decay(cw, w):
    return cw * w
