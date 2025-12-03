from app.core.db import get_db
from fastapi import APIRouter, Depends
from app.services.user_service import user_create
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/auth")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    return user_create(db=db, email=email, password=password)