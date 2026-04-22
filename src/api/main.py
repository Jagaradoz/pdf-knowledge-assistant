from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import query
from src.core.config import settings
from src.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    description="API for the PDF Knowledge Assistant RAG System",
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
app.include_router(query.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "app_name": settings.APP_NAME}

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME}...")
