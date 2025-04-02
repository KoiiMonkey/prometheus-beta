import os
import pytest
import tempfile
import shutil

from src.is_symbolic_link import is_symbolic_link

def test_is_symbolic_link_true():
    """Test that is_symbolic_link correctly identifies a symbolic link."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        original_file = os.path.join(tmpdir, 'original.txt')
        with open(original_file, 'w') as f:
            f.write('Test content')

        # Create a symbolic link
        symlink_path = os.path.join(tmpdir, 'symlink.txt')
        os.symlink(original_file, symlink_path)

        assert is_symbolic_link(symlink_path) is True

def test_is_symbolic_link_false_regular_file():
    """Test that is_symbolic_link returns False for a regular file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        file_path = os.path.join(tmpdir, 'regular.txt')
        with open(file_path, 'w') as f:
            f.write('Test content')

        assert is_symbolic_link(file_path) is False

def test_is_symbolic_link_false_directory():
    """Test that is_symbolic_link returns False for a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert is_symbolic_link(tmpdir) is False

def test_is_symbolic_link_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        is_symbolic_link(123)
        is_symbolic_link(None)

def test_is_symbolic_link_file_not_found():
    """Test that FileNotFoundError is raised for non-existent path."""
    with pytest.raises(FileNotFoundError, match="No file or directory found"):
        is_symbolic_link('/path/to/nonexistent/file')