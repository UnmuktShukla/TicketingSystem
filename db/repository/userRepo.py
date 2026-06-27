import datetime
from zoneinfo import ZoneInfo
from .base import BaseRepository
from models.Auth_Entities import (
    UserInDB,
    User,
    UserInSignup
)
from models.models import Users
import uuid

class UserRepository(BaseRepository):
    def create_user(self, user_data : UserInSignup):
        newUser = Users(
            username=user_data.username,
            password=user_data.password,  # map here
            role="Customer",
            created_at=datetime.datetime.now(ZoneInfo("Asia/Kolkata"))
        )

        self.session.add(instance = newUser)
        self.session.commit()
        self.session.refresh(instance = newUser)

        return newUser
    
    def user_exist_by_username(self , username : str):
        user = self.session.query(Users).filter(Users.username == username).first()
        if user is None : 
            return False
        return True
    
    def get_user_by_username(self , username : str):
        user = self.session.query(Users).filter(Users.username == username).first()
        if user: 
            return UserInDB(
                id=user.id,
                username=user.username,
                role=user.role,
                created_at=user.created_at,
                disabled=user.disabled,
                hashed_password=user.password,
            )
        else :
            return None       
    