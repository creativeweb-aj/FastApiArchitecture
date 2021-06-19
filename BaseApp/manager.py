import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# Import sql engine from database
from BaseApp.database import engine
# Import Apps module
from BaseApp import UserApp
from BaseApp import ProductApp
# Import models and router from App
from BaseApp.UserApp import models, router
from BaseApp.ProductApp import models, router

# No need to add or bind to database engine to our models here alembic do this
# Binding Apps models to database engine
# UserApp.models.Base.metadata.create_all(bind=engine)
# ProductApp.models.Base.metadata.create_all(bind=engine)

# FastApi Instance
app = FastAPI(
    title="FastApi Testing",
    description="This is tutorial of use fast api with user app",
    version="0.0.1",
)

# Add urls
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include App to FastApi Instance
app.include_router(UserApp.router.api, prefix="/auth")
app.include_router(ProductApp.router.api, prefix="/product")


