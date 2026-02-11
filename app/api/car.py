from app.core.db import get_db
from fastapi import APIRouter, Depends, HTTPException
from app.services.parts import get_parts
from sqlalchemy.orm import Session

router = APIRouter()



@router.get("/")
def get_cars(brand: str, model: str, db: Session = Depends(get_db)):
    cars = get_parts(db=db, brand = brand, model = model)
    
    return cars