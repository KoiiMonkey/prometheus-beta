import pytest
from src.partition_equal_subset_sum import can_partition

def test_partition_possible():
    """Test cases where partitioning is possible"""
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([2, 2, 3, 5]) == False
    assert can_partition([2, 2, 1, 1]) == True

def test_edge_cases():
    """Test edge cases for input"""
    assert can_partition([]) == False
    assert can_partition([1]) == False
    assert can_partition([2, 2]) == True
    assert can_partition([1, 1]) == True

def test_complex_cases():
    """Test more complex partitioning scenarios"""
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([1, 3, 4, 8]) == False
    assert can_partition([1, 2, 3, 5, 7]) == False

def test_repeated_numbers():
    """Test scenarios with repeated numbers"""
    assert can_partition([2, 2, 3, 5]) == False
    assert can_partition([2, 2, 2, 2]) == True
    assert can_partition([3, 3, 3, 3]) == True

def test_boundary_cases():
    """Test boundary conditions"""
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([100, 100, 100, 200]) == True
    assert can_partition([1, 2, 3, 4, 5]) == False