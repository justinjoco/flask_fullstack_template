from redis import Redis
from tracing.log import logger

class Cache:
    def __init__(self, table_name: str):
        self.redis = Redis(host="cache",
                           port=6379,
                           username="default",
                           password="mypassword",
                           db=0)

        self.table_name = table_name

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass

    def save(self, object):
        pass

    def save_all(self, objects):
        logger.info(f"Objects: {objects}")
        pass

    def delete_by_id(self, id):
        pass

    def health_check(self):
        self.redis.ping()


cache = Cache("book")
