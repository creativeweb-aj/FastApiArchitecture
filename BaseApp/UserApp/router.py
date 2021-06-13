from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from BaseApp.dependencies import get_db
from BaseApp.UserApp.schemas import UserCreateSchema, UserResponse
from BaseApp.UserApp.query import getUser, createUser

api = APIRouter()


@api.get("/users", response_model=List[UserResponse], status_code=200, tags=['user'])
async def users(db: Session = Depends(get_db)):
    data = getUser(db)
    return data


@api.post("/create-user", response_model=UserResponse, status_code=201, tags=['user'])
async def registerUser(userData: UserCreateSchema, db: Session = Depends(get_db)):
    data = createUser(userData, db)
    return data
