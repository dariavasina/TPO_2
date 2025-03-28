import pytest
from math import pi as PI
from math import sin, cos, isclose
from functions.trigonometry import sin_taylor, cos_taylor
from unittest.mock import patch

EPSILON = 1e-10


@pytest.mark.parametrize(
    "x, expected",
    [
        (0.0, 0.0),
        (PI / 2, 1.0),
        (PI, 0.0),
        (-PI / 2, -1.0),
        (2.0, 0.9092974268256817),
        (3.0, 0.1411200080598672),
    ],
)
def test_sin_taylor(x, expected):
    result = sin_taylor(x)
    assert isclose(
        result, expected, abs_tol=EPSILON
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "x, expected",
    [
        (0.0, 1.0),
        (PI / 2, 0.0),
        (PI, -1.0),
        (-PI / 2, 0.0),
        (2.0, -0.4161468365471424),
        (3.0, -0.9899924966004454),
    ],
)
def test_cos_taylor(x, expected):
    result = cos_taylor(x)
    assert isclose(
        result, expected, abs_tol=EPSILON
    ), f"Expected {expected}, got {result}"


@pytest.mark.parametrize(
    "x, expected, sin_value",
    [
        (0.0, 1.0, sin(PI / 2)),
        (PI / 2, 0.0, sin(0)),
        (PI, -1.0, sin(-PI / 2)),
        (PI / 4, cos(PI / 4), sin(PI / 2 - PI / 4)),
        (-2, cos(-2), sin(PI / 2 + 2)),
        (3, cos(3), sin(PI / 2 - 3)),
    ],
)
def test_cos_with_mock(x, expected, sin_value):
    with patch("functions.trigonometry.sin_taylor") as mock_sin:
        mock_sin.return_value = sin_value

        result = cos_taylor(x)

        assert isclose(result, expected, abs_tol=EPSILON)

        mock_sin.assert_called_once()
        call_arg = mock_sin.call_args[0][0]  # Get the first positional argument
        assert isclose(call_arg, PI / 2 - x, abs_tol=EPSILON)


@pytest.mark.parametrize(
    "x",
    [
        0.0,
        PI / 2,
        PI,
        -PI / 2,
        2.0,
        3.0,
    ],
)
def test_taylor_accuracy(x):
    result_sin = sin_taylor(x)
    expected_sin = sin(x)
    assert isclose(
        result_sin, expected_sin, abs_tol=EPSILON
    ), f"sin_taylor({x}) = {result_sin}, expected {expected_sin}"

    result_cos = cos_taylor(x)
    expected_cos = cos(x)
    assert isclose(
        result_cos, expected_cos, abs_tol=EPSILON
    ), f"cos_taylor({x}) = {result_cos}, expected {expected_cos}"
