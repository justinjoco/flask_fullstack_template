from flask_sqlalchemy import SQLAlchemy
from api.model.base import Base

db = SQLAlchemy(model_class=Base)
