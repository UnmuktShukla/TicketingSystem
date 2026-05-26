from fastapi import APIRouter , Depends
from models.Auth_Entities import (
    User,
    UserInDB,
    UserInLogin,
    Token,
    TokenData
)
from db.database import get_db
from sqlalchemy.orm import Session  
from service.UserService import UserService
from typing import Annotated

authRouter = APIRouter()

@authRouter.post("/login" , status_code=200 , response_model=Token)
def login(loginDetails : UserInLogin , session : Session = Depends(get_db)):
    try:
        return UserService(session=session).login(login_details= loginDetails)
    except Exception as error : 
        print(error)
        raise error

@authRouter.post("/signup" , status_code=201 , response_model=User)
def signup(signUpDetails : UserInDB , session : Session = Depends(get_db)):
    try : 
        return UserService(session=session).signup(user_details=signUpDetails)
    except Exception as error : 
        print(error)
        raise error


