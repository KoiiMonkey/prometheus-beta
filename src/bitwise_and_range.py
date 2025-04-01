def bitwise_and_range(m: int, n: int) -> int:
    """
    Calculate the bitwise AND of all numbers in the range [m, n].
    
    This function finds the bitwise AND of all integers from m to n (inclusive).
    It uses a bit manipulation technique to efficiently compute the result.
    
    Args:
        m (int): The lower bound of the range (inclusive)
        n (int): The upper bound of the range (inclusive)
    
    Returns:
        int: The bitwise AND of all numbers in the range
    
    Raises:
        ValueError: If m or n is negative, or if m > n
    
    Examples:
        >>> bitwise_and_range(5, 7)
        4
        >>> bitwise_and_range(0, 1)
        0
    """
    # Validate input
    if m < 0 or n < 0:
        raise ValueError("Input numbers must be non-negative")
    
    if m > n:
        raise ValueError("Lower bound must be less than or equal to upper bound")
    
    # If m and n are different, we need to find the common prefix
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    
    # Shift back to get the result
    return m << shift