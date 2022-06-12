import sys

from fastapi import APIRouter
from app.models.product_category import ProductCategory
from app.models.product import Product

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
async def create_product(product: Product):
    return {'product': Product}
