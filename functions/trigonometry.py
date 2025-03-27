EPSILON = 1e-10

def sin_taylor(x, eps=EPSILON):
    result = 0.0
    term = x
    n = 1

    while abs(term) >= eps:
        result += term
        term *= (-1) * x * x / ((2 * n) * (2 * n + 1))
        n += 1

    return result

def cos_taylor(x, eps=EPSILON):
    """
    Вычисление cos(x) через разложение Тейлора.
    cos(x) = 1 - x^2/2! + x^4/4! - ...
    """
    term = 1.0
    result = term
    n = 1
    while abs(term) > eps:
        term = -term * x * x / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result