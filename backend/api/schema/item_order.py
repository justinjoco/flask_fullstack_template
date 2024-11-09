from flask_marshmallow import Schema
from marshmallow.fields import Str, Int, DateTime, Decimal, Nested, Pluck
from api.schema.item_response import ItemResponse


class ItemOrder(Schema):
    class Meta:
        # Fields to expose
        fields = ["item", "amount_bought", "total_price", "date_created"]

    item = Pluck(ItemResponse, "name")
    amount_bought = Int()
    total_price = Decimal()
    date_created = DateTime()
