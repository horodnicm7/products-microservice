from pydantic import BaseModel


class ReviewCreate(BaseModel):
    author: str
    content: str


class ReviewView(ReviewCreate):
    id: str
    timestamp: str

    class Config:
        orm_mode = True
