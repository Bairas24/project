from app.core.db import get_db
from fastapi import APIRouter, Depends
from app.services.user_service import user_create, user_get
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/auth")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    return user_create(db=db, email=email, password=password)

@router.get("/auth")
def get_user(email: str, password: str, db: Session = Depends(get_db)):
    return user_get(db=db, email=email, password=password)