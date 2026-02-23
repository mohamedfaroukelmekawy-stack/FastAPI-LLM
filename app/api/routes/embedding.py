
from fastapi import APIRouter
from app.schemas.embedding import EmbeddingRequest, EmbeddingResponse
from app.services.embedding_service import generate_embedding

# ✅ لازم الاسم يكون router
router = APIRouter(
    prefix="/embedding",
    tags=["Embedding"]
)


@router.post("/", response_model=EmbeddingResponse)
async def create_embedding(data: EmbeddingRequest):
    vector = await generate_embedding(data.text)
    return {"embedding": vector}