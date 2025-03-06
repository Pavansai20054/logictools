import pytest
from logictools import math_utils

def test_factorial():
    assert math_utils.factorial(5) == 120
    assert math_utils.factorial(0) == 1
