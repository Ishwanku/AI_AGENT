# Import Quart, the async web framework
from quart import Quart

# Import the chat API blueprint
from .api.chat import chat_bp

# Import the logger setup function
from .core.logger import setup_logger

# Import app configuration (e.g., HOST, PORT)
from .config import Config

# Create an instance of the Quart application
app = Quart(__name__)

# Register the chat blueprint under the /api route prefix
# All routes inside chat_bp will be accessible under /api, e.g., /api/chat
app.register_blueprint(chat_bp, url_prefix="/api")

# Set up logging for the application
logger = setup_logger()

# Run the app only if this script is executed directly (not imported)
if __name__ == "__main__":
    # Import uvicorn (ASGI server) to run the Quart app
    import uvicorn

    # Start the app using settings from Config
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
