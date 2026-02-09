from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (        
    Mapped,                    
    mapped_column,                             
    declared_attr,             
    as_declarative             
)

@classmethod
@declared_attr
def __tablename__(cls) -> str:
    return cls.__name__.lower()


@as_declarative()
class Base:
    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class Category(Base):
    id: Mapped[int] = mapped_column(autoincrement = True, primary_key = True)
    title: Mapped[str] = mapped_column()

class Book(Base):
    id: Mapped[int] = mapped_column(autoincrement = True, primary_key = True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(nullable = True)
    price: Mapped[float] = mapped_column(nullable = True)
    url: Mapped[str] = mapped_column(nullable = True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'), nullable = True)