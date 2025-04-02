def recursive_power(base: float, exponent: int) -> float:
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (float): The base number to be raised to a power.
        exponent (int): The exponent (power) to raise the base to.
    
    Returns:
        float: The result of base raised to the exponent.
    
    Raises:
        TypeError: If base is not a number or exponent is not an integer.
        ValueError: If the exponent is negative.
    
    Examples:
        >>> recursive_power(2, 3)
        8.0
        >>> recursive_power(5, 0)
        1.0
        >>> recursive_power(10, 2)
        100.0
    """
    # Type checking
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    # Handle edge cases
    if exponent < 0:
        raise ValueError("Exponent cannot be negative")
    
    # Base cases
    if exponent == 0:
        return 1.0
    if exponent == 1:
        return float(base)
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)