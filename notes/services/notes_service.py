from db.mongo import notes_collection
from models.note import build_note, serialize_note
from bson import ObjectId
from fastapi import HTTPException


def create_note_service(note_data: dict):

    doc = build_note(note_data)

    result = notes_collection.insert_one(doc)

    return str(result.inserted_id)


def list_notes_service(limit: int, skip: int):

    cursor = (
        notes_collection
        .find()
        .sort("created_at", -1)
        .skip(skip)
        .limit(limit)
    )

    return [serialize_note(doc) for doc in cursor]


def validate_object_id(id: str):

    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid id")

    return ObjectId(id)


def update_note_service(note_id: str, update_data: dict):

    oid = validate_object_id(note_id)

    update_fields = {k: v for k, v in update_data.items() if v is not None}

    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    result = notes_collection.find_one_and_update(
        {"_id": oid},
        {"$set": update_fields},
        return_document=True
    )

    if not result:
        raise HTTPException(status_code=404, detail="Note not found")

    return serialize_note(result)

def delete_note_service(note_id: str):

    oid = validate_object_id(note_id)

    result = notes_collection.delete_one({"_id": oid})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"status": "deleted"}

