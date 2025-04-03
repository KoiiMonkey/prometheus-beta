import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindromic substring scenarios."""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"

def test_edge_cases():
    """Test edge cases like empty string and no palindromes."""
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring(" ") == " "

def test_longer_palindromes():
    """Test longer and more complex palindromes."""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_multiple_palindromes():
    """Test scenarios with multiple palindromes of same length."""
    result = longest_palindromic_substring("abcba")
    assert result == "abcba"
    
    result = longest_palindromic_substring("aacabdkacaa")
    assert result == "aca"

def test_no_complete_palindrome():
    """Test cases where no complete palindrome exists."""
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]

def test_repeated_characters():
    """Test cases with repeated characters."""
    assert longest_palindromic_substring("aaaaa") == "aaaaa"
    assert longest_palindromic_substring("abcddcba") == "abcddcba"

def test_mixed_case_and_special_chars():
    """Test mixed case and special characters."""
    assert longest_palindromic_substring("A man a plan a canal Panama") == " a plan a canal "
    assert longest_palindromic_substring("race a car") == " a "

def test_performance_and_boundaries():
    """Test performance with reasonable input size."""
    # Very long input to test performance
    long_input = "a" * 1000 + "b" * 1000
    assert longest_palindromic_substring(long_input) == "a" * 1000