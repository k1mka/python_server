from fastapi import APIRouter, HTTPException, Depends
from app.models.database import get_db
from app.schemas.product_schema import Product, ProductList
from app.crud.product_crud import *

router = APIRouter()

# CREATE (добавить продукт)
@router.post("/products/", response_model=Product)
def create_new_product(product: Product, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.post("/products/bulk/", response_model=list[Product])
def create_multiple_products(products: ProductList, db: Session = Depends(get_db)):
    return create_products(db, products.products)

# READ
@router.get("/products/", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return product

# UPDATE
@router.put("/products/{product_id}", response_model=Product)
def update_existing_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = update_product(db, product_id, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return product

# DELETE
@router.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    product = delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return {"message": "Продукт удалён"}
