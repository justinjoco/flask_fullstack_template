from tracing.log import logger
from api.model.db import db
from api.model.cache import cache
from api.model.book import Book
'''
Save 
'''


def init_cache():
    logger.info(f"Pinging redis cache: {cache.health_check()}")
    books = Book.query.all()
    logger.info(f"Books: {books}")
    cache.save_all(books)
