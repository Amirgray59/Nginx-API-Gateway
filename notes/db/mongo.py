
from pymongo import MongoClient
from core.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)

db = client[DB_NAME]



notes_collection = db["notes"]


def init_indexes():
    notes_collection.create_index(
        [("created_at", -1)],
        background=True
    )

init_indexes()
