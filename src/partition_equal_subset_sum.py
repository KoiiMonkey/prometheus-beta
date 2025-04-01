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
    
    # Memoization dictionary to speed up recursion
    memo = {}
    
    def dfs(index, current_sum):
        """
        Depth-first search to find if subset sum can reach target
        
        Args:
            index (int): Current index in the array
            current_sum (int): Current running sum
        
        Returns:
            bool: True if subset can be formed to reach target
        """
        # If we've reached the target, it's a valid partition
        if current_sum == target:
            return True
        
        # If we've gone too far or sum is too large, it's invalid
        if index >= len(nums) or current_sum > target:
            return False
        
        # Check memoized results to avoid redundant computations
        key = (index, current_sum)
        if key in memo:
            return memo[key]
        
        # Try including or excluding current number
        # Include current number
        include = dfs(index + 1, current_sum + nums[index])
        if include:
            memo[key] = True
            return True
        
        # Exclude current number
        exclude = dfs(index + 1, current_sum)
        memo[key] = exclude
        return exclude
    
    return dfs(0, 0)