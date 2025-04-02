import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting functionality"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_empty_list():
    """Test sorting an empty list"""
    assert sleep_sort([]) == [], "Empty list should return empty list"

def test_sleep_sort_single_element():
    """Test sorting a single-element list"""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Single-element list should remain unchanged"

def test_sleep_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    result = sleep_sort(input_list)
    assert result == input_list, "Already sorted list should remain in the same order"

def test_sleep_sort_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_with_zero():
    """Test sorting a list that includes zero"""
    input_list = [5, 0, 3, 2, 1]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_sleep_sort_performance():
    """Ensure sorting doesn't take unreasonably long"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    start_time = time.time()
    sleep_sort(input_list)
    end_time = time.time()
    
    # Sorting should complete within a reasonable time 
    # (max time is max value * 0.001 + some overhead)
    assert end_time - start_time < 0.1, "Sleep sort took too long to complete"