import pytest
from string_calculator import add


def test_add_empty_string_return_zero():
    """it should return 0 if the string is empty"""
    assert add("") == 0


def test_add_single_value_string_return_value_itself():
    """it should return value itself if the string is single value"""
    assert add("1") == 1


def test_add_two_csv_numbers_string():
    """
    Test case: Adding two numbers should return their sum.
    Input: "1,2"
    Expected Output: 3
    """
    assert add("1,2") == 3


def test_add_multiple_numbers():
    """
    Test case: Adding multiple numbers should return their sum.
    Input: "1,2,3,4,5"
    Expected Output: 15
    """
    assert add("1,2,3,4,5") == 15


def test_add_numbers_with_newlines():
    """
    Test case: Adding numbers separated by newlines should return their sum.
    Input: "1\n2,3"
    Expected Output: 6
    """
    assert add("1\n2\n3") == 6


def test_add_numbers_with_custom_delimiter():
    """
    Test case: Adding numbers separated by a custom delimiter should return their sum.
    Input: "//;\n1;2;3"
    Expected Output: 6
    """
    add("//;\n1;2;3") == 6


def test_add_negative_numbers():
    """
    Test case: Adding numbers with negative numbers should raise an exception.
    Input: "-1,2,3"
    Expected Output: "Negative numbers are not allowed: -1, -3"
    """
    with pytest.raises(ValueError) as exc_info:
        add("-1,2,-3")
    assert str(exc_info.value) == "Negative numbers are not allowed: -1, -3"


def test_add_ignore_numbers_greater_than_1000():
    """
    Test case: Numbers greater than 1000 should be ignored when calculating the sum.
    Input: "1,1001,2,3"
    Expected Output: 6
    """
    assert add("1,1001,2,3") == 6
