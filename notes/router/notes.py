from fastapi import APIRouter, Query
from models.note import NoteCreate, NoteUpdate
from services.notes_service import (
    create_note_service,
    list_notes_service,
    update_note_service,
    delete_note_service
)

router = APIRouter()


@router.post("/")
def create_note(note: NoteCreate):

    note_id = create_note_service(note.model_dump())

    return {"id": note_id}


@router.get("/")
def list_notes(
    limit: int = Query(10, le=100),
    skip: int = 0
):

    return list_notes_service(limit, skip)


@router.patch("/{note_id}")
def update_note(note_id: str, data: NoteUpdate):

    return update_note_service(
        note_id,
        data.model_dump(exclude_unset=True)
    )


@router.delete("/{note_id}")
def delete_note(note_id: str):

    return delete_note_service(note_id)


