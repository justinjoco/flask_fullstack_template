from api.database.book import Book

from api.database.db import db
from sqlalchemy import insert, delete, update
from api.cache.cache import Cache
from api.cache.book_cache import book_cache
from tracing.log import logger
from typing import List
import uuid
from datetime import datetime
from decimal import Decimal
import pytz
from tzlocal import get_localzone

class BookRepository:
    def __init__(self, cache: Cache):
        self.cache = cache
        self.timezone = get_localzone()

    def find_all(self):
        cached_books = self.cache.find_all()
        #cached_books = None
        logger.info(f"Cached books: {cached_books}")
        return cached_books if cached_books is not None else Book.query.all()

    def find_by_id(self, id):
        cached_book = self.cache.find_by_id(id)
        logger.info(f"Cached book: {cached_book}")
        return cached_book if cached_book is not None else Book.query.get_or_404(id)

    def insert(self, new_book):
        insert_stmt = insert(Book).values(new_book)
        db.session.execute(insert_stmt)
        db.session.commit()
        self.cache.save(new_book)
        return new_book

    def update(self, id, book_update):
        book : Book = Book.query.get_or_404(id)
        update_stmt = update(Book).where(Book.id == id).values(**book_update)
        db.session.execute(update_stmt)
        db.session.commit()
        updated_book = {"id": id, **book.to_dict(), **book_update}
        self.cache.save(updated_book)
        return updated_book

    def delete_by_id(self, id):
        self.cache.delete_by_id(id)
        delete_stmt = delete(Book).where(Book.id == id)
        db.session.execute(delete_stmt)
        db.session.commit()

    def seed_db(self):
        logger.info("Seeding database")
        db.create_all()
        if Book.query.count() == 0:
            book1: Book = Book(id=uuid.UUID('75d78c06-f134-4d9c-b1ae-c3e28d312faa'), title = "Harry Potter", author = "JK Rowling", genre = "fantasy", description = "Kid goes to magic school",  rating = Decimal("9.2"), date_published=datetime(2004, 10, 19, 10, 23, 54, 0, self.timezone))
            book2 : Book = Book(id=uuid.UUID('1561d744-0124-4dbd-b43a-e37bca283c55'), title = "Percy Jackson", author = "Rick Riordan", genre = "fantasy", description = "Kid goes to magic camp",  rating = Decimal("9.0"), date_published=datetime(2010, 10, 19, 11, 23, 54, 0, self.timezone))
            book3 : Book = Book(id=uuid.UUID('12e78d1b-f003-4d9f-a71c-1e66b3ed660a'), title = "Twilight", author = "Stephanie Meyer", genre = "fantasy", description = "Girl falls in love with vampire",  rating = Decimal("6.0"), date_published=datetime(2004, 10, 19, 10, 23, 54, 0, self.timezone))
            book4 : Book = Book(id=uuid.UUID('027be1fa-eaaf-4a25-aa45-dc37a7fd9079'), title = "Star Wars", author = "George Lucas", genre = "sci-fi", description = "Kid goes on space adventure",  rating = Decimal("8"), date_published=datetime(2004, 10, 19, 10, 23, 54, 0, self.timezone))
            db.session.add_all([book1, book2, book3, book4])
            db.session.commit()
            print("Database seeded successfully!")
        else:
            print("Database already has data. Skipping seeding.")

    def init_cache(self):
        logger.info(f"Pinging redis cache: {book_cache.health_check()}")
        books: List[Book] = Book.query.all()
        books_as_maps = [book.to_dict() for book in books]
        self.cache.save_all(books_as_maps)


book_repository = BookRepository(book_cache)
