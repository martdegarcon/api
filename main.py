from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.models import Base
from schemas.schemas import Politician, PoliticianCreate
from crud.crud import create_politician, get_politicians  # <-- ВАЖНО!
from database import SessionLocal, engine

# Создаём таблицы в базе данных (если их ещё нет)
Base.metadata.create_all(bind=engine)

# Создаём экземпляр приложения FastAPI
app = FastAPI()

# Зависимость для подключения к базе данных
def get_db():
    """
    Получить сессию базы данных.
    Автоматически открывает и закрывает соединение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания нового политика
@app.post("/politicians/", response_model=Politician)
def create_politician_endpoint(politician: PoliticianCreate, db: Session = Depends(get_db)):
    """
    Создать нового политика.
    """
    return create_politician(db=db, politician=politician)

# Эндпоинт для получения списка политиков
@app.get("/politicians/", response_model=list[Politician])
def read_politicians(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получить список политиков с поддержкой пагинации.
    """
    return get_politicians(db=db, skip=skip, limit=limit)
