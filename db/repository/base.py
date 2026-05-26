from sqlalchemy.orm import session

class BaseRepository:
    def __init__(self , session : session) -> None:
        self.session = session
