from flask import Blueprint, request
from tracing.log import logger
from api.service.book_service import book_service
from api.schema.book_response import BookResponse
book_api = Blueprint('book_api', __name__)


@book_api.post('/book')
def insert_book():
    logger.info("Inserting book")
    book = request.json
    result = book_service.insert_book(book)
    return BookResponse().dump(result), 201


@book_api.get('/books')
def get_books():
    logger.info("Getting all books")
    result = book_service.get_books()
    return BookResponse(many=True).dump(result), 200


@book_api.get('/book/<book_id>')
def get_book_by_id(book_id):
    logger.info(f"Get book with id={book_id}")
    result = book_service.get_book_by_id(book_id)
    return BookResponse().dump(result), 200


@book_api.put('/book/<book_id>')
def update_book_by_id(book_id):
    logger.info(f"Updating book by id={book_id}")
    body = request.json
    result = book_service.update_book_by_id(book_id, body)
    return BookResponse().dump(result), 200


@book_api.delete('/book/<book_id>')
def delete_book_by_id(book_id):
    logger.info(f"Deleting book by id={book_id}")
    book_service.delete_book_by_id(book_id)
    return "Book has been deleted", 204
