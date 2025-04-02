import pytest
from src.rabin_karp import rabin_karp_search

def test_basic_pattern_matching():
    """Test basic pattern matching"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [10]

def test_multiple_occurrences():
    """Test multiple occurrences of pattern"""
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    assert rabin_karp_search(text, pattern) == [0, 10, 15]

def test_no_match():
    """Test when pattern is not in text"""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert rabin_karp_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "LONGER PATTERN"
    assert rabin_karp_search(text, pattern) == []

def test_case_sensitive():
    """Test case sensitivity"""
    text = "Hello World"
    pattern = "world"
    assert rabin_karp_search(text, pattern) == []
    
    pattern = "World"
    assert rabin_karp_search(text, pattern) == [6]

def test_entire_text_match():
    """Test when entire text matches the pattern"""
    text = "ABABCABAB"
    pattern = "ABABCABAB"
    assert rabin_karp_search(text, pattern) == [0]

def test_single_character_match():
    """Test matching single character"""
    text = "ABCDEFG"
    pattern = "C"
    assert rabin_karp_search(text, pattern) == [2]

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        rabin_karp_search(123, "pattern")
    
    with pytest.raises(TypeError):
        rabin_karp_search("text", 456)

def test_empty_pattern():
    """Test handling of empty pattern"""
    with pytest.raises(ValueError):
        rabin_karp_search("text", "")