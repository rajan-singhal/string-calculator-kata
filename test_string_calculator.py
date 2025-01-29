import pytest
from string_calculator import add
def test_empty_string():
	"""it should return 0 if the string is empty"""
	assert add('') == 0

def test_single_value_string():
	"""it should return value itself if the string is single value"""
	assert add('1') == 1