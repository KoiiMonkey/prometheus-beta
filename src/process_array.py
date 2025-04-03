def process_array(numbers):
    """
    Process an array of numbers by multiplying every third number by 2 
    and then finding the sum of all even numbers, excluding the modified numbers.
    
    Args:
        numbers (list): A list of numbers to process
    
    Returns:
        float/int: Sum of even numbers, excluding modified numbers
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    
    # Create a copy of the original list to avoid modifying the input
    processed_numbers = numbers.copy()
    
    # Multiply every third number by 2 (starting from index 2, which is the 3rd number)
    for i in range(2, len(processed_numbers), 3):
        processed_numbers[i] *= 2
    
    # Sum even numbers, excluding the modified numbers
    even_sum = sum(num for i, num in enumerate(numbers) 
                   if (isinstance(num, int) and num % 2 == 0 or 
                       isinstance(num, float) and num % 2 == 0.0) and 
                   i % 3 != 2)
    
    return even_sum