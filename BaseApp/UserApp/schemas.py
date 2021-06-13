from typing import List
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    is_active: bool
    updated_on: str

    # It's required for orm db config to send db data
    class Config:
        orm_mode = True
