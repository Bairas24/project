from sqlalchemy import Column, Integer, String, DateTime, func
from app.core.db import Base

class Part(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    brand = Column(String, nullable=False)
    article = Column(String, unique=True, nullable=False) 
    description = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())