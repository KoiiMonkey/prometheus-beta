def sum_subarrays(arr, k):
    """
    Calculate the sum of all elements in subarrays with length less than or equal to k.
    
    Args:
        arr (list): A sorted list of integers
        k (int): Maximum subarray length to consider
    
    Returns:
        int: Sum of all elements in subarrays of length <= k
    
    Raises:
        ValueError: If k is negative or arr is None
    """
    # Validate inputs
    if arr is None:
        raise ValueError("Input array cannot be None")
    if k < 0:
        raise ValueError("k must be non-negative")
    
    # If k is 0, return 0
    if k == 0:
        return 0
    
    # Track total sum of valid subarrays
    total_sum = 0
    
    # Generate subarrays
    n = len(arr)
    for length in range(1, min(k, n) + 1):
        for start in range(n - length + 1):
            # Sum of this specific subarray
            total_sum += sum(arr[start:start+length])
    
    return total_sum