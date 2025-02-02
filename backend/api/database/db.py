from flask_sqlalchemy import SQLAlchemy
from api.database.base import Base

db = SQLAlchemy(model_class=Base)
