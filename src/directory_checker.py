import os

def directory_exists(path):
    """
    Check if a directory exists at the specified path.

    Args:
        path (str): The path to the directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.

    Raises:
        TypeError: If the path is not a string.
    """
    # Check if the input is a string
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    # Use os.path.isdir to check if path is an existing directory
    return os.path.isdir(path)