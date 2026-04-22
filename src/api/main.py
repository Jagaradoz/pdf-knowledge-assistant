from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import query, system
from src.core.config import settings
from src.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    description="PDF Knowledge Assistant (Basic RAG Implementation)",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(query.router, prefix="/api")
app.include_router(system.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME}...")
