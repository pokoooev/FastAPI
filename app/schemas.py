from typing import Optional
from pydantic import BaseModel



class CategoryBase(BaseModel):
    title: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The title"
            }
        }

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True 


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[str] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True