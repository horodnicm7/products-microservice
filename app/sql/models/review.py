from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.sql.database import Database
from app.schemas.review import ReviewCreate


class Review(Database.base()):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    author = Column(String)
    content = Column(String)
    rating = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))

    products = relationship('Product', back_populates='reviews')

    def __init__(self, review: ReviewCreate):
        self.author = review.author
        self.content = review.content
        self.rating = review.rating
