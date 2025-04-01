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
    
    # Dynamic programming approach
    # Create DP table to track possible sums
    dp = [False] * (target + 1)
    dp[0] = True
    
    # Track subset of unique numbers
    nums_set = set(nums)
    
    # Iterate through unique numbers
    for num in nums_set:
        # Iterate backwards to prevent multiple uses of the same number
        for j in range(target, num - 1, -1):
            # Update DP table
            dp[j] |= dp[j - num]
    
    return dp[target]