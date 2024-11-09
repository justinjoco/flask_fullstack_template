from flask import Blueprint, request
from tracing.log import logger
from api.service.store import store_service
customer_api = Blueprint('customer_api', __name__)
'''
1. Implement these endpoints with userId as part of the request body
(Optional) 2. Put the userId in the JWT. Validate the JWT and parse the payload for the userId
'''


@customer_api.post('/items/purchase')
def purchase_items():
    user_id = request.headers["userId"]
    items_info = request.json
    logger.info(f"Purchasing items")
    result = store_service.purchase_items(user_id, items_info)
    return result, 201


@customer_api.post('/item/<item_id>/purchase')
def purchase_specific_item(item_id):
    user_id = request.headers["userId"]
    body = request.json
    count = body["count"]
    logger.info(f"Purchasing specific item with id {item_id}")
    result = store_service.purchase_specific_item(user_id, item_id, count)
    return result, 201
