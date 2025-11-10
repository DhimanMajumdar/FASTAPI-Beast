from fastapi import FastAPI , HTTPException
from typing import List
from models import Book
from crud import create_book, get_books, update_book, delete_book
from database import init_db


app=FastAPI(title='📚 FastAPI Crud App')

# create db tables when startup
@app.on_event("startup")
def on_startup():
    init_db()

# Create a new book
@app.post("/books/",response_model=Book)
def add_book(book:Book):
    new_book=create_book(book)
    return new_book

# Read all books
@app.get("/books/",response_model=List[Book])
def read_books():
    return get_books()

# 🟣 UPDATE an existing book by ID
@app.put("/books/{book_id}", response_model=Book)
def modify_book(book_id: int, book: Book):
    updated = update_book(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


# 🔴 DELETE a book by ID
@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    deleted = delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully!"}