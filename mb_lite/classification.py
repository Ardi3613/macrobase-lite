from scipy.stats import median_abs_deviation as mad
from numpy import median


def is_outlier(arr, point, cut_off=2.0):
    mad_val = mad(arr)
    med = median(arr)
    median_deviation = abs(point - med) / abs(med)
    return median_deviation > (cut_off * mad_val)
