from datetime import datetime, timedelta , timezone
from typing import Annotated
import jwt
from fastapi import Depends , FastAPI , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from models.Auth_Entities import (
    User,
    UserInDB,
    Token,
    TokenData
)

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "token")

@app.get("/index")
async def get_index(token : Annotated[str , Depends(oauth2_scheme)]):
    return {"token" : token}