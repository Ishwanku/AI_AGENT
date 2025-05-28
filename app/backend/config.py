# Import the function to load environment variables from a .env file
from dotenv import load_dotenv

# Import the os module to access environment variables
import os import environ

# Load environment variables from a .env file into the environment
load_dotenv()

# Define a configuration class to hold application settings
class Config:
    # Get the AI API key from the environment variable 'AI_API_KEY'.
    # If it's not set, default to 'your-api-key'.
    AI_API_KEY = environ.get("AI_API_KEY", "your-api-key")

    # Get the port number from the environment variable 'PORT'.
    # If not provided, default to 8000.
    # Convert the string value to an integer.
    PORT = int(environ.get("PORT", 8000))

    # Get the host address from the environment variable 'HOST'.
    # If not provided, default to '0.0.0.0' (listen on all network interfaces).
    HOST = environ.get("HOST", "0.0.0.0")
