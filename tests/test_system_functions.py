import pytest
from math import isclose
from functions.system_function import system_function
from unittest.mock import patch

EPSILON = 1e-3


@pytest.mark.parametrize(
    "x, expected",
    [
        (-12, 0.00005288),
        (-4, 0.00009174),
        (-1, 0.00002277),
        (0, 0),
        (2, -2.5508987383),
        (4, -1.2754493691),
        (23, -0.56391373),
    ],
)
def test_system_function_values(x, expected):
    result = system_function(x)
    assert isclose(result, expected, abs_tol=EPSILON), f"For x={x}, expected {expected}, got {result}"


@pytest.mark.parametrize(
    "invalid_input",
    [
        1,  # division by zero
        "aaaa"
    ]
)
def test_system_function_invalid_input(invalid_input):
    """Test that system_function raises ValueError for invalid inputs"""
    with pytest.raises(Exception):
        system_function(invalid_input)


