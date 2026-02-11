from sqlalchemy.orm import Session
from app.models.car import Cars


# Создание функции логики БД
# Входные данные

def get_parts(db: Session, brand: str, model: str):
    cars = db.query(cars).where(Cars.brand == brand, Cars.model == model).all()

    return cars