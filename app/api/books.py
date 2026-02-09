from typing import List
from unicodedata import category
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate
from sqlalchemy.orm import Session
from typing import Optional  
from fastapi import Query

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.get("/", response_model=List[BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по ID категории"),
    db: Session = Depends(get_db)
):
    if category_id:
        books = crud.get_books_by_category(db, category_id=category_id)
    else:
        books = crud.get_all_books(db)
    return books

@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = crud.get_book(db, book_id = book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} doesn't exist"
        )
    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate,
    db: Session=Depends(get_db)
):
    existing = crud.get_book_by_title(db, title=book.title)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Book with this title already exists"
        )
    return crud.create_book(db, title=book.title, description=book.description, price=book.price, url=book.url, category_id=book.category_id)


@router.put("/{book_id}", response_model= BookResponse)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_db)
):
    book = crud.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} doesn't exist"
        )
    if book_update.category_id is not None:
        book_category = crud.get_category(db, category_id=book_update.category_id)
        if book_category is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with {book_update.category_id} doesn't exist"
            )
    updated_book = crud.update_book(
        db,
        book_id=book_id,
        **book_update.dict(exclude_unset=True)
        )
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = crud.get_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with {book_id} doesn't exist"
        )
    deleted = crud.delete_book(db, book_id=book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete book"
        )
    return None