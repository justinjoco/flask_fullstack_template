from flask_marshmallow import Schema
from marshmallow.fields import Str, Decimal


class BookResponse(Schema):
    class Meta:
        # Fields to expose
        fields = ["id", "title", "author", "genre", "description", "rating",
                  "date_published"]

    id = Str()
    title = Str()
    author = Str()
    genre = Str()
    description = Str()
    rating = Decimal()
    date_published = Str()
