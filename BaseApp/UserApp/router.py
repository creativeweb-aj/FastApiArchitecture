from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from BaseApp.dependencies import get_db
from BaseApp.UserApp.schemas import UserCreateSchema
from BaseApp.UserApp.models import User
import datetime

api = APIRouter()


@api.get("/users")
def users(db: Session = Depends(get_db)):
    data = db.query(User).all()
    return data


@api.post("/create-user")
def registerUser(userData: UserCreateSchema, db: Session = Depends(get_db)):
    dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
    userObj = User(
        first_name=userData.first_name,
        last_name=userData.last_name,
        username=userData.username,
        email=userData.email,
        password=userData.password,
        created_on=dateTime,
        updated_on=dateTime
    )
    db.add(userObj)
    db.commit()
    return {"status": "User created"}
