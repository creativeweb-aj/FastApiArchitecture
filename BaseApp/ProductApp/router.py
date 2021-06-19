from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
# get_db method from dependencies
from BaseApp.UserApp.schemas import UserResponse
from BaseApp.dependencies import get_db, get_current_user
from BaseApp.ProductApp.schemas import ProductResponse, CategoryResponse, ProductCreate, CategoryCreate
from BaseApp.ProductApp.query import addProduct, addCategory, getAllProducts, getAllCategory

# Create Router Instance of FastApi to create api's
api = APIRouter(tags=['Products'])


# Tag name for this app is blog || use tags=['blog']

# API's created here
@api.get("/products", response_model=List[ProductResponse], status_code=200)
async def allProducts(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    data = getAllProducts(db)
    return data


@api.post("/product-create", response_model=ProductResponse, status_code=201)
async def createProduct(data: ProductCreate, db: Session = Depends(get_db),
                        current_user: UserResponse = Depends(get_current_user)):
    data = addProduct(data, db)
    return data


@api.get("/categories", response_model=List[CategoryResponse], status_code=200)
async def allCategory(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    data = getAllCategory(db)
    return data


@api.post("/create-category", response_model=CategoryResponse, status_code=201)
async def createCategory(data: CategoryCreate, db: Session = Depends(get_db),
                         current_user: UserResponse = Depends(get_current_user)):
    data = addCategory(data, db)
    return data
