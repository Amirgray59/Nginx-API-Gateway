
from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str



from datetime import datetime

def build_note(data: dict):

    return {
        "title": data["title"],
        "content": data["content"],
        "created_at": datetime.utcnow()
    }



