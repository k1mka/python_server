from sqlalchemy.orm import Session
from app.models import ProductDB
from app.schemas.product_schema import Product

# CREATE
def create_product(db: Session, product: Product):
    db_product = ProductDB(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_products(db: Session, products: list[Product]):
    db_products = [ProductDB(**product.dict()) for product in products]
    db.add_all(db_products)
    db.commit()
    return db_products

# READ
def get_products(db: Session):
    return db.query(ProductDB).all()

def get_product(db: Session, product_id: int):
    return db.query(ProductDB).filter(ProductDB.id == product_id).first()

# UPDATE
def update_product(db: Session, product_id: int, updated_product: Product):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if product:
        for key, value in updated_product.dict().items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
    return product

# DELETE
def delete_product(db: Session, product_id: int):
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product
