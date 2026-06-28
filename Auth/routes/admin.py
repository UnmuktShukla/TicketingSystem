import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.utils.protectedRoutes import requireAdmin
from models.Auth_Entities import RoleEscalation, User
from service.AdminService import AdminService


adminRouter = APIRouter()

@adminRouter.patch("/users/{id}/role" , status_code=200)
def escalate_role(id: uuid.UUID , role: RoleEscalation , admin_user : User = Depends(requireAdmin) ,session : Session = Depends(get_db)):
    try :
        return AdminService(session=session).elscalate_priveleges(user_id=id , role=role)
    except Exception as error :
        print(error)
        raise error 