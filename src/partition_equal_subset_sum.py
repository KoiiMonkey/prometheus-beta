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
    
    # Special case for uniformly equal numbers
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    def check_partition():
        # For every unique configuration, check if it's an exact partition
        def backtrack(index, subset_sum, used_nums):
            # Reached target exactly
            if subset_sum == target:
                return True
            
            # Gone too far
            if index >= len(nums) or subset_sum > target:
                return False
            
            # Try including current number with tracking
            # Ensure we're not using the same instance of a number multiple times
            current_num = nums[index]
            remaining_count = counts[current_num] - used_nums.get(current_num, 0)
            
            # Include the number
            if remaining_count > 0:
                used_nums[current_num] = used_nums.get(current_num, 0) + 1
                if backtrack(index + 1, subset_sum + current_num, used_nums):
                    return True
                used_nums[current_num] -= 1  # backtrack
            
            # Exclude the number
            if backtrack(index + 1, subset_sum, used_nums):
                return True
            
            return False
        
        return backtrack(0, 0, {})
    
    return check_partition()