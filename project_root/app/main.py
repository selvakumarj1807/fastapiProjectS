from fastapi import FastAPI
from app.api.routes import user_routes, note_routes

app = FastAPI()

# Include routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(note_routes.router, prefix="/notes", tags=["Notes"])
