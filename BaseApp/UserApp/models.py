from sqlalchemy import Boolean, Column, Integer, String
from BaseApp.database import Base


# Create database models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verify = Column(Boolean, default=True, nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
    created_on = Column(String(100), nullable=True)
    updated_on = Column(String(100), nullable=True)

    def __repr__(self):
        return 'User : %r' % self.username
