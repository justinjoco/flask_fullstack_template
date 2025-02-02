from api.repository.book import Book

from api.repository.db import db
from sqlalchemy import insert, update, delete
from api.repository.cache import cache, Cache


class BookRepository:
    def __init__(self, cache: Cache):
        self.cache = cache

    def find_all(self):
        return Book.query.all()

    def find_by_id(self, id):
        return Book.query.get_or_404(id)

    def insert(self, object):
        insert_stmt = insert(Book).values(object)
        db.session.execute(insert_stmt)
        db.session.commit()
        return object

    def update(self, id, object):
        Book.query.get_or_404(id)
        update_stmt = update(Book).where(Book.id == id).values(**object)
        db.session.execute(update_stmt)
        db.session.commit()
        return {"id": id, ** object}

    def delete_by_id(self, id):
        delete_stmt = delete(Book).where(Book.id == id)
        db.session.execute(delete_stmt)
        db.session.commit()

    def init_cache(self):
        pass


book_repository = BookRepository(cache)
