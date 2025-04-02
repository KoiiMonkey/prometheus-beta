import os
import pytest
import tempfile
import shutil

from src.directory_checker import directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert directory_exists(temp_dir) is True

def test_non_existing_directory():
    """Test that a non-existing directory returns False."""
    # Create a path that's very unlikely to exist
    non_existing_path = "/tmp/this_directory_should_not_exist_23475982"
    assert directory_exists(non_existing_path) is False

def test_file_path_returns_false():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert directory_exists(temp_file.name) is False

def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        directory_exists(123)
    
    with pytest.raises(TypeError):
        directory_exists(None)

def test_empty_string_path():
    """Test that an empty string path returns False."""
    assert directory_exists("") is False

def test_relative_path():
    """Test checking a relative path."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a subdirectory in the temp directory
        sub_dir = os.path.join(temp_dir, "subdir")
        os.makedirs(sub_dir)
        
        # Change current working directory
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            assert directory_exists("subdir") is True
        finally:
            # Restore original working directory
            os.chdir(original_cwd)