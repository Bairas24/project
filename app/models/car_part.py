from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.db import Base

class CarPart(Base):
    __tablename__ = "car_part"
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    part_id = Column(Integer,ForeignKey('parts.id'), nullable=False)