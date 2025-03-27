import pytest
from math import isclose
from functions.logarithms import ln_taylor, log_base

EPSILON = 1e-10

# Тест для ln_taylor
@pytest.mark.parametrize("x, expected", [
    (1.0, 0.0),              # ln(1) = 0
    (2.718281828459045, 1.0), # ln(e) ≈ 1
    (10.0, 2.302585092994046), # ln(10) ≈ 2.302585
    (0.5, -0.6931471805599453), # ln(0.5) ≈ -0.693147
])
def test_ln_taylor(x, expected):
    result = ln_taylor(x)
    assert isclose(result, expected, abs_tol=EPSILON), f"Expected {expected}, got {result}"

# Тест на исключение для ln_taylor при x <= 0
@pytest.mark.parametrize("x", [
    0,   # Значение, которое должно вызвать ошибку
    -1.0 # Значение, которое должно вызвать ошибку
])
def test_ln_taylor_invalid_input(x):
    with pytest.raises(ValueError, match="ln(x) неопределён для x<=0"):
        ln_taylor(x)

# Тест для log_base
@pytest.mark.parametrize("x, base, expected", [
    (8.0, 2.0, 3.0),   # log2(8) = 3
    (100.0, 10.0, 2.0), # log10(100) = 2
    (27.0, 3.0, 3.0),   # log3(27) = 3
    (10.0, 10.0, 1.0),  # log10(10) = 1
])
def test_log_base(x, base, expected):
    result = log_base(x, base)
    assert isclose(result, expected, abs_tol=EPSILON), f"Expected {expected}, got {result}"

# Тест на исключение для log_base при x <= 0 или base <= 0 или base == 1
@pytest.mark.parametrize("x, base", [
    (0.0, 2.0),     # log(0) должно вызвать ошибку
    (-1.0, 2.0),    # log(-1) должно вызвать ошибку
    (10.0, 1.0),    # log с base = 1 должно вызвать ошибку
    (10.0, -2.0),   # log с base <= 0 должно вызвать ошибку
])
def test_log_base_invalid_input(x, base):
    with pytest.raises(ValueError):
        log_base(x, base)
