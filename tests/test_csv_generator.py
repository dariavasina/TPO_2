import pytest
import os
import csv
from unittest.mock import patch, mock_open
from functions.csv_generator import generate_csv


TEST_FILENAME = "test_results.csv"
EPSILON = 1e-10


@pytest.fixture(autouse=True)
def cleanup_test_files():
    yield
    if os.path.exists(TEST_FILENAME):
        os.remove(TEST_FILENAME)


def test_generate_csv_creates_file():
    generate_csv(0, 1, 0.5, TEST_FILENAME)
    assert os.path.exists(TEST_FILENAME), "CSV file was not created"


def test_generate_csv_content():
    start, end, step = 0, 1, 0.5
    generate_csv(start, end, step, TEST_FILENAME)

    with open(TEST_FILENAME, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        assert len(rows) == 3, f"Expected 3 rows (0, 0.5, 1), got {len(rows)}"

        x_values = [float(row[0]) for row in rows]
        assert x_values == [
            0.0,
            0.5,
            1.0,
        ], f"Expected x values [0.0, 0.5, 1.0], got {x_values}"

        for row in rows:
            assert len(row) == 2, f"Expected 2 columns per row, got {len(row)}"


def test_generate_csv_with_custom_delimiter():
    delimiter = ";"
    generate_csv(0, 1, 1, TEST_FILENAME, delimiter=delimiter)

    with open(TEST_FILENAME, mode="r") as file:
        content = file.read()
        assert (
            delimiter in content
        ), f"Custom delimiter '{delimiter}' not found in CSV content"


@patch("functions.csv_generator.system_function")
def test_generate_csv_handles_exceptions(mock_system_function):

    def side_effect(x, eps):
        if x == 1:
            raise ValueError("Test exception")
        return x * 2

    mock_system_function.side_effect = side_effect

    generate_csv(0, 2, 1, TEST_FILENAME)

    with open(TEST_FILENAME, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        assert len(rows) == 3

        assert rows[1][0] == "1"
        assert rows[1][1] == ""


def test_generate_csv_with_empty_range():
    generate_csv(10, 5, 1, TEST_FILENAME)

    with open(TEST_FILENAME, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        assert len(rows) == 0


@pytest.mark.parametrize("step", [0, -1])
def test_generate_csv_with_invalid_step(step):
    with pytest.raises(Exception):
        generate_csv(0, 10, step, TEST_FILENAME)
        generate_csv(0, 10, step, TEST_FILENAME)
