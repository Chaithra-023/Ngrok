from sqlalchemy.orm import Session
from model import User

class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, email: str, hashed_password: str):
        db_user = User(email=email, password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user