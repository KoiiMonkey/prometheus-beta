def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a given array of integers.
    
    This function uses Kadane's algorithm to efficiently find the maximum subarray sum
    in linear time complexity O(n).
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input array.
        If the array is empty, returns 0.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    
    Examples:
        >>> max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4])
        10
        >>> max_subarray_sum([-1, -2, -3, -4])
        -1
        >>> max_subarray_sum([])
        0
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty array
    if not arr:
        return 0
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far