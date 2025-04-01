def can_partition(nums):
    """
    Determines if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    
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
    
    # Memoization to cache results
    memo = {}
    
    def can_find_subset(index, remaining):
        """
        Recursively find if a subset with the given remaining sum exists
        
        Args:
            index (int): Current index in the array
            remaining (int): Remaining sum to achieve
        
        Returns:
            bool: True if subset exists, False otherwise
        """
        # Base cases
        if remaining == 0:
            return True
        
        if index < 0 or remaining < 0:
            return False
        
        # Memoization key
        key = (index, remaining)
        
        # Check memoized results
        if key in memo:
            return memo[key]
        
        # Try two scenarios:
        # 1. Include current number
        include = can_find_subset(index - 1, remaining - nums[index])
        if include:
            memo[key] = True
            return True
        
        # 2. Exclude current number
        exclude = can_find_subset(index - 1, remaining)
        memo[key] = exclude
        return exclude
    
    # Start from the last index
    return can_find_subset(len(nums) - 1, target)