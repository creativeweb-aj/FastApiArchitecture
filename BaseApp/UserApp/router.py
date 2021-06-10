from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from BaseApp.dependencies import get_db
from BaseApp.UserApp.schemas import UserCreateSchema, UserResponse, UserList
from BaseApp.UserApp.query import getUser, createUser
from typing import List
# from BaseApp.database import database

api = APIRouter()


# @api.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @api.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@api.get("/users", response_model=List[UserResponse], status_code=200)
async def users(db: Session = Depends(get_db)):
    data = getUser(db)
    print(data)
    return data


@api.post("/create-user", status_code=201)
async def registerUser(userData: UserCreateSchema, db: Session = Depends(get_db)):
    data = createUser(userData, db)
    return data
