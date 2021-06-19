from typing import List

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_on: str

    # Required for ORM based response data to enable ORM mode
    class Config:
        orm_mode = True


class ProductResponse(BaseModel):
    id: int
    name: str
    detail: str
    category_id: int
    created_on: str

    # Required for ORM based response data to enable ORM mode
    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    name: str
    detail: str
    category: int


class CategoryCreate(BaseModel):
    name: str
