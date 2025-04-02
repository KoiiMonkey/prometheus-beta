from typing import List

def max_increasing_subsequence_sum(nums: List[int]) -> int:
    """
    Calculate the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns 0
    - Single element array returns that element
    """
    if not nums:
        return 0
    
    # Store the maximum sum at each "pile" in patience sorting
    pile_sums = []
    
    for num in nums:
        # Find the correct insertion point
        left, right = 0, len(pile_sums)
        
        while left < right:
            mid = (left + right) // 2
            if pile_sums[mid] <= num:
                left = mid + 1
            else:
                right = mid
        
        # If we've reached the end, append a new pile
        if left == len(pile_sums):
            pile_sums.append(num)
        else:
            # Update the pile sum maintaining increasing subsequence property
            pile_sums[left] = max(pile_sums[left], num)
    
    # Return the maximum sum (last pile)
    return max(pile_sums) if pile_sums else 0