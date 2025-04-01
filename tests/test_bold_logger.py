import pytest
from src.bold_logger import log_bold

def test_log_bold_basic():
    """Test basic bold text formatting"""
    assert log_bold("Hello") == "\033[1mHello\033[0m"

def test_log_bold_empty_string():
    """Test bold formatting with an empty string"""
    assert log_bold("") == "\033[1m\033[0m"

def test_log_bold_with_spaces():
    """Test bold formatting with spaces"""
    assert log_bold("  Hello World  ") == "\033[1m  Hello World  \033[0m"

def test_log_bold_with_special_characters():
    """Test bold formatting with special characters"""
    assert log_bold("Hello, World!") == "\033[1mHello, World!\033[0m"

def test_log_bold_type_error():
    """Test that a TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(["Hello"])