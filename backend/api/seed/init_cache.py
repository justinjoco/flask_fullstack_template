from tracing.log import logger
from api.cache.redis import r
from api.model.db import db

def init_cache():
    logger.info(f"Pinging redis cache: {r.ping()}")
