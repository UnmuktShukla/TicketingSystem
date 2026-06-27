from pydantic import BaseModel 
from typing import Optional ,Any
from datetime import datetime


class User(BaseModel):
    id : Optional[Any] = None
    username : Optional[str] = None
    role : Optional[str] = None
    created_at : Optional[datetime] = None
    disabled : Optional[bool] = False

class Token(User):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    access_token : str 

class UserInDB(User):
    hashed_password : str

class UserInLogin(BaseModel):
    username : Optional[str] = None
    password : Optional[str] = None

class UserInSignup(BaseModel):
    username : str
    password : str