from fastapi import FastAPI
from api.router import router
from db.postgres import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}
