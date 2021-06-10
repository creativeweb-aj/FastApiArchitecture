from fastapi import Depends, APIRouter, HTTPException, status
from BaseApp.UserApp import schemas

api = APIRouter()


@api.get("/")
def index():
    return {"key": "value"}
