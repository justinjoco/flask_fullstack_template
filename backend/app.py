"""app.py"""

from flask import Flask
from waitress import serve
from api.route.book_controller import book_api
from api.route.health_check_controller import health_check_api
from flask_cors import CORS
from api.repository.book_repository import book_repository
from api.database.db import db
from tracing.log import logger


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"
               ] = "postgresql://admin:password@postgres/app_db"
    # initialize the app with the extension
    db.init_app(app)
    ## Initialize Config
    app.register_blueprint(health_check_api)
    app.register_blueprint(book_api)

    return app


if __name__ == '__main__':
    logger.info("Starting server...")
    app = create_app()
    with app.app_context():
        book_repository.init_cache()
    serve(app, host="0.0.0.0", port=5000)
