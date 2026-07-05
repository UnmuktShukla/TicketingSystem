from datetime import datetime
from time import timezone
import uuid
from zoneinfo import ZoneInfo
from db.repository.userRepo import UserRepository
from models.Auth_Entities import (
    RefreshTokenRequest,
    TokenData,
    UserInLogin,
    UserInSignup,
    RefreshTokenResponse
)
from Auth.security.authHandler import AuthHandler
from Auth.security.hashHelper import HashHelper
from sqlalchemy.orm import Session
from fastapi import HTTPException
import secrets
import logging

logger = logging.getLogger(__name__)

class UserService:

    def __init__(self , session : Session):
        self.__userRepository = UserRepository(session= session)
    
    def signup(self , user_details : UserInSignup):
        if self.__userRepository.user_exist_by_username(user_details.username):
            raise HTTPException(status_code=400 , detail = "Please Login")
        
        hashed_password = HashHelper.get_password_hash(plain_pw=user_details.password)
        user_details.password = hashed_password
        return self.__userRepository.create_user(user_data= user_details)
    
    def login(self , login_details : UserInLogin):
        if not self.__userRepository.user_exist_by_username(login_details.username):
            raise HTTPException(status_code=400 , detail= " User Does not exist please Sign UP")
        
        user = self.__userRepository.get_user_by_username(login_details.username)
        if HashHelper.verify_password(plain_pw=login_details.password , hashed_pw=user.hashed_password):
            token = AuthHandler.sign_jwt(username=user.username)
            refresh_token =  str(secrets.token_urlsafe(32))
            hashed_refresh_token = AuthHandler.sign_refresh_token(refresh_token)
            self.__userRepository.create_refresh_token(hashed_refresh_token , user.id)
            if token and hashed_refresh_token: 
                return RefreshTokenResponse(
                    access_token= token,
                    refreshToken= refresh_token
                )
            raise HTTPException(status_code=500 , detail="Unable to process request")
        raise HTTPException(status_code=400 , detail="Please check your credentials")

    def logout(self , refresh_token : str):
        candidate_hash = AuthHandler.sign_refresh_token(refresh_token)
        stored_hash = self.__userRepository.get_refresh_token(candidate_hash)
        if stored_hash is None:
            raise HTTPException(status_code=401 , detail = "Unauthorised")
        self.__userRepository.revoke_refresh_token(stored_hash.id)
        return "Logged Out Successfully"

    def get_user_by_username(self , username : str):
        user = self.__userRepository.get_user_by_username(username=username)
        if user : 
            return user
        raise HTTPException(status_code=400 , detail="User Not Found")

    def refresh(self , refresh_token : str) -> TokenData:
        candidate_hash = AuthHandler.sign_refresh_token(refresh_token)
        stored_hash = self.__userRepository.get_refresh_token(candidate_hash)
        if stored_hash is None:
            raise HTTPException(status_code=401 , detail = "Unauthorised")
        now = datetime.now(ZoneInfo("Asia/Kolkata"))
        expires = stored_hash.expires

        if expires.tzinfo is None:
            expires = expires.replace(tzinfo=ZoneInfo("Asia/Kolkata"))
        
        try:
            if expires > now and not stored_hash.revoked:
                if AuthHandler.verify_refresh_token(candidate_hash , stored_hash.token):
                    user = self.__userRepository.get_user_by_id(stored_hash.user_id)
                    token = AuthHandler.sign_jwt(user.username)
                    return TokenData(
                        access_token= token
                    )
            else :
                raise HTTPException(status_code=401 , detail = "Unauthorised")
        except:
            raise HTTPException(status_code=401 , detail= "Session Expired")

