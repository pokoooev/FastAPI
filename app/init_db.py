from app.db.db import engine  
from sqlalchemy import text
from app.db.models import Base      
from app.db.models import Category, Book

def init_database():
    Base.metadata.create_all(bind=engine)
    
    
    tables = list(Base.metadata.tables.keys())
    print(text(f"Таблицы созданы: {tables}"))
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_database();"))
        db_name = result.scalar()
        print(text(f"Подключены к базе данных: {db_name}"))

if __name__ == "__main__":
    init_database()