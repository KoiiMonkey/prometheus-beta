import pytest
from src.switch_cases import switch_cases

def test_basic_case_switching():
    """Test basic case switching for alphabetic characters"""
    assert switch_cases("Hello", "World") == "hELLO"
    assert switch_cases("PytHON", "Test") == "pYThon"

def test_mixed_case():
    """Test strings with mixed case"""
    assert switch_cases("HeLLo WoRLd", "Test") == "hEllO wOrlD"

def test_non_alphabetic_characters():
    """Test handling of non-alphabetic characters"""
    assert switch_cases("Hello123!", "Test") == "hELLO123!"

def test_empty_string():
    """Test empty string input"""
    assert switch_cases("", "Test") == ""

def test_different_length_strings():
    """Test case switching with strings of different lengths"""
    assert switch_cases("Short", "Longer Test String") == "sHORT"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        switch_cases(123, "Test")
    
    with pytest.raises(TypeError):
        switch_cases("Hello", ["Not", "A", "String"])
    
    with pytest.raises(TypeError):
        switch_cases(None, "Test")