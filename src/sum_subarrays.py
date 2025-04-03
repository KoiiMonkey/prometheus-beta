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
    
    # Generate all possible subarrays
    for start in range(len(arr)):
        current_sum = 0
        for end in range(start, len(arr)):
            # Add current element to sum
            current_sum += arr[end]
            
            # Check if current subarray length is <= k
            if end - start + 1 <= k:
                total_sum += current_sum
            else:
                # Stop if subarray exceeds k
                break
    
    return total_sum