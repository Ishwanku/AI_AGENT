# Import Blueprint to organize routes, and request to access HTTP request data
from quart import Blueprint, request

# Import Pydantic's ValidationError to handle bad input formats
from pydantic import ValidationError

# Import request/response models defined in models.py
from .models import ChatRequest, ChatResponse

# Import the AI service that processes chat messages
from ..core.ai_service import AIService

# Create a Blueprint for chat-related API routes
chat_bp = Blueprint("chat", __name__)

# Define an asynchronous POST route for handling chat requests
@chat_bp.route("/chat", methods=["POST"])
async def chat():
    try:
        # Parse the incoming JSON request body
        data = await request.get_json()
        
        # Validate and convert the data to a ChatRequest Pydantic model
        chat_request = ChatRequest(**data)
        
        # Create an instance of the AIService to process the chat message
        ai_service = AIService()
        
        # Process the user's message and get the reply and session ID
        reply, session_id = await ai_service.process_message(
            chat_request.message, chat_request.session_id
        )
        
        # Return a structured ChatResponse as a dictionary (JSON-compatible)
        return ChatResponse(reply=reply, session_id=session_id).dict()
    
    # If the input data is invalid or missing required fields, return a 400 error
    except ValidationError as e:
        return {"error": str(e)}, 400
    
    # Catch any unexpected server-side errors and return a 500 error
    except Exception as e:
        return {"error": str(e)}, 500
