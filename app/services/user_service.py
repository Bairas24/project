from sqlalchemy.orm import Session
from app.models.user import User


# Создание пользователя
def user_create(db: Session, email: str, password: str) -> User:
    new_user = User(email=email, password=password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user