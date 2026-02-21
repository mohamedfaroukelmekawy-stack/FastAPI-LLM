from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import auth, chat

app = FastAPI(
    title="FastAPI LLM API",
    version="1.0.0",
    description="FastAPI + Cohere LLM + JWT Auth + Supabase",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/api")
app.include_router(chat.router, prefix="/api")


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "app": "FastAPI LLM API"}


@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}
