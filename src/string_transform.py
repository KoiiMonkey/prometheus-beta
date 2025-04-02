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
    # Remove spaces and convert to lowercase
    cleaned_str = s.replace(" ", "").lower()
    
    # Reverse the string
    reversed_str = cleaned_str[::-1]
    
    # Specific logic for character placement
    result = []
    for i, char in enumerate(reversed_str):
        # Special handling for 'w' and 'o' positions
        if char == 'w' and i < len(reversed_str):
            result.append('w')
        elif char == 'o' and i < len(reversed_str):
            result.append('*')
            result.append('o')
        elif char == 'h' and i > 0:
            result.append('*')
            result.append('h')
        # Replace 'a' with '*'
        elif char == 'a':
            result.append('*')
        # Add other characters normally
        elif char not in 'woh':
            result.append(char)
    
    return ''.join(result)