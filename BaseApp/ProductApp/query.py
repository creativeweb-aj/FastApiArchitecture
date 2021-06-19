from BaseApp.ProductApp.models import Product, Category
import datetime


def getCategory(id, db):
    return db.query(Category).filter_by(id=id, is_delete=False).first()


def getAllCategory(db):
    return db.query(Category).all()


def addCategory(data, db):
    dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
    category = Category(
        name=data.name,
        created_on=dateTime,
        updated_on=dateTime
    )
    db.add(category)
    db.commit()
    return category


def getProduct(id, db):
    return db.query(Product).filter_by(id=id, is_delete=False).first()


def getAllProducts(db):
    return db.query(Product).all()


def addProduct(data, db):
    dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
    category = getCategory(data.category, db)
    product = Product(
        name=data.name,
        detail=data.detail,
        category_id=category.id,
        created_on=dateTime,
        updated_on=dateTime
    )
    db.add(product)
    db.commit()
    return product
