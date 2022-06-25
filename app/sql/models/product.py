from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.sql.database import Database
from app.schemas.product import ProductCreate


class Product(Database.base()):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)
    description = Column(String)

    review_ids = Column(Integer, ForeignKey('reviews.id'))

    reviews = relationship('Review', back_populates='products')

    def __init__(self, product: ProductCreate):
        self.name = product.name
        self.price = product.price
        self.description = product.description
