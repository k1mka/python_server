from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    productName: str
    description: str = None
    price: float
    stock: int
    isAvailable: bool

class ProductList(BaseModel):
    products: List[Product]
