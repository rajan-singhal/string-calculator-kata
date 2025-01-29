import pytest
from string_calculator import add
def test_empty_string():
	"""it should return 0 if the string is empty"""
	assert add('') == 0