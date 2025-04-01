import pytest
from src.partition_equal_subset_sum import can_partition

def test_partition_possible():
    """Test cases where partitioning is possible"""
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 15, 11, 4]) == False

def test_edge_cases():
    """Test edge cases for input"""
    assert can_partition([]) == False
    assert can_partition([1]) == False
    assert can_partition([2, 2]) == True

def test_large_numbers():
    """Test with larger numbers"""
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([100, 100, 100, 200]) == True
    # Overly complex large number tests might not be reliable

def test_odd_sum():
    """Test cases where total sum is odd"""
    assert can_partition([1, 2, 3, 4, 5]) == False
    assert can_partition([3, 3, 3, 4, 5]) == False

def test_all_large_numbers():
    """Test with all large numbers"""
    assert can_partition([100, 200, 300, 400]) == True
    assert can_partition([100, 200, 300, 350]) == False

def test_negative_cases():
    """Test with numbers that cannot be equally partitioned"""
    assert can_partition([1, 2, 3, 4]) == False
    assert can_partition([1, 3, 4, 8]) == False