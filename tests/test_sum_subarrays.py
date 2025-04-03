import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_functionality():
    """Test normal case with valid inputs"""
    arr = [1, 2, 3, 4]
    k = 2
    assert sum_subarrays(arr, k) == 25  # (1), (2), (3), (4), (1,2), (2,3)

def test_single_element_array():
    """Test array with single element"""
    arr = [5]
    k = 1
    assert sum_subarrays(arr, k) == 5

def test_empty_array():
    """Test empty array"""
    arr = []
    k = 3
    assert sum_subarrays(arr, k) == 0

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    k = 0
    assert sum_subarrays(arr, k) == 0

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 5
    assert sum_subarrays(arr, k) == 20  # Sum of all possible subarrays

def test_negative_k_raises_error():
    """Test that negative k raises ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be non-negative"):
        sum_subarrays(arr, -1)

def test_none_array_raises_error():
    """Test that None array raises ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        sum_subarrays(None, 3)

def test_large_array():
    """Test with a larger array"""
    arr = [10, 20, 30, 40, 50]
    k = 3
    assert sum_subarrays(arr, k) == 660

def test_mixed_array():
    """Test array with mixed positive and negative numbers"""
    arr = [-1, 2, -3, 4, -5]
    k = 2
    # Sum of suitable subarrays
    assert sum_subarrays(arr, k) == 11