import pytest
from logictools.math_utils import factorial, divide

class TestFactorial:
    def test_factorial_of_zero(self):
        assert factorial(0) == 1
    
    def test_factorial_of_one(self):
        assert factorial(1) == 1
    
    def test_factorial_of_positive_number(self):
        assert factorial(5) == 120
        assert factorial(7) == 5040
    
    def test_factorial_of_negative_number(self):
        with pytest.raises(ValueError) as excinfo:
            factorial(-3)
        assert "negative numbers" in str(excinfo.value)
    
    def test_factorial_input_type(self):
        with pytest.raises(TypeError) as excinfo:
            factorial("five")
        assert "must be an integer" in str(excinfo.value)
        
        with pytest.raises(TypeError):
            factorial(5.5)

class TestDivide:
    def test_divide_normal_case(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
    
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError) as excinfo:
            divide(10, 0)
        assert "Cannot divide by zero" in str(excinfo.value)
    
    def test_divide_floats(self):
        assert divide(5.5, 2) == 2.75
        assert divide(4, 2.5) == 1.6
    
    def test_divide_invalid_input(self):
        with pytest.raises(TypeError):
            divide("10", 2)
        with pytest.raises(TypeError):
            divide(10, "2")
        with pytest.raises(TypeError):
            divide([], 2)