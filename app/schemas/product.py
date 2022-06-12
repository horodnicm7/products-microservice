from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str


class ProductView(ProductCreate):
    id: int

    class Config:
        orm_mode = True
