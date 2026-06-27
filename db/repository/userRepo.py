import datetime
from gc import disable
from zoneinfo import ZoneInfo
from .base import BaseRepository
from models.Auth_Entities import (
    UserInDB,
    User,
    UserInSignup
)
from models.models import Users , UserRoles

class UserRepository(BaseRepository):

    def get_role_id_by_name(self , user_role : str):
        role_id = self.session.query(UserRoles).filter(UserRoles.role == user_role).first()
        return role_id.id if role_id else None    
    
    def get_role_by_id(self , id):
        role = self.session.query(UserRoles).filter(UserRoles.id == id).first()
        return role.role if role else None
    
    def create_user(self, user_data : UserInSignup):
        newUser = Users(
            username=user_data.username,
            password=user_data.password,  # map here
            role=self.get_role_id_by_name("customer"),
            created_at=datetime.datetime.now(ZoneInfo("Asia/Kolkata")),
            disabled = False 
        )

        self.session.add(instance = newUser)
        self.session.commit()
        self.session.refresh(instance = newUser)

        return User(
            id= newUser.id,
            username= newUser.username,
            role= self.get_role_by_id(newUser.role),
            created_at=newUser.created_at,
            disabled= newUser.disabled
        )
    
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
                role=self.get_role_by_id(user.role),
                created_at=user.created_at,
                disabled=user.disabled,
                hashed_password=user.password,
            )
        else :
            return None   