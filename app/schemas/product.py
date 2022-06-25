from pydantic import BaseModel
from typing import List
from app.schemas.review import ReviewView


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str


class ProductView(ProductCreate):
    id: int
    reviews: List[ReviewView]

    class Config:
        orm_mode = True
