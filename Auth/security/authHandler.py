from jose import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, status
from datetime import datetime , timedelta , timezone
import os 

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class AuthHandler(object):

    @staticmethod
    def sign_jwt(username : str , expires : timedelta | None = None) -> str:
        if expires: 
            expire = datetime.now(timezone.utc) + expires
        else :
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
        payload = {
            "username" : username,
            "expires" : str(expire)
        }

        encoded_jwt = jwt.encode(payload , SECRET_KEY ,algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_jwt(token : str) -> dict:
        credential_exception = HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers = {"WWW-Authenticate": "Bearer"}
        )
        try : 
            decoded_token  = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
            if decoded_token["expires"]>=datetime.now(timezone.utc) : 
                return decoded_token 
            else:
                 raise credential_exception
        except : 
            raise credential_exception

