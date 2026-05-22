from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id : Optional[str] = None
    email : Optional[str] = None
    password : Optional[str] = None
    role : Optional[str] = None
    created_at : Optional[datetime] = None
    disabled : Optional[bool] = False

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : str 

class UserInDB(BaseModel):
    hashed_password : str