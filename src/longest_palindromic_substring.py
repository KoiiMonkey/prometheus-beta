def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring within the given string.
    
    A palindrome is a string that reads the same backward as forward.
    If multiple palindromic substrings exist with the same maximum length,
    return the first one encountered.
    
    Args:
        s (str): The input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s or len(s) < 1:
        return ""
    
    start, max_length = 0, 0
    
    def expand_around_center(left: int, right: int) -> int:
        """Helper function to expand around a center and find palindrome length."""
        while left >= 0 and right < len(s) and s[left].lower() == s[right].lower():
            left -= 1
            right += 1
        return right - left - 1
    
    # Iterate through each character as potential center of palindrome
    for i in range(len(s)):
        # Check odd-length palindromes
        odd_length = expand_around_center(i, i)
        # Check even-length palindromes
        even_length = expand_around_center(i, i + 1)
        
        # Update max length and start index
        current_max = max(odd_length, even_length)
        if current_max > max_length:
            max_length = current_max
            # Calculate start index based on current center and length
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_length]