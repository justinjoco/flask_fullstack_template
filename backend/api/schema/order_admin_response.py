from flask_marshmallow import Schema
from marshmallow.fields import Str, Int, DateTime, Decimal, List, Nested
from api.schema.item_order import ItemOrder


class OrderAdminResponse(Schema):
    class Meta:
        # Fields to expose
        fields = ["id", "item_orders", "user_id", "order_price", "date_created"
                  ]

    id = Str()
    item_orders = List(Nested(ItemOrder))
    user_id = Str()
    order_price = Decimal()
    date_created = DateTime()
