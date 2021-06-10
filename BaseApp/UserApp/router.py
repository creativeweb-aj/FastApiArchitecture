from fastapi import Depends, APIRouter, HTTPException, status
from BaseApp.UserApp import schemas

api = APIRouter()


@api.get("/index")
def index():
    return {"key": "value"}
