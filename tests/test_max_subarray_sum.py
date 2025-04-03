import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]) == 10

def test_all_negative():
    """Test with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_empty_array():
    """Test with an empty array."""
    assert max_subarray_sum([]) == 0

def test_single_element_positive():
    """Test with a single positive element."""
    assert max_subarray_sum([42]) == 42

def test_single_element_negative():
    """Test with a single negative element."""
    assert max_subarray_sum([-42]) == -42

def test_alternating_signs():
    """Test with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_subarray_sum("not a list")

def test_invalid_input_non_numeric():
    """Test that TypeError is raised for non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        max_subarray_sum([1, 2, "3", 4])

def test_floating_point_numbers():
    """Test with floating point numbers."""
    assert max_subarray_sum([1.5, -2.5, 3.7, 4.2]) == 6.4