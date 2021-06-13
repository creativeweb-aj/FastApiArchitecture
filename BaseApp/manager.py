import uvicorn
from fastapi import FastAPI
# Import sql engine from database
from BaseApp.database import engine
# Import Apps module
from BaseApp import UserApp
# Import models and router from App
from BaseApp.UserApp import models, router

# Binding Apps models to database engine
UserApp.models.Base.metadata.create_all(bind=engine)

# FastApi Instance
app = FastAPI(
    title="FastApi Testing",
    description="This is tutorial of use fastapi with user app",
    version="0.0.1",
)

# Include App to FastApi Instance
app.include_router(UserApp.router.api, prefix="/users")

# Run FastApi to main
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
