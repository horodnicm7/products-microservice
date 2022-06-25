from sqlalchemy.orm import Session
from app.sql.models.review import Review
from app.schemas.review import ReviewCreate


def get_reviews_by_product_id(db: Session, product_id: int):
    return db.query(Review).filter(Review.product_id == product_id).first()


def create_review(db: Session, review: ReviewCreate):
    db_review = Review(review)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    query = db.query(Review).filter(Review.id == review_id)
    query.delete(synchronize_session=False)
    db.commit()
    return query
