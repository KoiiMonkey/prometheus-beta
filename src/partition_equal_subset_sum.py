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
    def solve_subset_partition(arr):
        """
        Solve subset partition problem with optimization
        
        Args:
            arr (list): Input array to partition
        
        Returns:
            bool: True if valid partition exists, False otherwise
        """
        # Create DP table
        dp = [[False] * (target + 1) for _ in range(len(arr) + 1)]
        
        # Initialize first column (empty subset is always possible)
        for i in range(len(arr) + 1):
            dp[i][0] = True
        
        # Build DP table
        for i in range(1, len(arr) + 1):
            for j in range(1, target + 1):
                # If current number is less than current subset target
                if arr[i-1] <= j:
                    # Include or exclude current number
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    # Copy previous row's decision
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(arr)][target]
    
    return solve_subset_partition(nums)