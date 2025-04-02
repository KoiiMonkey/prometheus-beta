import readline
import logging
from typing import Optional, Callable

def log_interactive_prompt(
    prompt: str, 
    log_level: int = logging.INFO, 
    logger: Optional[logging.Logger] = None,
    validator: Optional[Callable[[str], bool]] = None
) -> str:
    """
    Logs an interactive prompt and captures user input with optional validation.

    Args:
        prompt (str): The prompt text to display to the user.
        log_level (int, optional): Logging level for the prompt. Defaults to logging.INFO.
        logger (logging.Logger, optional): Logger to use. Creates a default logger if None.
        validator (Callable[[str], bool], optional): Function to validate user input.

    Returns:
        str: The user's input after optional validation.

    Raises:
        ValueError: If input fails validation and no valid input is provided.
    """
    # Create a default logger if none provided
    if logger is None:
        logger = logging.getLogger(__name__)
        # If no handlers, add a basic console handler
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(levelname)s: %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

    # Log the prompt
    logger.log(log_level, prompt)

    while True:
        try:
            # Get user input
            user_input = input(prompt)

            # Validate input if a validator is provided
            if validator is None or validator(user_input):
                # Log the input
                logger.log(log_level, f"User input: {user_input}")
                return user_input
            
            # If validation fails, log and prompt again
            logger.warning("Invalid input. Please try again.")

        except (KeyboardInterrupt, EOFError):
            # Handle interrupts gracefully
            logger.error("Input interrupted.")
            raise