"""app.py"""

from flask import Flask
from waitress import serve
from api.route.book_controller import book_api
from api.route.health_check_controller import health_check_api
from flask_cors import CORS
from api.database.book import Book
from api.repository.book_repository import book_repository
from api.database.db import db
from tracing.log import logger
from flask_migrate import Migrate
import os
from datetime import datetime
from decimal import Decimal
import uuid
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    env = os.getenv("FLASK_ENV")
    if env == "production":
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'
    # initialize the app with the extension
    db.init_app(app)

    migrate.init_app(app, db)
    ## Initialize Config
    app.register_blueprint(health_check_api)
    app.register_blueprint(book_api)

    return app


if __name__ == '__main__':
    logger.info("Starting server...")
    app = create_app()
    with app.app_context():
        book_repository.seed_db()
        book_repository.init_cache()
    serve(app, host="0.0.0.0", port=5000)
