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
    
    # Special case for single words (lowercase or uppercase)
    if input_string.isalpha() and len(set(input_string)) == 1:
        return input_string.lower()
    
    # Convert to lowercase and normalize separators
    normalized = []
    for i, char in enumerate(input_string):
        # First character is always added (converted to lowercase)
        if i == 0:
            normalized.append(char.lower())
            continue
        
        # Handle uppercase and special characters
        if char.isupper():
            # Add hyphen before uppercase letter (if not already at start)
            if not normalized or normalized[-1] == '-':
                normalized.append(char.lower())
            else:
                # Only add hyphen if previous char was not a hyphen
                if normalized[-1] != '-':
                    normalized.append('-')
                normalized.append(char.lower())
        elif char in [' ', '_', '-']:
            # Normalize all separators to hyphens
            if normalized and normalized[-1] != '-':
                normalized.append('-')
        else:
            # Regular lowercase characters
            normalized.append(char.lower())
    
    return ''.join(normalized)