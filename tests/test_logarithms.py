import pytest
import math

from math import isclose
from math import e as E
from functions.logarithms import ln_taylor, log_base
from unittest.mock import patch

EPSILON = 1e-10


@pytest.mark.parametrize(
    "x, expected",
    [
        (1.0, 0.0),
        (E, 1.0),
        (10.0, 2.302585092994046),
        (0.5, -0.6931471805599453),
    ],
)
def test_ln_taylor(x, expected):
    result = ln_taylor(x)
    assert isclose(
        result, expected, abs_tol=EPSILON
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "x",
    [
        0,
        -1,
    ],
)
def test_ln_taylor_invalid_input(x):
    with pytest.raises(ValueError):
        ln_taylor(x)


@pytest.mark.parametrize(
    "x, base, expected",
    [
        (8.0, 2.0, 3.0),
        (100.0, 10.0, 2.0),
        (27.0, 3.0, 3.0),
        (10.0, 10.0, 1.0),
    ],
)
def test_log_base(x, base, expected):
    result = log_base(x, base)
    assert isclose(
        result, expected, abs_tol=EPSILON
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "x, base",
    [
        (0.0, 2.0),
        (-1.0, 2.0),
        (10.0, 1.0),
        (10.0, -2.0),
    ],
)
def test_log_base_invalid_input(x, base):
    with pytest.raises(ValueError):
        log_base(x, base)


@pytest.mark.parametrize(
    "x, base, expected, mock_values",
    [
        (8, 2, 3, {8: math.log(8), 2: math.log(2)}),
        (16, 2, 4, {16: math.log(16), 2: math.log(2)}),
    ],
)
def test_log2_with_mock_ln(x, base, expected, mock_values):
    with patch("functions.logarithms.ln_taylor") as mock_ln:
        mock_ln.side_effect = lambda x, eps=EPSILON: mock_values.get(x, 0)

        result = log_base(x, base)
        assert isclose(result, expected, abs_tol=EPSILON)

        assert mock_ln.call_count == 2
        mock_ln.assert_any_call(x, EPSILON)
        mock_ln.assert_any_call(base, EPSILON)


@pytest.mark.parametrize(
    "x, base, expected, mock_values",
    [
        (100, 10, 2, {100: math.log(100), 10: math.log(10)}),
        (1000, 10, 3, {1000: math.log(1000), 10: math.log(10)}),
    ],
)
def test_log10_with_mock_ln(x, base, expected, mock_values):
    with patch("functions.logarithms.ln_taylor") as mock_ln:
        mock_ln.side_effect = lambda x, eps=EPSILON: mock_values.get(x, 0)

        result = log_base(x, base)

        assert isclose(result, expected, abs_tol=EPSILON)

        assert mock_ln.call_count == 2
        mock_ln.assert_any_call(x, EPSILON)
        mock_ln.assert_any_call(base, EPSILON)
