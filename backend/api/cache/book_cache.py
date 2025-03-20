from redis import Redis, from_url
from tracing.log import logger
from api.cache.cache import Cache
from typing import List, Dict
import os
class BookCache(Cache):
    def __init__(self, url):
        self.redis = from_url(f"{url}?decode_responses=True")

    def find_all(self):
        books = []
        keys = self.redis.scan_iter("book:*")
        for key in keys:
            books.append(self.redis.hgetall(key))
        return books if len(books) > 0 else None

    def find_by_id(self, id: str):
        return self.redis.hgetall(f"book:{id}")

    def save(self, book: Dict[str, any]):
        id = book.get("id")
        self.redis.hset(f"book:{id}", None, None, book)

    def save_all(self, books: List[Dict[str, any]]):
        logger.info(f"Books: {books}")
        for book in books:
            self.save(book)

    def delete_by_id(self, id):
        self.redis.delete(f"book:{id}")

    def health_check(self):
        return self.redis.ping()

book_cache = BookCache(os.getenv("REDIS_URL"))
