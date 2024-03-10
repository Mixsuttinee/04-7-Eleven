# test_seven_eleven.py

"""Test case for Seven-Eleven package."""

# Standard Library

# 3rd Party Library
import pytest

# Project Library
from seven_eleven import to_seven_eleven

#-------------------------------------------------------
@pytest.mark.parametrize(
    "number, expected",
    [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (76, '76'),
        (78, '78'),
    ]
)
def test_number(number, expected):
    """Test numbers not divisible by 7 or 11."""
    assert to_seven_eleven(number) == expected

@pytest.mark.parametrize(
    "number, expected",
    [
        (7, 'seven'),
        (14, 'seven'),
        (21, 'seven'),
        (28, 'seven'),
        (35, 'seven'),
        (42, 'seven'),
        (49, 'seven'),
        (56, 'seven'),
        (98, 'seven'),
        (189, 'seven'),
    ]
)
def test_print_seven(number, expected):
    """Test numbers divisible by 7."""
    assert to_seven_eleven(number) == expected

@pytest.mark.parametrize(
    "number, expected",
    [
        (11, 'eleven'),
        (22, 'eleven'),
        (33, 'eleven'),
        (44, 'eleven'),
        (55, 'eleven'),
        (66, 'eleven'),
        (88, 'eleven'),
        (99, 'eleven'),
        (110, 'eleven'),
        (198, 'eleven'),
    ]
)
def test_print_eleven(number, expected):
    """Test numbers divisible by 11."""
    assert to_seven_eleven(number) == expected

@pytest.mark.parametrize(
    "number, expected",
    [
        (77, '7-Eleven'),
        (154, '7-Eleven'),
        (231, '7-Eleven'),
    ]
)
def test_print_seven_eleven(number, expected):
    """Test numbers divisible by both 7 and 11."""
    assert to_seven_eleven(number) == expected
