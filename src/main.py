from fastapi import FastAPI
from src.interfaces.api import router

app = FastAPI()
app.include_router(router)