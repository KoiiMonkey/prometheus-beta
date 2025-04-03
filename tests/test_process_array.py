import pytest
from src.process_array import process_array

def test_process_array_basic():
    """Test basic functionality of process_array"""
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Expected: 
    # Modified array would be [1, 2, 6, 4, 5, 12, 7, 8, 18]
    # Even numbers to sum: 2, 4, 8 (excluding 6, 12, 18)
    assert process_array(input_array) == 14

def test_process_array_empty_list():
    """Test with an empty list"""
    assert process_array([]) == 0

def test_process_array_no_even_numbers():
    """Test with no even numbers"""
    assert process_array([1, 3, 5, 7, 9]) == 0

def test_process_array_all_even_numbers():
    """Test with all even numbers"""
    input_array = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    # Expected: 2, 4, 8, 10, 14, 16 (excluding 6, 12, 18)
    assert process_array(input_array) == 54

def test_process_array_with_floats():
    """Test with floating point numbers"""
    input_array = [1.5, 2.0, 3.0, 4.5, 5.0, 6.0]
    # Expected: 2.0 (because 4.5 is not an integer even number)
    assert process_array(input_array) == 2.0

def test_process_array_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        process_array("not a list")

def test_process_array_invalid_element_type():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        process_array([1, 2, "three", 4, 5])