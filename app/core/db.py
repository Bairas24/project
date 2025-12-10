from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from collections.abc import Generator
from sqlalchemy.orm import Session

from app.core.config import settings


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_user():
    return {"message": "Добро пожаловать"}
def User_login(Session):
    email = Session.username
    password = Session.password