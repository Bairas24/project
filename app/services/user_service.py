from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password


# Создание пользователя
def user_create(db: Session, email: str, password: str) -> User:
    hashed_password = hash_password(password)
    new_user = User(email=email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Получение пользователя
def user_get(email: str, password: str, db: Session) -> User | None:
    user = db.query(User).where(User.email == email, User.password == password).first()

    if user and verify_password(plain_password=password, hashed_password=user.password):
        return user
    else:
        return None
