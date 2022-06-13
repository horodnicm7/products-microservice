from sqlalchemy.orm import Session
from app.sql.models.product import Product
from app.schemas.product import ProductCreate


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products_by_filters(db: Session, page_size=50, page_number=0, **kwargs):
    return db.query(Product).offset(page_number).limit(page_size).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    query = db.query(Product).filter(Product.id == product_id)
    query.delete(synchronize_session=False)
    db.commit()
    return query


def update_product(db: Session, product_id: int, product: ProductCreate):
    db.query(Product).filter(Product.id == product_id).update(product.dict())
    db.commit()
