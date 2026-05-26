from db.database import Base, engine
from models.models import Users , UserRoles

def create_tables():
    Base.metadata.create_all(bind = engine)