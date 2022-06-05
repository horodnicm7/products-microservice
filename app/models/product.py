from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str

    # def __repr__(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'price': self.price,
    #         'description': self.description
    #     }
