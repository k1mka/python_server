from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base_class import Base

DATABASE_URL = "postgresql://george@localhost:5432/products_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
