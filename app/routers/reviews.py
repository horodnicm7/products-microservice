from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.routers import dependencies
from app.schemas.review import ReviewCreate, ReviewView
from app.sql.crud import review as review_crud


router = APIRouter(
    prefix='/products',
    tags=['reviews']
)


@router.get('/{product_id}/reviews')
async def get_product_reviews(product_id: int, db: Session = Depends(dependencies.get_database_session)) -> ReviewView:
    return review_crud.get_reviews_by_product_id(db, product_id)


@router.post('/{product_id}/reviews')
async def create_product_review(product_id: int,
                                review: ReviewCreate,
                                db: Session = Depends(dependencies.get_database_session)):
    pass


@router.delete('/{product_id}/reviews/{review_id}')
async def delete_product_review(product_id: int,
                                review_id: int,
                                db: Session = Depends(dependencies.get_database_session)):
    pass
