"""app.py"""

from flask import Flask
from waitress import serve
from api.route.book_controller import book_api
from flask_cors import CORS

from api.model.db import db
from tracing.log import logger


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"
               ] = "postgresql://admin:password@postgres/book_db"
    # initialize the app with the extension
    db.init_app(app)
    ## Initialize Config
    app.register_blueprint(book_api)

    return app


if __name__ == '__main__':
    logger.info("Starting server...")
    app = create_app()
    serve(app, host="0.0.0.0", port=5000)
