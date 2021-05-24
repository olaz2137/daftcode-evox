from fastapi import FastAPI

from .views import router as text_api_router

app = FastAPI()

app.include_router(text_api_router, tags=["text"])
