from jose import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, status
from datetime import datetime , timedelta , timezone
import os 
import secrets
import hmac
import hashlib

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
            "exp" : expire
        }

        encoded_jwt = jwt.encode(payload , SECRET_KEY ,algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_jwt(token : str) -> dict:
        credential_exception = HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try : 
            decoded_token  = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
            return decoded_token
        except : 
            raise credential_exception

    @staticmethod
    def sign_refresh_token( token : str ) -> str:
        token_hash = hmac.new(
            SECRET_KEY.encode(),
            token.encode(),
            hashlib.sha256
        ).hexdigest()
        return token_hash

    @staticmethod
    def verify_refresh_token(candidate_hash: str , stored_hash : str) -> bool:
        credential_exception = HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            return hmac.compare_digest(candidate_hash, stored_hash)
        except :
            raise credential_exception
