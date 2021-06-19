from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# Import Base variable of database from database
from BaseApp.database import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    detail = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
    created_on = Column(String(100), nullable=True)
    updated_on = Column(String(100), nullable=True)

    def __repr__(self):
        return 'Product name : %r' % self.name


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    is_delete = Column(Boolean, default=False, nullable=False)
    created_on = Column(String(100), nullable=True)
    updated_on = Column(String(100), nullable=True)
    product = relationship("Product", backref="category", lazy=True)

    def __repr__(self):
        return 'Category name : %r' % self.name
