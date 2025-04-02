import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.interactive_prompt_logger import log_interactive_prompt

def test_basic_prompt_logging():
    """Test basic logging of an interactive prompt."""
    with patch('builtins.input', return_value='test answer'):
        # Capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Call the function
        result = log_interactive_prompt("Enter something: ", logger=logger)

        # Check results
        log_output = log_capture.getvalue()
        assert 'Enter something: ' in log_output
        assert 'User input: test answer' in log_output
        assert result == 'test answer'

def test_input_validation():
    """Test input validation with a custom validator."""
    def validate_length(s):
        return len(s) >= 3

    # Simulate multiple inputs with first two being invalid
    inputs = iter(['ab', 'no', 'valid input'])
    with patch('builtins.input', lambda _: next(inputs)):
        # Capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Call the function with validator
        result = log_interactive_prompt(
            "Enter input (min 3 chars): ", 
            validator=validate_length, 
            logger=logger
        )

        # Check results
        log_output = log_capture.getvalue()
        assert result == 'valid input'
        assert log_output.count('Invalid input. Please try again.') == 2

def test_custom_log_level():
    """Test using a custom log level."""
    with patch('builtins.input', return_value='test'):
        # Capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        # Call with custom log level
        result = log_interactive_prompt(
            "Enter something: ", 
            log_level=logging.DEBUG, 
            logger=logger
        )

        # Check results
        log_output = log_capture.getvalue()
        assert 'DEBUG' in log_output
        assert result == 'test'

def test_interrupt_handling():
    """Test handling of keyboard interrupt."""
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        # Capture log output
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger('test_logger')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Expect an exception
        with pytest.raises(KeyboardInterrupt):
            log_interactive_prompt("Enter something: ", logger=logger)

        # Check error logged
        log_output = log_capture.getvalue()
        assert 'Input interrupted.' in log_output