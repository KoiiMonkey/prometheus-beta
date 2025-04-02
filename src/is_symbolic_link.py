import os

def is_symbolic_link(file_path):
    """
    Detect whether a given file path is a symbolic link.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a symbolic link, False otherwise.

    Raises:
        TypeError: If the input is not a string.
        FileNotFoundError: If the file path does not exist.
    """
    # Validate input type
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string representing a file path")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file or directory found at path: {file_path}")

    # Use os.path.islink to check if the path is a symbolic link
    return os.path.islink(file_path)