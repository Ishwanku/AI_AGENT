# Import the built-in logging module for application-wide logging
import logging

# Define a function to configure and return a logger instance
def setup_logger():
    # Configure the root logger with basic settings:
    # - level: INFO (logs info, warning, error, and critical messages)
    # - format: Specifies how log messages should appear
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    # Return a logger instance with the name of the current module
    return logging.getLogger(__name__)
