from typing import List
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
# get_db method from dependencies
from BaseApp.dependencies import get_db, get_current_user
# Import schemas from app
from BaseApp.UserApp.schemas import UserCreateSchema, UserResponse, Token
# Import queries from app
from BaseApp.UserApp.query import getUserByEmail, getUserByUsername, getAllUsers, createUser, authenticateUser
from BaseApp.UserApp.modules.token import createAccessToken

# Create Router Instance of FastApi to create api's
api = APIRouter(tags=['Authentication'])


# Tag name for this app is user || use tags=['user']

# API's created here

@api.post("/token", response_model=Token)
async def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticateUser(form_data, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"Authorization": "Bearer"},
        )
    data = {"username": form_data.username}
    access_token = createAccessToken(data)
    return {"access_token": access_token, "token_type": "bearer"}


@api.post("/create-user", response_model=UserResponse, status_code=201)
async def registerUser(userData: UserCreateSchema, db: Session = Depends(get_db)):
    byUsername = getUserByUsername(userData, db)
    if byUsername:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail="Username already exist"
        )
    byEmail = getUserByEmail(userData, db)
    if byEmail:
        raise HTTPException(
            status_code=status.HTTP_208_ALREADY_REPORTED,
            detail="Email already exist"
        )
    data = createUser(userData, db)
    return data


@api.get("/users", response_model=List[UserResponse], status_code=200)
async def users(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    data = getAllUsers(db)
    return data

