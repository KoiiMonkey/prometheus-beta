def to_kebab_case(input_string):
    """
    Convert a given string to kebab-case.
    
    Kebab case is a string formatting style where words are 
    lowercase and separated by hyphens.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to kebab-case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("snake_case_string")
        'snake-case-string'
        >>> to_kebab_case("camelCaseString")
        'camel-case-string'
        >>> to_kebab_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to lowercase
    # Replace underscores, spaces, and camel case transitions with hyphens
    result = []
    for i, char in enumerate(input_string):
        # Add first character (always lowercase)
        if i == 0:
            result.append(char.lower())
            continue
        
        # Replace spaces, underscores with hyphens
        if char in [' ', '_']:
            result.append('-')
            continue
        
        # Handle camel case: insert hyphen before uppercase letters
        if char.isupper():
            result.append('-')
            result.append(char.lower())
            continue
        
        # Regular characters
        result.append(char.lower())
    
    return ''.join(result)