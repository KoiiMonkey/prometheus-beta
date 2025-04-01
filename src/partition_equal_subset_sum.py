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
    
    def find_subset_sum(index, curr_sum):
        """
        Find if a subset sum can be created starting from given index
        
        Args:
            index (int): Current index in the array
            curr_sum (int): Current running sum
        
        Returns:
            bool: True if subset sum can be created, False otherwise
        """
        # If we've reached the target, it's a valid partition
        if curr_sum == target:
            return True
        
        # If we've gone too far or sum is excessive, return False
        if index >= len(nums) or curr_sum > target:
            return False
        
        # Create memoization key
        key = (index, curr_sum)
        
        # Check if result is memoized
        if key in memo:
            return memo[key]
        
        # Try two scenarios: include or exclude current number
        # 1. Include current number
        include = find_subset_sum(index + 1, curr_sum + nums[index])
        if include:
            memo[key] = True
            return True
        
        # 2. Exclude current number
        exclude = find_subset_sum(index + 1, curr_sum)
        memo[key] = exclude
        return exclude
    
    return find_subset_sum(0, 0)