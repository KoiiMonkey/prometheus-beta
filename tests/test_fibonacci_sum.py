import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic_cases():
    """Test basic cases of Fibonacci sum"""
    assert fibonacci_sum(1) == 0  # First Fibonacci number is 0
    assert fibonacci_sum(2) == 1  # Sum of first two numbers (0 + 1)
    assert fibonacci_sum(3) == 1  # Sum of first three numbers (0 + 1 + 0)
    assert fibonacci_sum(5) == 7  # Sum of first five numbers (0 + 1 + 1 + 2 + 3)

def test_fibonacci_sum_larger_input():
    """Test Fibonacci sum for larger input values"""
    assert fibonacci_sum(10) == 88  # Calculated sum of first 10 Fibonacci numbers

def test_fibonacci_sum_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")