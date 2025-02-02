from tracing.log import logger
from api.repository.book_repository import book_repository
from uuid import uuid4


class BookService:
    def get_books(self):
        logger.info("Retrieving items from repo")
        return book_repository.find_all()

    def get_book_by_id(self, book_id):
        logger.info(f"Retrieving item with id {book_id} from repo")
        return book_repository.find_by_id(book_id)

    def update_book_by_id(self, book_id, book_update):
        logger.info(f"Updating book with id = {book_id}")
        return book_repository.update(book_id, book_update)

    def delete_book_by_id(self, book_id):
        logger.info(f"Delete book where book id ={book_id}")
        return book_repository.delete_by_id(book_id)

    def insert_book(self, book):
        logger.info("Inserting new book into repo")
        book_to_insert = {"id": str(uuid4()), ** book}
        return book_repository.insert(book_to_insert)


book_service = BookService()
