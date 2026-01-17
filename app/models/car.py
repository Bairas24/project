from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False) 
    year_from = Column(Integer, nullable=True)
    year_to = Column(Integer, nullable=True)
    engine = Column(String, nullable=True)