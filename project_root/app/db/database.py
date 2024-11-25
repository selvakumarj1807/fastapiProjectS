from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client['notes_app']
users_collection = db['users']
notes_collection = db['notes']
