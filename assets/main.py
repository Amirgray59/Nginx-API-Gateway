from fastapi import FastAPI
from pydantic import BaseModel

from utils.router import router as asset_router
from core.errors import register_exception_handlers

from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

register_exception_handlers(app)

app.include_router(asset_router)

    

@app.get("/")
def root():
    return {"service": "assets"}

@app.get("/health")
def health():
    return {"status": "ok"}
