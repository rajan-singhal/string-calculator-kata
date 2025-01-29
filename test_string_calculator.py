import pytest

def test_empty_string():
	"""it should return 0 if the string is empty"""
	assert string_calculator.add('') == 0