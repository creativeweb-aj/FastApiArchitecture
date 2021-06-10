from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


