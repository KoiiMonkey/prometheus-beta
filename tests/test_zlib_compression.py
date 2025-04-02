import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_string():
    """Test compressing a simple string."""
    input_data = "Hello, world!"
    compressed = compress_data(input_data)
    assert isinstance(compressed, bytes)

def test_compress_bytes():
    """Test compressing bytes data."""
    input_data = b"Binary data to compress"
    compressed = compress_data(input_data)
    assert isinstance(compressed, bytes)

def test_decompress_data():
    """Test full compression and decompression cycle."""
    input_data = "Hello, world!"
    compressed = compress_data(input_data)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        compress_data(123)
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_compression_levels():
    """Test different compression levels."""
    input_data = "Test compression levels" * 100  # Larger data to see compression differences
    
    # Test all compression levels
    for level in range(10):
        compressed = compress_data(input_data, compression_level=level)
        decompressed = decompress_data(compressed)
        assert decompressed.decode('utf-8') == input_data

def test_invalid_compression_level():
    """Test error handling for invalid compression levels."""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)

def test_empty_data():
    """Test compressing and decompressing empty data."""
    empty_str = ""
    empty_bytes = b""
    
    for data in [empty_str, empty_bytes]:
        compressed = compress_data(data)
        decompressed = decompress_data(compressed)
        assert decompressed == data.encode('utf-8') if isinstance(data, str) else data

def test_large_data():
    """Test compressing and decompressing a large amount of data."""
    large_data = "Large test data " * 10000
    compressed = compress_data(large_data)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == large_data

def test_invalid_compressed_data():
    """Test decompression of invalid compressed data."""
    with pytest.raises(zlib.error):
        decompress_data(b"Invalid compressed data")