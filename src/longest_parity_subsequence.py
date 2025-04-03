def longest_parity_subsequence(nums):
    """
    Find the longest subsequence with the same parity (all even or all odd).
    
    Args:
        nums (list[int]): Input list of integers
    
    Returns:
        list[int]: Longest subsequence with consistent parity
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Track the longest subsequences for even and odd parities
    even_subsequence = []
    odd_subsequence = []
    
    # Track the best subsequence
    best_subsequence = []
    
    for num in nums:
        # Determine current number's parity
        is_even = num % 2 == 0
        
        # Reset or extend even subsequence
        if is_even:
            even_subsequence = even_subsequence + [num] if even_subsequence and even_subsequence[-1] % 2 == 0 else [num]
        # Reset or extend odd subsequence
        else:
            odd_subsequence = odd_subsequence + [num] if odd_subsequence and odd_subsequence[-1] % 2 != 0 else [num]
        
        # Update best subsequence based on length
        best_subsequence = max(even_subsequence, odd_subsequence, key=len)
    
    return best_subsequence