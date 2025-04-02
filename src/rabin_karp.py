def rabin_karp_search(text, pattern):
    """
    Implement the Rabin-Karp algorithm for string pattern matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Prime number for hash calculation to reduce collisions
    prime = 101
    
    # Base for rolling hash (using a prime base)
    base = 256
    
    # Length of pattern and text
    m, n = len(pattern), len(text)
    
    # Compute the hash value for the pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Compute h = base^(m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime
    
    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # List to store matching indices
    matches = []
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # If hash matches, do character by character comparison
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Compute hash for next window of text
        if i < n - m:
            # Remove leading digit, add trailing digit
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # We might get negative values, convert to positive
            if text_hash < 0:
                text_hash += prime
    
    return matches