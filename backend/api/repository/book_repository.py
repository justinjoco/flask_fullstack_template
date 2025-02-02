from api.database.book import Book

from api.database.db import db
from sqlalchemy import insert, delete, update
from api.cache.cache import Cache
from api.cache.book_cache import book_cache
from tracing.log import logger
from typing import List

class BookRepository:
    def __init__(self, cache: Cache):
        self.cache = cache

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

    def init_cache(self):
        logger.info(f"Pinging redis cache: {book_cache.health_check()}")
        books: List[Book] = Book.query.all()
        books_as_maps = [book.to_dict() for book in books]
        self.cache.save_all(books_as_maps)


book_repository = BookRepository(book_cache)
