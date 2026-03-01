from fastapi import APIRouter
from schemas.chat_schema import ChatRequest
from agents.orchestrator import process_message

router = APIRouter()

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    return process_message(request.message)