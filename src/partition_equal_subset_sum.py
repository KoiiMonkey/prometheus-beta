def can_partition(nums):
    """
    Determines if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * total_sum)
    Space Complexity: O(total_sum)
    
    Examples:
        >>> can_partition([1, 5, 11, 5])
        True
        >>> can_partition([1, 2, 3, 5])
        False
    """
    # Handle edge cases
    if not nums or len(nums) < 2:
        return False
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If sum is odd, equal partition is impossible
    if total_sum % 2 != 0:
        return False
    
    # Target is half the total sum
    target = total_sum // 2
    
    # Create DP set to track achievable sums
    possible_subset_sums = {0}
    
    # Iterate through numbers to find achievable sums
    for num in nums:
        # Create a copy of current possible sums to avoid modifying during iteration
        current_sums = list(possible_subset_sums)
        
        for curr_sum in current_sums:
            new_sum = curr_sum + num
            
            # If new sum equals target, a valid partition exists
            if new_sum == target:
                return True
            
            # Add new sum to possible subset sums if it's less than target
            if new_sum < target:
                possible_subset_sums.add(new_sum)
    
    return False