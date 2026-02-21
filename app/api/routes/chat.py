from fastapi import APIRouter, Depends
from app.core.security import get_current_user_id
from app.services.chat_service import ChatService
from app.schemas.schemas import ChatRequest, ChatResponse, ChatMessageResponse
from fastapi import UploadFile, File
from app.services.file_service import FileService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(data: ChatRequest, user_id: str = Depends(get_current_user_id)):
    """Send a message to the LLM"""
    return ChatService().chat(user_id, data.message)


@router.get("/history", response_model=list[ChatMessageResponse])
def get_history(user_id: str = Depends(get_current_user_id)):
    """Get your chat history"""
    return ChatService().get_history(user_id)


@router.delete("/history")
def clear_history(user_id: str = Depends(get_current_user_id)):
    """Clear your chat history"""
    return ChatService().clear_history(user_id)
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user_id),
):
    content = await FileService().extract_content(file)

    # send extracted content to chat service
    return ChatService().chat(
        user_id,
        f"Analyze this file content:\n{content[:4000]}"
    )
