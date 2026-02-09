from fastapi import FastAPI

from app.api import books, categories

app = FastAPI(title="Bookstore API", version="1.0.0")
app.include_router(categories.router)
app.include_router(books.router)
@app.get("/")
def read_root():
    return {"message": "Bookstore API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

