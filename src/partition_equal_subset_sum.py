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
    
    # Count of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    def find_partition(available, current_sum, target_sum, depth=0):
        """
        Recursive function to find partition
        
        Args:
            available (dict): Available numbers and their counts
            current_sum (int): Current sum of subset
            target_sum (int): Target sum to achieve
            depth (int): Recursion depth to prevent infinite recursion
        
        Returns:
            bool: True if partition possible, False otherwise
        """
        # If we've reached the target, we found a valid partition
        if current_sum == target_sum:
            return True
        
        # Gone too far or too deep in recursion
        if current_sum > target_sum or depth > len(nums):
            return False
        
        # Try each available number
        for num, count in list(available.items()):
            if count > 0 and current_sum + num <= target_sum:
                # Use this number
                available[num] -= 1
                if available[num] == 0:
                    del available[num]
                
                # Recursive call
                if find_partition(available.copy(), current_sum + num, target_sum, depth + 1):
                    return True
                
                # Restore number for backtracking
                available[num] = available.get(num, 0) + 1
        
        return False
    
    return find_partition(counts.copy(), 0, target)