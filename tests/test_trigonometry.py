import pytest
from math import sin, cos, isclose
from functions.trigonometry import *

EPSILON = 1e-10

# Тест для sin_taylor
@pytest.mark.parametrize("x, expected", [
    (0.0, 0.0),                        # sin(0) = 0
    (1.5707963267948966, 1.0),          # sin(π/2) ≈ 1
    (3.141592653589793, 0.0),           # sin(π) = 0
    (-1.5707963267948966, -1.0),        # sin(-π/2) ≈ -1
    (3.0, 0.1411200080598672),         # sin(3) ≈ 0.141120008
])
def test_sin_taylor(x, expected):
    result = sin_taylor(x)
    assert isclose(result, expected, abs_tol=EPSILON), f"Expected {expected}, got {result}"

# Тест для cos_taylor
@pytest.mark.parametrize("x, expected", [
    (0.0, 1.0),                        # cos(0) = 1
    (1.5707963267948966, 0.0),          # cos(π/2) ≈ 0
    (3.141592653589793, -1.0),          # cos(π) = -1
    (-1.5707963267948966, 0.0),         # cos(-π/2) ≈ 0
    (3.0, -0.9899924966004454),        # cos(3) ≈ -0.989992
])
def test_cos_taylor(x, expected):
    result = cos_taylor(x)
    assert isclose(result, expected, abs_tol=EPSILON), f"Expected {expected}, got {result}"

# Тесты на синус и косинус с использованием стандартных функций для сравнения
@pytest.mark.parametrize("x", [
    0.0,  # sin(0), cos(0)
    1.5707963267948966,  # sin(π/2), cos(π/2)
    3.141592653589793,   # sin(π), cos(π)
    -1.5707963267948966, # sin(-π/2), cos(-π/2)
    3.0                  # sin(3), cos(3)
])
def test_sin_taylor_accuracy(x):
    result_sin = sin_taylor(x)
    expected_sin = sin(x)  # Сравниваем с точным значением из math.sin
    assert isclose(result_sin, expected_sin, abs_tol=EPSILON), f"sin_taylor({x}) = {result_sin}, expected {expected_sin}"

    result_cos = cos_taylor(x)
    expected_cos = cos(x)  # Сравниваем с точным значением из math.cos
    assert isclose(result_cos, expected_cos, abs_tol=EPSILON), f"cos_taylor({x}) = {result_cos}, expected {expected_cos}"
