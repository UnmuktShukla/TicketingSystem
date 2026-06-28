import uuid
from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.repository.userRepo import UserRepository
from models.Auth_Entities import RoleEscalation
from models.models import Users


class AdminService:
    def __init__(self , session : Session):
        self.__userRepository = UserRepository(session=session)

    def elscalate_priveleges(self , user_id : uuid.UUID , role : RoleEscalation):
        if not self.__userRepository.user_exist_by_id(user_id=user_id):
            raise HTTPException(status_code=400 , detail="User Does not Exist")

        user_role_id = self.__userRepository.get_role_id_by_name(role.role)
        self.__userRepository.update_role(user_id=user_id , role_id=user_role_id)
        
        return "Rights Escalated"


        

