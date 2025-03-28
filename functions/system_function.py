from functions.trigonometry import *
from functions.logarithms import *

EPSILON = 1e-10


def system_function(x, eps=EPSILON):
    if x <= 0:
        sin_val = sin_taylor(x, eps)
        cos_val = cos_taylor(x, eps)
        return ((((sin_val * cos_val) ** 3) ** 2) * cos_val) ** 2
    else:
        ln_val = ln_taylor(x, eps)
        log2_val = log_base(x, 2, eps)
        log3_val = log_base(x, 3, eps)
        log5_val = log_base(x, 5, eps)
        log10_val = log_base(x, 10, eps)
        return (((log2_val - ln_val) * log10_val) / log10_val - log2_val) / (
            log3_val * log5_val
        )
