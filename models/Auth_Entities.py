from pydantic import BaseModel 
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id : Optional[str] = None
    username : Optional[str] = None
    role : Optional[int] = None
    created_at : Optional[datetime] = None
    disabled : Optional[bool] = False

class Token(User):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : str 

class UserInDB(User):
    hashed_password : str

class UserInLogin(BaseModel):
    username : Optional[str] = None
    password : Optional[str] = None