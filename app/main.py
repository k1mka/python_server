from fastapi import FastAPI
from app.models.database import Base, engine
from app.routers.product_router import router


# Создание таблиц
Base.metadata.create_all(bind=engine)

# Инициализация приложения
app = FastAPI()

# Подключение роутера
app.include_router(router)
