
from fastapi import FastAPI

from app.routers.events import router as events_router


from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Intelligent Threat Detection Dashboard API",
    version=settings.APP_VERSION,
)

app.include_router(events_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to SentinelAI",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
