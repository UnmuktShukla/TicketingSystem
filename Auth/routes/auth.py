from fastapi import APIRouter , Depends
from models.Auth_Entities import (
    RefreshTokenRequest,
    User,
    UserInLogin,
    RefreshTokenResponse,
    TokenData,
    UserInSignup
)
from db.database import get_db
from sqlalchemy.orm import Session, session  
from service.UserService import UserService
from typing import Annotated

authRouter = APIRouter()

@authRouter.post("/login" , status_code=200 , response_model=RefreshTokenResponse)
def login(loginDetails : UserInLogin , session : Session = Depends(get_db)):
    try:
        return UserService(session=session).login(login_details= loginDetails)
    except Exception as error : 
        print(error)
        raise error

@authRouter.post("/signup" , status_code=201 , response_model=User)
def signup(signUpDetails : UserInSignup , session : Session = Depends(get_db)):
    try : 
        return UserService(session=session).signup(user_details=signUpDetails)
    except Exception as error : 
        print(error)
        raise error

@authRouter.post("/refresh" , status_code=200 , response_model=TokenData)
def refresh(refreshToken : RefreshTokenRequest , session : Session = Depends(get_db)):
    try : 
        return UserService(session=session).refresh(refreshToken.refreshToken)
    except Exception as error:
        print(error)
        raise error

@authRouter.post("/logout" , status_code = 201 )
def logout(refresh_token : RefreshTokenRequest , session : Session = Depends(get_db)):
    try : 
        return UserService(session=session).logout(refresh_token.refreshToken)
    except Exception as error:
        print(error)
        raise error

