import pytest
from src.max_increasing_subsequence_sum import max_increasing_subsequence_sum

def test_empty_array():
    assert max_increasing_subsequence_sum([]) == 0

def test_single_element():
    assert max_increasing_subsequence_sum([5]) == 5

def test_simple_increasing_sequence():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 5

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60]) == 60

def test_negative_numbers():
    assert max_increasing_subsequence_sum([-2, -1, 1, 2]) == 2

def test_complex_sequence():
    assert max_increasing_subsequence_sum([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 15

def test_all_decreasing():
    assert max_increasing_subsequence_sum([5, 4, 3, 2, 1]) == 5

def test_random_sequence():
    assert max_increasing_subsequence_sum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 9

def test_large_numbers():
    assert max_increasing_subsequence_sum([1000, 1, 1001, 1002, 1003]) == 1003