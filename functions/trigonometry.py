import math


EPSILON = 1e-10


def sin_taylor(x, eps=EPSILON):
    n = 0
    result = 0
    term = math.inf

    while abs(term) >= eps:
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        result += term
        n += 1

    return result


def cos_taylor(x, eps=EPSILON):
    return sin_taylor(math.pi / 2 - x, eps)
