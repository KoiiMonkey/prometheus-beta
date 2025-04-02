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
    
    # Replace 'a' with '*'
    asterisk_str = lowercase_str.replace('a', '*')
    
    # Reverse the string
    transformed_str = asterisk_str[::-1]
    
    return transformed_str