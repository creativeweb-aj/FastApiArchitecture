# Import models from app
from BaseApp.UserApp.models import User
from BaseApp.UserApp.modules import encrypt
import datetime


# Get all user method query
def getUser(db):
    return db.query(User).all()


# Create user method query
def createUser(data, db):
    dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
    # get encrypted password hash
    passHash = encrypt.get_password_hash(data.password)
    userObj = User(
        first_name=data.first_name,
        last_name=data.last_name,
        username=data.username,
        email=data.email,
        password=passHash,
        created_on=dateTime,
        updated_on=dateTime
    )
    db.add(userObj)
    db.commit()
    return userObj
