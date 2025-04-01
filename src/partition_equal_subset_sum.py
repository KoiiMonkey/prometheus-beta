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
    
    # Dynamic programming solution
    def find_partition(index, curr_sum, remaining_sum):
        # Base cases
        # If current sum matches half total, we found a valid partition
        if curr_sum == target:
            return True
        
        # If index out of bounds or current sum exceeds target, backtrack
        if index >= len(nums) or curr_sum > target:
            return False
        
        # Try including or excluding current number
        # Include current number
        if find_partition(index + 1, curr_sum + nums[index], remaining_sum - nums[index]):
            return True
        
        # Exclude current number
        if find_partition(index + 1, curr_sum, remaining_sum):
            return True
        
        return False
    
    return find_partition(0, 0, total_sum)