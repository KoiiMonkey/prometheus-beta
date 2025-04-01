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
    
    def exact_subset_sum(remaining_nums, current_subset_sum):
        """
        Recursively find if an exact subset sum can be formed
        
        Args:
            remaining_nums (list): Remaining numbers to consider
            current_subset_sum (int): Current running subset sum
        
        Returns:
            bool: True if exact subset sum can be formed, False otherwise
        """
        # Reached the target exactly
        if current_subset_sum == target:
            return True
        
        # Exceeded the target
        if current_subset_sum > target or not remaining_nums:
            return False
        
        # Try including or excluding the current number
        # 1. Include current number
        if exact_subset_sum(remaining_nums[1:], current_subset_sum + remaining_nums[0]):
            return True
        
        # 2. Exclude current number
        if exact_subset_sum(remaining_nums[1:], current_subset_sum):
            return True
        
        return False
    
    # Use a sorted nums in descending order for faster pruning
    sorted_nums = sorted(nums, reverse=True)
    
    # Check multiple ways of partitioning
    attempts = 3  # Limit the number of attempts to prevent excessive recursion
    for _ in range(attempts):
        if exact_subset_sum(sorted_nums, 0):
            return True
        # Small shuffle to try different arrangements
        sorted_nums = sorted_nums[1:] + [sorted_nums[0]]
    
    return False