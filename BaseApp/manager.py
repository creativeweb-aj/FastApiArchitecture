from fastapi import Depends, FastAPI, HTTPException, status
from BaseApp.database import engine

# Import Apps here
from BaseApp import UserApp
from BaseApp.UserApp import models, router

# Binding Apps to database engine
UserApp.models.Base.metadata.create_all(bind=engine)

# FastApi Object
app = FastAPI()

# Include Apps to main fast app
app.include_router(UserApp.router.api, prefix="/users")
