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
    # Check for invalid input or edge cases
    if not nums or len(nums) < 2:
        return False
    
    # Calculate total sum
    total_sum = sum(nums)
    
    # If total sum is odd, we can't partition equally
    if total_sum % 2 != 0:
        return False
    
    # Target is half the total sum
    target = total_sum // 2
    
    # If any single number is greater than target, it can't be partitioned
    if max(nums) > target:
        return False
    
    # DP table to track possible subset sums
    dp = [False] * (target + 1)
    dp[0] = True
    
    # Iterate through each number in the input
    for num in nums:
        # Work backwards to avoid using same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target]