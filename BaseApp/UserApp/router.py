from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
# get_db method from dependencies
from BaseApp.dependencies import get_db
# Import schemas from app
from BaseApp.UserApp.schemas import UserCreateSchema, UserResponse
# Import queries from app
from BaseApp.UserApp.query import getUser, createUser

# Create Router Instance of FastApi to create api's
api = APIRouter()


# Tag name for this app is user || use tags=['user']

# API's created here

@api.get("/users", response_model=List[UserResponse], status_code=200, tags=['user'])
async def users(db: Session = Depends(get_db)):
    data = getUser(db)
    return data


@api.post("/create-user", response_model=UserResponse, status_code=201, tags=['user'])
async def registerUser(userData: UserCreateSchema, db: Session = Depends(get_db)):
    data = createUser(userData, db)
    return data
