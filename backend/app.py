"""app.py"""

from flask import Flask
from waitress import serve
from api.route.common import common_api
from api.route.customer import customer_api
from api.route.admin import admin_api
from flask_cors import CORS

from api.model.db import db
from tracing.log import logger


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"
               ] = "postgresql://admin:password@db/shopping_store"
    # initialize the app with the extension
    db.init_app(app)
    ## Initialize Config
    app.register_blueprint(common_api)
    app.register_blueprint(customer_api)
    app.register_blueprint(admin_api)

    return app


if __name__ == '__main__':
    logger.info("Starting server...")
    app = create_app()
    serve(app, host="0.0.0.0", port=5000)
