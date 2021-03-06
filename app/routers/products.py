from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product_category import ProductCategory
from app.schemas.product import ProductCreate
from app.sql.crud import product as product_crud
from app.routers import dependencies


router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/')
async def get_products(category: ProductCategory = ProductCategory.none,
                       price_start: float = 0.0,
                       price_end: float = 1000.0,
                       page_number: int = 0,
                       page_size: int = 50,
                       db: Session = Depends(dependencies.get_database_session)):
    filters = {
        'category': category,
        'price_start': price_start,
        'price_end': price_end
    }
    return product_crud.get_products_by_filters(db, page_size=page_size, page_number=page_number, **filters)


@router.get('/{product_id}')
async def get_product_by_id(product_id: int, db: Session = Depends(dependencies.get_database_session)):
    return product_crud.get_product_by_id(db, product_id)


@router.post('/')
async def create_product(product: ProductCreate, db: Session = Depends(dependencies.get_database_session)):
    return product_crud.create_product(db, product)


@router.put('/{product_id}')
async def update_product(product_id: int, product: ProductCreate,
                         db: Session = Depends(dependencies.get_database_session)):
    return product_crud.update_product(db, product_id, product)


@router.delete('/{product_id}')
async def delete_product(product_id: int, db: Session = Depends(dependencies.get_database_session)):
    return product_crud.delete_product(db, product_id)
