from app.core.db import SessionLocal
from app.models import User

# Создание пользователя
def user_create(email: str, password: str):
    new_user = User(email=email, password=password)
    
    SessionLocal.add(new_user)
    SessionLocal.commit()
    
    user = SessionLocal.refresh(new_user)
    
    return user
