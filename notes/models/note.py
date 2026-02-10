from pydantic import BaseModel, Field
from datetime import datetime

class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str


class NoteOut(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime



class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None  = None


def build_note(data: dict):
    return {
        "title": data["title"],
        "content": data["content"],
        "created_at": datetime.utcnow()
    }


def serialize_note(doc):
    return {
        "id": str(doc["_id"]),
        "title": doc["title"],
        "content": doc["content"],
        "created_at": doc["created_at"]
    }
