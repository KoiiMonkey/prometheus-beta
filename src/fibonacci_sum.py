def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci 
                 sequence elements to sum.
    
    Returns:
        int: The sum of the first n Fibonacci numbers.
    
    Raises:
        ValueError: If n is not a positive integer.
    
    Examples:
        >>> fibonacci_sum(1)
        0
        >>> fibonacci_sum(2)
        1
        >>> fibonacci_sum(5)
        7
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Handle small n cases
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    # Initialize Fibonacci sequence and sum
    fib_prev, fib_curr = 0, 1
    fib_sum = 0
    
    # Iterate to calculate sum of first n Fibonacci numbers
    for _ in range(n):
        fib_sum += fib_prev
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    
    return fib_sum