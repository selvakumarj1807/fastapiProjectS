from app.db.database import users_collection
from app.core.security import create_access_token
from passlib.hash import bcrypt

async def register_user(user):
    existing_user = await users_collection.find_one({"user_email": user.user_email})
    if existing_user:
        return {"error": "User already exists"}
    user.password = bcrypt.hash(user.password)
    await users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

async def login_user(email: str, password: str):
    user = await users_collection.find_one({"user_email": email})
    if not user or not bcrypt.verify(password, user['password']):
        return {"error": "Invalid credentials"}
    access_token = create_access_token({"user_id": user['user_id']})
    return {"access_token": access_token}
from app.db.database import notes_collection

async def create_note(note):
    await notes_collection.insert_one(note.dict())
    return {"message": "Note created"}

async def get_notes(user_id):
    return await notes_collection.find({"user_id": user_id}).to_list(100)
