from fastapi import FastAPI
from app.api.users import router as users_router
from app.api.car import router as cars_router

app = FastAPI(
    title="My API",
    version="1.0.0"
)

# Подключаем роуты
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(cars_router, prefix="/cars", tags=["cars"])

@app.get("/")
def root():
    return {"message": "API is running"}
