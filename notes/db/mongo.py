
from pymongo import MongoClient
from core.config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)

db = client[DB_NAME]

notes_collection = db["notes"]
