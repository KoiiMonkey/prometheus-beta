import os
import pytest
import shutil
import tempfile
from src.file_backup import create_file_backup

@pytest.fixture
def temp_file():
    """Create a temporary file for testing."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp:
        temp.write("Test content for backup")
        temp_path = temp.name
    yield temp_path
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)

@pytest.fixture
def temp_backup_dir():
    """Create a temporary directory for backups."""
    backup_dir = tempfile.mkdtemp()
    yield backup_dir
    # Cleanup
    shutil.rmtree(backup_dir)

def test_create_file_backup_default_location(temp_file):
    """Test creating a backup in the same directory as the source file."""
    backup_path = create_file_backup(temp_file)
    
    # Verify backup was created
    assert os.path.exists(backup_path)
    assert os.path.basename(backup_path).startswith(os.path.basename(temp_file))
    assert '_backup_' in os.path.basename(backup_path)

def test_create_file_backup_custom_location(temp_file, temp_backup_dir):
    """Test creating a backup in a specified directory."""
    backup_path = create_file_backup(temp_file, backup_dir=temp_backup_dir)
    
    # Verify backup was created in the specified directory
    assert os.path.exists(backup_path)
    assert os.path.dirname(backup_path) == temp_backup_dir
    assert os.path.basename(backup_path).startswith(os.path.basename(temp_file))

def test_backup_file_contents(temp_file):
    """Verify that backup file contents match the original."""
    with open(temp_file, 'r') as original:
        original_content = original.read()
    
    backup_path = create_file_backup(temp_file)
    
    with open(backup_path, 'r') as backup:
        backup_content = backup.read()
    
    assert original_content == backup_content

def test_backup_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent files."""
    with pytest.raises(FileNotFoundError):
        create_file_backup('/path/to/nonexistent/file.txt')

def test_backup_directory():
    """Test that IsADirectoryError is raised when trying to backup a directory."""
    with pytest.raises(IsADirectoryError):
        create_file_backup(os.path.dirname(__file__))

def test_multiple_backups(temp_file):
    """Test that multiple backups can be created with different timestamps."""
    backup1 = create_file_backup(temp_file)
    backup2 = create_file_backup(temp_file)
    
    assert backup1 != backup2
    assert os.path.exists(backup1)
    assert os.path.exists(backup2)