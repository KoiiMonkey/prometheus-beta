import pytest
from src.string_converter import to_kebab_case

def test_basic_conversion():
    """Test basic string conversion to kebab case."""
    assert to_kebab_case("Hello World") == "hello-world"
    assert to_kebab_case("hello world") == "hello-world"

def test_snake_case_conversion():
    """Test conversion from snake case to kebab case."""
    assert to_kebab_case("hello_world") == "hello-world"
    assert to_kebab_case("snake_case_string") == "snake-case-string"

def test_camel_case_conversion():
    """Test conversion from camel case to kebab case."""
    assert to_kebab_case("helloWorld") == "hello-world"
    assert to_kebab_case("camelCaseString") == "camel-case-string"

def test_mixed_case_conversion():
    """Test conversion with mixed casing and separators."""
    assert to_kebab_case("Hello_World") == "hello-world"
    assert to_kebab_case("Hello-World") == "hello-world"
    assert to_kebab_case("HelloWorld") == "hello-world"

def test_empty_string():
    """Test conversion of empty string."""
    assert to_kebab_case("") == ""

def test_single_word():
    """Test conversion of single word."""
    assert to_kebab_case("hello") == "hello"
    assert to_kebab_case("HELLO") == "hello"

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_kebab_case(None)
    
    with pytest.raises(TypeError):
        to_kebab_case(["hello"])