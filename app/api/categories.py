from unicodedata import category
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from fastapi.exception_handlers import http_exception_handler
from app.db import crud
from app.db.db import get_db
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", response_model=List[CategoryResponse])
def get_categories (
    db: Session = Depends(get_db)
):
    
    categories = crud.get_all_categories(db)
    return categories

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = crud.get_category(db, category_id=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} doesn't exists"
        )
    return category

@router.post("/", response_model = CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    existing = crud.get_category_by_title(db, title=category.title)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this title already exists"
        )
    return crud.create_category(db, title=category.title)

@router.put("/{category_id}", response_model = CategoryResponse)
def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    db: Session = Depends(get_db)
):
    category = crud.get_category(db, category_id=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} doesn't exists"
        )
    updated_category = crud.update_category(
        db,
        category_id = category_id,
        title = category_update.title
          )
    return updated_category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = crud.get_category(db, category_id=category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_NOT_FOUND,
            detail="Category with this title doesn't exists"
        )
    deleted = crud.delete_category(db, category_id = category_id)
    if not deleted:
                raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete category"
        )
    return None
