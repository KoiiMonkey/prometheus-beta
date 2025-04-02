import pytest
import math
from src.recursive_power import recursive_power

def test_positive_integer_power():
    """Test power calculation with positive integers"""
    assert recursive_power(2, 3) == 8.0
    assert recursive_power(5, 2) == 25.0
    assert recursive_power(10, 0) == 1.0
    assert recursive_power(7, 1) == 7.0

def test_zero_exponent():
    """Test power calculation with zero exponent"""
    assert recursive_power(100, 0) == 1.0
    assert recursive_power(0, 0) == 1.0
    assert recursive_power(1, 0) == 1.0

def test_float_base():
    """Test power calculation with float base"""
    assert math.isclose(recursive_power(2.5, 2), 6.25)
    assert math.isclose(recursive_power(1.5, 3), 3.375)

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Negative exponent
    with pytest.raises(ValueError, match="Exponent cannot be negative"):
        recursive_power(2, -1)
    
    # Invalid base type
    with pytest.raises(TypeError, match="Base must be a number"):
        recursive_power("2", 2)
    
    # Invalid exponent type
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 2.5)

def test_edge_cases():
    """Test various edge cases"""
    assert recursive_power(1, 100) == 1.0
    assert recursive_power(0, 5) == 0.0