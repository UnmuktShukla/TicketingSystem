from typing import Annotated, Union
from fastapi import Depends, HTTPException, Header, status
from sqlalchemy.orm import Session

from Auth.security.authHandler import AuthHandler
from db.database import get_db
from models.Auth_Entities import User
from service.UserService import UserService

AUTH_PREFIX = "Bearer "

def getCurrentUser(
    session : Session = Depends(get_db),
    authorization : Annotated[Union[str, None] , Header()] = None
) -> User:
    auth_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Authorization Credential"
    )

    if not authorization:
        raise auth_exception
    
    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception

    payload = AuthHandler.decode_jwt(token=authorization[len(AUTH_PREFIX):])

    if payload and payload['username']:
        try:   
            user = UserService(session=session).get_user_by_username(payload['username'])
            return User(
                id = user.id,
                username=user.username,
                role = user.role,
                created_at= user.created_at
            )
        except Exception as error:
            raise error
    raise auth_exception
    
def requireAdmin(
    user : User = Depends(getCurrentUser)
):
    isAdminException = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN ,
        detail= "This user is not authorised to perform this operation"
    )
    if user.role != 'admin':
        raise isAdminException
    return user