# Import models from app
from BaseApp.UserApp.models import User
from BaseApp.UserApp.modules import encrypt
import datetime


# Get all user method query
def getUser(data, db):
    return db.query(User).filter_by(username=data, is_delete=False).first()


def getUserByUsername(data, db):
    return db.query(User).filter_by(username=data.username, is_delete=False).first()


def getUserByEmail(data, db):
    return db.query(User).filter_by(email=data.email, is_delete=False).first()


def getAllUsers(db):
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


def authenticateUser(data, db):
    user = getUserByUsername(data, db)
    if not user:
        return False
    if not encrypt.verify_password(data.password, user.password):
        return False
    return True
