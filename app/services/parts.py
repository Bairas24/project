from sqlalchemy.orm import Session
from app.models.car import Cars
from app.models.part import Part
from app.models.car_part import CarPart

# Создание функции логики БД
# Входные данные

def get_parts(db: Session, brand: str, model: str):
    cars = db.query(Cars).where(Cars.brand == brand, Cars.model == model).all()
    
    car_id_list = []
    for car in cars:
        car_id_list.append(car.id)
        print(car_id_list)
    cars_parts = db.query(CarPart).where(CarPart.car_id.in_(car_id_list)).all()



    parts_id = []
    for x in cars_parts:
        parts_id.append(x.part_id)
    print(parts_id)
   
    Parts = db.query(Part).where(Part.id.in_(parts_id)).all()
    part_name_list = []
    for part in Parts:
        part_name_list.append(part.name)
        print(part_name_list)
    return part_name_list



    #разобрать код 
    # вернуть список запчасти Parts
    # видосы про циклы + массивы 

    # cars_parts  - лист []

    # x -каждый элемент листа cars_parts 




