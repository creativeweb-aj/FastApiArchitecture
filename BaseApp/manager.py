import uvicorn
from fastapi import FastAPI
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

# Include App to FastApi Instance
app.include_router(UserApp.router.api, prefix="/auth")
app.include_router(ProductApp.router.api, prefix="/product")


