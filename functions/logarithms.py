EPSILON = 1e-10

def ln_taylor(x, eps=EPSILON):
    """
    Вычисление натурального логарифма ln(x) через разложение Тейлора по формуле:
    ln(x) = 2 * sum_{n=0}∞ [ ((x-1)/(x+1))^(2n+1) / (2n+1) ]
    Данная формула сходится для всех x > 0.
    """
    if x <= 0:
        raise ValueError("ln(x) неопределён для x<=0")
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
    """
    Вычисление логарифма log_base(x) через натуральный логарифм.
    """
    return ln_taylor(x, eps) / ln_taylor(base, eps)