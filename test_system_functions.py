import math
import pytest
from system_functions import sin_taylor, cos_taylor, ln_taylor, log_base, system_function, generate_csv

def test_sin_taylor():
    for x in [-math.pi, -math.pi/2, 0, math.pi/2, math.pi]:
        print(sin_taylor(x))
        print(math.sin(x))
        assert math.isclose(sin_taylor(x), math.sin(x), rel_tol=1e-8)

def test_cos_taylor():
    for x in [-math.pi, -math.pi/2, 0, math.pi/2, math.pi]:
        assert math.isclose(cos_taylor(x), math.cos(x), rel_tol=1e-8)

def test_ln_taylor():
    for x in [0.5, 1, 2, math.e, 10]:
        assert math.isclose(ln_taylor(x), math.log(x), rel_tol=1e-8)

def test_log_base():
    for x in [2, 10, math.e]:
        for base in [2, 3, 10]:
            expected = math.log(x) / math.log(base)
            assert math.isclose(log_base(x, base), expected, rel_tol=1e-8)

def test_system_function_negative():
    for x in [-1, -math.pi, -2.5]:
        result = system_function(x)
        assert result >= 0

def test_system_function_positive():
    for x in [0.5, 2, 10]:
        ln_val = math.log(x)
        log3_val = math.log(x) / math.log(3)
        log5_val = math.log(x) / math.log(5)
        expected = (-ln_val) / (log3_val * log5_val) if log3_val * log5_val != 0 else None
        result = system_function(x)
        if expected is not None:
            assert math.isclose(result, expected, rel_tol=1e-8)

def test_csv_generation(tmp_path):
    filename = tmp_path / "test_results.csv"
    generate_csv(-1, 1, 0.5, filename)
    with open(filename, "r") as f:
        lines = f.readlines()
    assert len(lines) == 5
