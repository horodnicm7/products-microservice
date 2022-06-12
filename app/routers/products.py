import sys

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product_category import ProductCategory
from app.models.product import Product
from app.utils.configuration import Configuration
from app.sql.database import Database

Database.base().metadata.create_all(bind=Database.engine())


def get_database_session():
    db = Database.session()

    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/')
async def get_products(category: ProductCategory = ProductCategory.none,
                       price_start: float = 0.0,
                       price_end: float = sys.float_info.max,
                       page: int = 0,
                       page_size: int = 50):
    return {'products': [category, price_start, price_end]}


@router.get('/{product_id}')
async def get_product_by_id(product_id: int):
    return {'product': {'id': product_id}}


@router.post('/')
async def create_product(product: Product, db: Session = Depends(get_database_session)):
    db.add(product)
    db.commit()
    db.refresh(product)

    return {'product': Product}
