def find_median(numbers):
    """
    Find the median of a list of numbers.

    Args:
        numbers (list): A list of numbers (int or float)

    Returns:
        float: The median value of the input list

    Raises:
        TypeError: If the input is not a list
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate median
    if n % 2 == 0:
        # Even number of elements: average of two middle values
        mid_right = n // 2
        mid_left = mid_right - 1
        return (sorted_numbers[mid_left] + sorted_numbers[mid_right]) / 2
    else:
        # Odd number of elements: middle value
        return sorted_numbers[n // 2]