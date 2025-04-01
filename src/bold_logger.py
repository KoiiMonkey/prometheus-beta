def log_bold(message):
    """
    Log a message in bold text using ANSI escape codes.
    
    Args:
        message (str): The message to be logged in bold.
    
    Returns:
        str: The bold-formatted message.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(message, str):
        raise TypeError("Input must be a string")
    
    # ANSI escape code for bold text
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    
    # Return the message wrapped in bold formatting
    return f"{BOLD_START}{message}{BOLD_END}"