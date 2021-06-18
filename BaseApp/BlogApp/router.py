from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
# get_db method from dependencies
from BaseApp.dependencies import get_db

# Create Router Instance of FastApi to create api's
api = APIRouter()


# Tag name for this app is blog || use tags=['blog']

# API's created here

@api.get("/", tags=['blog'])
def index():
    return {"data": "hello"}
