def string_transform(s: str) -> str:
    """
    Transform the input string by:
    1. Removing all spaces
    2. Converting all uppercase letters to lowercase
    3. Reversing the order of characters
    4. Replacing all occurrences of 'a' with '*'

    Args:
        s (str): The input string to transform

    Returns:
        str: The transformed string

    Examples:
        >>> string_transform("Hello World")
        'dlrow*h*o'
        >>> string_transform("Python Programming")
        'gnimm*rg*p*nht*yp'
    """
    # Remove spaces
    no_space_str = s.replace(" ", "")
    
    # Convert to lowercase
    lowercase_str = no_space_str.lower()
    
    # Reverse the string
    reversed_str = lowercase_str[::-1]
    
    # Replace 'a' with '*'
    transformed_str = reversed_str.replace('a', '*')
    
    return transformed_str