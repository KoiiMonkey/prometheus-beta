import zlib
from typing import Union, Optional

def compress_data(data: Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using Zlib compression algorithm.

    Args:
        data (Union[str, bytes]): The data to be compressed. 
                                  Can be a string or bytes object.
        compression_level (int, optional): Compression level from 0 to 9. 
                                           Defaults to 6 (default zlib compression).
                                           0 = no compression, 9 = maximum compression.

    Returns:
        bytes: Compressed data as a bytes object.

    Raises:
        TypeError: If input data is not a string or bytes object.
        ValueError: If compression level is not between 0 and 9.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be a string or bytes object")

    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Compress the data
    try:
        compressed_data = zlib.compress(data, compression_level)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zlib compressed data.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not a bytes object.
        zlib.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be a bytes object")

    # Decompress the data
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")