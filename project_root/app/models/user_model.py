from datetime import datetime
from uuid import uuid4

def user_document():
    return {
        "user_id": str(uuid4()),
        "user_name": "",
        "user_email": "",
        "mobile_number": "",
        "password": "",
        "last_update": datetime.utcnow(),
        "created_on": datetime.utcnow(),
    }
def note_document():
    return {
        "note_id": str(uuid4()),
        "user_id": "",
        "note_title": "",
        "note_content": "",
        "last_update": datetime.utcnow(),
        "created_on": datetime.utcnow(),
    }
