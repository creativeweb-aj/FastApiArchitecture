from sqlalchemy import Boolean, Column, Integer, String, DateTime
import datetime
from BaseApp.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
