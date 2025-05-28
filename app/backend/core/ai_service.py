# Import the uuid module to generate unique session IDs
import uuid

# Import the httpx library for making HTTP requests (not used directly here but likely used later for API calls)
import httpx

# Import the configuration class (not used directly here but likely used later for API keys, etc.)
from ..config import Config

# Define a service class to handle AI message processing logic
class AIService:
    # Define an async method to process incoming messages
    async def process_message(self, message: str, session_id: str | None) -> tuple[str, str]:
        """
        Process the user's message and return a reply along with a session ID.

        Parameters:
        - message: The input text from the user.
        - session_id: An optional session ID to track conversation context.

        Returns:
        - A tuple containing the AI-generated reply and the session ID.
        """

        # If no session_id was provided, generate a new unique one using UUID
        if not session_id:
            session_id = str(uuid.uuid4())
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.x.ai/v1/chat",  # Replace with actual endpoint
                headers={"Authorization": f"Bearer {Config.AI_API_KEY}"},
                json={"message": message, "session_id": session_id},
            )
            response.raise_for_status()
            # Retrieve the AI's reply from the response JSON
            reply = response.json().get("reply", "No response")
        return reply, session_id
    