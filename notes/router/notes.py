
from fastapi import APIRouter
from models.note import NoteCreate, build_note
from db.mongo import notes_collection

router = APIRouter()

@router.post("/")
def create_note(note: NoteCreate):

    doc = build_note(note.model_dump())

    result = notes_collection.insert_one(doc)

    return {"id": str(result.inserted_id)}
