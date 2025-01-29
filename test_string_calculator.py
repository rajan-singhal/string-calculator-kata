import pytest
from string_calculator import add
def test_add_empty_string_return_zero():
	"""it should return 0 if the string is empty"""
	assert add('') == 0

def test_add_single_value_string_return_value_itself():
	"""it should return value itself if the string is single value"""
	assert add('1') == 1

def test_add_two_csv_numbers_string():
	"""
    Test case: Adding two numbers should return their sum.
    Input: "1,2"
    Expected Output: 3
    """
	assert add('1,2') == 3

def test_add_multiple_numbers():
    """
    Test case: Adding multiple numbers should return their sum.
    Input: "1,2,3,4,5"
    Expected Output: 15
    """
    assert add("1,2,3,4,5") == 15