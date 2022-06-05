from fastapi import FastAPI
from models.product_category import ProductCategory
from models.product import Product

import sys

app = FastAPI()


@app.get('/products')
async def get_products(category: ProductCategory = ProductCategory.none,
                       price_start: float = 0.0,
                       price_end: float = sys.float_info.max,
                       page: int = 0,
                       page_size: int = 50):
    return {'products': [category, price_start, price_end]}


@app.get('/products/{product_id}')
async def get_product_by_id(product_id: int):
    return {'product': {'id': product_id}}


@app.post('/products/')
async def create_product(product: Product):
    return {'product': Product}
