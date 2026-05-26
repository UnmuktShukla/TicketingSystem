from sqlalchemy import Boolean, Column, DateTime , ForeignKey , Integer , String
from db.database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(String , primary_key=True ,index = True )
    created_at = Column(DateTime , index=True)
    username = Column(String , index=True)
    password = Column(String , index=True)
    role = Column(Integer,index=True)
    disabled = Column(Boolean , default=True) 


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id = Column(String ,  primary_key=True , index=True)
    role = Column(String , index=True)


