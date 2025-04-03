import pytest
from src.fizzy_numbers import find_fizzy_numbers

def test_basic_fizzy_numbers():
    """Test basic functionality of finding fizzy numbers."""
    assert find_fizzy_numbers(10) == [3, 6, 7, 9]

def test_larger_range():
    """Test finding fizzy numbers in a larger range."""
    result = find_fizzy_numbers(20)
    expected = [3, 6, 7, 9, 12, 14, 15, 18]
    assert result == expected

def test_minimum_fizzy_number():
    """Test the smallest possible fizzy number."""
    assert find_fizzy_numbers(1) == []
    assert find_fizzy_numbers(3) == [3]
    assert find_fizzy_numbers(7) == [3, 6, 7]

def test_only_divisible_by_3():
    """Test numbers only divisible by 3."""
    result = find_fizzy_numbers(6)
    assert 3 in result and 6 in result
    assert 7 not in result

def test_only_divisible_by_7():
    """Test numbers only divisible by 7."""
    result = find_fizzy_numbers(14)
    assert 7 in result and 14 in result
    assert 3 in result

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        find_fizzy_numbers("10")