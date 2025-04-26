# crud functions

from sqlalchemy.orm import Session
from models.models import Politician as PoliticianModel
from schemas.schemas import PoliticianCreate

# function for creating a new politician
def create_politician(db: Session, politician: PoliticianCreate):
    """
    Создать нового политика.
    """
    db_politician = PoliticianModel(**politician.dict())  # превращаем схему в модель
    db.add(db_politician)                                 # добавляем в сессию
    db.commit()                                           # сохраняем изменения в базу
    db.refresh(db_politician)                             # обновляем объект (получаем uuid, created_at)
    return db_politician

# function to get list of politicians
def get_politicians(db: Session, skip: int = 0, limit: int = 10):
    """
    Получить список политиков из базы данных.
    """
    return db.query(PoliticianModel).offset(skip).limit(limit).all()
