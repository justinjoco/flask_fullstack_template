from api.model.book import Book

from tracing.log import logger
from api.model.db import db
from sqlalchemy import insert, update, delete
from uuid import uuid4


class BookService:
    def get_books(self):
        logger.info("Retrieving items from DB")
        return Book.query.all()

    def get_book_by_id(self, book_id):
        logger.info(f"Retrieving item with id {book_id} from DB")
        return Book.query.get_or_404(book_id)

    def update_book_by_id(self, book_id, book_update):
        logger.info(f"Updating book with id = {book_id}")
        Book.query.get_or_404(book_id)
        update_stmt = update(Book).where(Book.id == book_id).values(
            **book_update)
        db.session.execute(update_stmt)
        db.session.commit()
        return {"id": book_id, ** book_update}

    def delete_book_by_id(self, book_id):
        logger.info(f"Delete book where book id ={book_id}")
        delete_stmt = delete(Book).where(Book.id == book_id)
        db.session.execute(delete_stmt)
        db.session.commit()

    def insert_book(self, book):
        logger.info("Inserting new book into DB")
        book_to_insert = {"id": str(uuid4()), ** book}
        insert_stmt = insert(Book).values(book_to_insert)
        db.session.execute(insert_stmt)
        db.session.commit()
        return book_to_insert


book_service = BookService()
