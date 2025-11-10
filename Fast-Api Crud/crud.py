from sqlmodel import Session, select
from models import Book
from database import engine

def create_book(book:Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

def get_books():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books


def update_book(book_id: int, new_data: Book):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            return None
        book.title = new_data.title
        book.author = new_data.author
        book.year = new_data.year
        book.genre = new_data.genre
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

    
def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            return None
        session.delete(book)
        session.commit()
        return book
