from datetime import datetime
import uuid
from sqlalchemy import Boolean, Column, DateTime , ForeignKey , Integer , String, Uuid
from sqlalchemy.orm import Mapped, mapped_column 
from db.database import Base

class Users(Base):
    __tablename__ = 'users' 

    id : Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at : Mapped[datetime] = mapped_column(DateTime)
    username : Mapped[str] = mapped_column(String)
    password : Mapped[str] = mapped_column(String)
    role : Mapped[uuid.UUID] = mapped_column(ForeignKey("user_roles.id"))
    disabled : Mapped[bool] = mapped_column(Boolean)


class UserRoles(Base):
    __tablename__ = 'user_roles'

    id : Mapped[uuid.UUID] = mapped_column(Uuid , primary_key=True , default=uuid.uuid4)
    role : Mapped[str] = mapped_column(String , unique=True)


