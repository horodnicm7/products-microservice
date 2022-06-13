from sqlalchemy.orm import Session
from app.sql.models.review import Review
from app.schemas.review import ReviewCreate


def get_review_by_id(db: Session, review_id: int):
    pass


def create_review(db: Session, review: ReviewCreate):
    pass


def delete_review(db: Session, review_id: int):
    pass
