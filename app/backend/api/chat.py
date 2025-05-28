from quart import Blueprint, request, jsonify
from pydantic import BaseModel
from ..core.ai_service import AIService

chat_bp = Blueprint("chat", __name__)
ai_service = AIService()

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None

@chat_bp.route("/chat", methods=["POST"])
async def chat():
    data = await request.get_json()
    chat_request = ChatRequest(**data)
    reply, session_id = await ai_service.process_message(
        chat_request.message, chat_request.session_id
    )
    return jsonify({"reply": reply, "session_id": session_id})