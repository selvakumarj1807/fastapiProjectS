from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    user_name: str
    user_email: EmailStr
    mobile_number: str
    password: str
