import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_normal_case():
    """Test bitwise AND for a standard range of numbers."""
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_same_number():
    """Test when lower and upper bounds are the same."""
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_zero():
    """Test with zero and another number."""
    assert bitwise_and_range(0, 1) == 0

def test_bitwise_and_range_large_numbers():
    """Test with larger numbers."""
    assert bitwise_and_range(12, 15) == 12

def test_bitwise_and_range_error_negative_lower():
    """Test error handling for negative lower bound."""
    with pytest.raises(ValueError, match="Input numbers must be non-negative"):
        bitwise_and_range(-1, 5)

def test_bitwise_and_range_error_negative_upper():
    """Test error handling for negative upper bound."""
    with pytest.raises(ValueError, match="Input numbers must be non-negative"):
        bitwise_and_range(1, -5)

def test_bitwise_and_range_error_invalid_range():
    """Test error handling when lower bound is greater than upper bound."""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_zero_to_zero():
    """Test bitwise AND when range is [0, 0]."""
    assert bitwise_and_range(0, 0) == 0

def test_bitwise_and_range_larger_complex_case():
    """Test a more complex case with larger numbers."""
    assert bitwise_and_range(600000, 700000) == 524288