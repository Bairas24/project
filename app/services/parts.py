from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.car import Cars
from app.models.part import Part
from app.models.car_part import CarPart

# Создание функции логики БД
# Входные данные

def get_parts(db: Session, brand: str, model: str):
    # 1. получаем автомобили по brand и model
    cars = db.query(Cars).where(Cars.brand == brand, Cars.model == model).all()
    
    car_id_list = []
    for car in cars:
        car_id_list.append(car.id)
        
    # 2. получаем связи авто и запчасти по списку id из пункта 1
    cars_parts = db.query(CarPart).where(CarPart.car_id.in_(car_id_list)).all()

    parts_id = []
    for x in cars_parts:
        parts_id.append(x.part_id)
   
    # 3. получаем запчатси по списку id из пункта 2
    parts = db.query(Part).where(Part.id.in_(parts_id)).all()

    part_name_list = []
    for part in parts:
        part_name_list.append(part.name)

    return part_name_list

def get_parts_with_join(db: Session, brand: str, model: str):
    parts = db.query(Part.name).join(CarPart, CarPart.part_id == Part.id).join(Cars, Cars.id == CarPart.car_id).where(Cars.brand == brand, Cars.model == model).all()

    part_name_list = []
    for part in parts:
        part_name_list.append(part.name)

    return part_name_list

    # stmt = select(Part.name).join(CarPart, CarPart.part_id == Part.id).join(Cars, Cars.id == CarPart.car_id).where(Cars.brand == brand, Cars.model == model)
    # parts = db.execute(stmt).scalars().all()
    # return parts