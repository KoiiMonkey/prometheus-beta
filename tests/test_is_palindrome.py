import pytest
from src.is_palindrome import is_palindrome

def test_palindrome_basic():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True
    assert is_palindrome("race a car") == False

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation and mixed case"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_palindrome_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string is a palindrome
    assert is_palindrome(" ") == True  # String with only spaces
    assert is_palindrome("!@#$%^&*()") == True  # String with only punctuation

def test_palindrome_negative_cases():
    """Test non-palindrome cases"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("not a palindrome") == False

def test_palindrome_numbers():
    """Test palindrome numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_palindrome_mixed_characters():
    """Test palindromes with mixed alphanumeric characters"""
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False