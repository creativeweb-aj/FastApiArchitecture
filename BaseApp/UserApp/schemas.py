from pydantic import BaseModel
from typing import Optional
import datetime
from fastapi import Body


class User(BaseModel):
    username: str


class UserCreate(User):
    password: str
    email: str
