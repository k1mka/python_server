from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    productName = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    stock = Column(Integer)
    isAvailable = Column(Boolean)
