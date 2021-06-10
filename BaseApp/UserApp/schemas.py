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
    password: str
    is_active: bool
    is_verify: bool
    is_delete: bool
    created_on: str
    updated_on: str


class UserList(BaseModel):
    data: List = UserResponse
