import pytest
from src.string_transform import string_transform

def test_string_transform_basic():
    """Test basic string transformation."""
    assert string_transform("Hello World") == "dlrow*h*o"

def test_string_transform_mixed_case():
    """Test transformation with mixed case letters."""
    assert string_transform("Python Programming") == "gnimm*rg*p*nht*yp"

def test_string_transform_empty_string():
    """Test transformation of an empty string."""
    assert string_transform("") == ""

def test_string_transform_no_spaces():
    """Test transformation of a string without spaces."""
    assert string_transform("NoSpaces") == "secsp*on"

def test_string_transform_only_spaces():
    """Test transformation of a string with only spaces."""
    assert string_transform("   ") == ""

def test_string_transform_with_numbers_and_symbols():
    """Test transformation with numbers and symbols."""
    assert string_transform("Hello 123 World!") == "!dlrow321*h*o"

def test_string_transform_with_multiple_a_chars():
    """Test transformation with multiple 'a' characters."""
    assert string_transform("banana") == "*n*n*b"