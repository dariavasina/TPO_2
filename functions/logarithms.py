EPSILON = 1e-10


def ln_taylor(x, eps=EPSILON):
    if x <= 0:
        raise ValueError("ln(x) is undefined for  x <= 0")

    y = (x - 1) / (x + 1)
    term = 2 * y
    result = term
    n = 1

    while abs(term) > eps:
        term = 2 * (y ** (2 * n + 1)) / (2 * n + 1)
        result += term
        n += 1

    return result


def log_base(x, base, eps=EPSILON):
    if base <= 0 or base == 1:
        raise ValueError("log is undefined for base <= 0 and base == 1") 
    return ln_taylor(x, eps) / ln_taylor(base, eps)
