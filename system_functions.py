import math
import csv

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

def system_function(x, eps=EPSILON):
    """
    Вычисление составной функции:
    Для x <= 0:
      f(x) = (((((sin(x)*cos(x))^3)^2 * cos(x))^2)
    Для x > 0:
      f(x) = (((((log2(x) - ln(x))*log10(x))/log10(x)) - log2(x)) / (log3(x)*log5(x)))
    Все логарифмы вычисляются через ln(x).
    """
    if x <= 0:
        sin_val = sin_taylor(x, eps)
        cos_val = cos_taylor(x, eps)
        # Вычисляем ((((sin(x)*cos(x))^3)^2 * cos(x))^2)
        part1 = (sin_val * cos_val) ** 3
        part2 = part1 ** 2
        part3 = part2 * cos_val
        result = part3 ** 2
        return result
    else:
        ln_val = ln_taylor(x, eps)
        log2_val = log_base(x, 2, eps)
        log10_val = log_base(x, 10, eps)
        log3_val = log_base(x, 3, eps)
        log5_val = log_base(x, 5, eps)
        # Вычисляем (((((log2 - ln)*log10)/log10) - log2) / (log3*log5))
        temp1 = log2_val - ln_val
        temp2 = temp1 * log10_val
        temp3 = temp2 / log10_val  # Деление допустимо, т.к. x>0 (за исключением x=1, где log10(1)=0)
        temp4 = temp3 - log2_val
        denominator = log3_val * log5_val
        result = temp4 / denominator
        return result

def generate_csv(start, end, step, filename, eps=EPSILON):
    """
    Генерация csv-файла с двумя столбцами: x и system_function(x).
    Параметры:
      start – начальное значение x,
      end – конечное значение x,
      step – шаг изменения x,
      filename – имя файла для сохранения.
    """
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        x = start
        while x <= end:
            try:
                result = system_function(x, eps)
            except Exception as e:
                result = str(e)
            writer.writerow([x, result])
            x += step

if __name__ == "__main__":
    generate_csv(-5, 5, 0.5, "results.csv")
