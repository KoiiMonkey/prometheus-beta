def switch_cases(str1, str2):
    """
    Takes two strings and returns a new string with swapped character cases.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: A new string where characters from str1 have their case swapped
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Check if inputs are strings
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # If input is empty, return empty string
    if not str1:
        return ""
    
    # Switch cases of characters
    switched_chars = []
    for char in str1:
        if char.isupper():
            switched_chars.append(char.lower())
        elif char.islower():
            switched_chars.append(char.upper())
        else:
            switched_chars.append(char)
    
    return ''.join(switched_chars)