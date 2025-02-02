from flask_sqlalchemy import SQLAlchemy
from api.repository.base import Base

db = SQLAlchemy(model_class=Base)
