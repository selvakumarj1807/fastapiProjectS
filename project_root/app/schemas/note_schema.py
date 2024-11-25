from pydantic import BaseModel

class NoteModel(BaseModel):
    note_title: str
    note_content: str
