from flask import Blueprint, request
from api.service.store import store_service
from api.schema.item_response import ItemResponse
from api.schema.order_admin_response import OrderAdminResponse
from api.schema.order_customer_response import OrderCustomerResponse

common_api = Blueprint('common_api', __name__)


@common_api.get('/items')
def items():
    result = store_service.get_items()
    return ItemResponse(many=True).dump(result), 200


@common_api.get('/item/<item_id>')
def get_specific_item(item_id):
    result = store_service.get_item(item_id)
    return ItemResponse().dump(result), 200


@common_api.get('/orders')
def orders():
    result = None
    role = request.headers.get("role")
    if role is not None and role == "admin":
        result = store_service.get_all_orders()
        return OrderAdminResponse(many=True).dump(result), 200

    user_id = request.headers["userId"]
    result = store_service.get_orders_by_user_id(user_id)
    return OrderCustomerResponse(many=True).dump(result), 200
