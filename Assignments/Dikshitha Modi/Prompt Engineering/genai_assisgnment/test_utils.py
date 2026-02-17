# Exercise 3 — Test Generation

import pytest
from utils import divide

# Happy path tests
def test_divide_normal():
    assert divide(10, 2) == 5

# Edge cases
def test_divide_negative():
    assert divide(-10, 2) == -5

def test_divide_float():
    assert divide(5, 2) == 2.5

# Error handling
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
