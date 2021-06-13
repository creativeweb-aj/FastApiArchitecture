from pydantic import BaseModel


# User create schema
class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


# User response schema
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    is_active: bool
    updated_on: str

    # Required for ORM based response data to enable ORM mode
    class Config:
        orm_mode = True
