import pytest
from src.alternating_case import convert_to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert convert_to_alternating_path_case("hello world") == "Hello-world"
    assert convert_to_alternating_path_case("python programming language") == "Python_programming-Language"

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_alternating_path_case("hello") == "Hello"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_path_case("") == ""

def test_multiple_words():
    """Test conversion of multiple words with alternating separators."""
    assert convert_to_alternating_path_case("a b c d e") == "A-b_c-d_E"

def test_invalid_input():
    """Test that invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(None)
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)

def test_leading_trailing_spaces():
    """Test handling of leading and trailing spaces."""
    assert convert_to_alternating_path_case("  hello  world  ") == "Hello-world"

def test_multiple_spaces():
    """Test handling of multiple consecutive spaces."""
    assert convert_to_alternating_path_case("hello    world") == "Hello-world"