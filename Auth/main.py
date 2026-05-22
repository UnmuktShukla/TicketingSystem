from datetime import datetime, timedelta , timezone
from typing import Annotated

import jwt
from fastapi import Depends , FastAPI , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

from models.Auth_Entities import (
    User,
    UserInDB,
    Token,
    TokenData
)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "token")

@app.get("/index")
async def get_index(token : Annotated[str , Depends(oauth2_scheme)]):
    return {"token" : token}