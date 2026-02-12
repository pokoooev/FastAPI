from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, or_

from app.db.models import Category, Book



'''CRUD для категорий'''
def create_category(db: Session, title:str) :
    new_category = Category(title=title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def get_category(db: Session, category_id: int):

    return db.query(Category).filter(Category.id == category_id).first()


def get_category_by_title(db: Session, title: str):

    return db.query(Category).filter(Category.title == title).first()


def get_all_categories(db: Session):

    return db.query(Category).all()


def update_category(db: Session, category_id: int, title: str):
    category = db.query(Category).filter(Category.id == category_id).first()

    if category:
        category.title = title
        db.commit()
        db.refresh(category)

    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return True
    
    return False



'''CRUD для книг'''

def create_book(db: Session, title:str, description:str = None, price:float = None, url:str = None, category_id:int = None) :
    new_book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
        )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

def get_book(db: Session, book_id: int):

    return db.query(Book).filter(Book.id == book_id).first()


def get_book_by_title(db: Session, title: str):

    return db.query(Book).filter(Book.title == title).first()


def get_all_books(db: Session):

    return db.query(Book).all()

def get_books_by_category(db: Session, category_id: int):
    
    return db.query(Book).filter(Book.category_id == category_id).all()


def update_book(db: Session, book_id: int, **kwargs):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        for key, value in kwargs.items():
            if hasattr(book, key) and value is not None:
                setattr(book, key, value)
        db.commit()
        db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()
        return True
    
    return False
