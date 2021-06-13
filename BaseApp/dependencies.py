# Local Session maker to get db session for database
# Import SessionLocal variable from database file
from BaseApp.database import SessionLocal


# Dependencies are created here

# To get db session by this get_db method
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
