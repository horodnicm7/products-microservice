from pydantic import BaseModel


class ReviewCreate(BaseModel):
    author: str
    content: str
    rating: int


class ReviewView(ReviewCreate):
    id: str
    timestamp: str

    class Config:
        orm_mode = True
