import pytest
from src.longest_parity_subsequence import longest_parity_subsequence

def test_mixed_parity_sequence():
    """Test a mixed sequence returns the longest parity subsequence"""
    assert longest_parity_subsequence([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
    assert longest_parity_subsequence([1, 3, 5, 2, 4, 6, 8]) == [2, 4, 6, 8]

def test_all_even_sequence():
    """Test a sequence with all even numbers"""
    assert longest_parity_subsequence([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]

def test_all_odd_sequence():
    """Test a sequence with all odd numbers"""
    assert longest_parity_subsequence([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_single_even_number():
    """Test a sequence with a single even number"""
    assert longest_parity_subsequence([2]) == [2]

def test_single_odd_number():
    """Test a sequence with a single odd number"""
    assert longest_parity_subsequence([1]) == [1]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        longest_parity_subsequence([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        longest_parity_subsequence("not a list")
        longest_parity_subsequence(123)

def test_duplicate_parity_sequence():
    """Test a sequence with multiple subsequences of same parity length"""
    result = longest_parity_subsequence([1, 3, 5, 2, 4, 6])
    assert len(result) == 3
    assert all(num % 2 == 0 for num in result) or all(num % 2 != 0 for num in result)

def test_alternating_parity_sequence():
    """Test an alternating parity sequence"""
    assert longest_parity_subsequence([1, 2, 3, 4, 5, 6]) == [2, 4, 6]