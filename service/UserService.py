import stat
from db.repository.userRepo import UserRepository
from models.Auth_Entities import (
    User,
    UserInDB,
    UserInLogin,
    Token,
    TokenData
)
from Auth.security.authHandler import AuthHandler
from Auth.security.hashHelper import HashHelper
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class UserService:

    def __init__(self , session : Session):
        self.__userRepository = UserRepository(session= session)
    
    def signup(self , user_details : UserInDB):
        if self.__userRepository.user_exist_by_username(user_details.username):
            raise HTTPException(status_code=400 , detail = "Please Login")
        
        hashed_password = HashHelper.get_password_hash(plain_pw=user_details.hashed_password)
        user_details.hashed_password = hashed_password
        return self.__userRepository.create_user(user_data= user_details)
    
    def login(self , login_details : UserInLogin):
        if not self.__userRepository.user_exist_by_username(login_details.username):
            raise HTTPException(status_code=400 , detail= " User Does not exist please Sign UP")
        
        user = self.__userRepository.get_user_by_username(login_details.username)
        if HashHelper.verify_password(plain_pw=login_details.password , hashed_pw=user.hashed_password):
            token = AuthHandler.sign_jwt(username=user.username)
            if token : 
                return TokenData(
                    access_token= token,
                )
            raise HTTPException(status_code=500 , detail="Unable to process request")
        raise HTTPException(status_code=400 , detail="Please check your credentials")

    def get_user_by_username(self , username : str):
        user = self.__userRepository.get_user_by_username(username=username)
        if user : 
            return user
        raise HTTPException(status_code=400 , detail="User Not Found")